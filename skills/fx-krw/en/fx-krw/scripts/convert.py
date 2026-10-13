#!/usr/bin/env python3
"""
Convert foreign currency amounts to Korean won (KRW)

Fetches exchange rates from the Frankfurter API (v2) and multiplies them out.
Both the lookup and the arithmetic live in this script so that a language model
never has to guess a rate.

Two rate methods:
- Date rate: the value on --date (latest value when omitted)
- Period average: simple mean of the daily values between --start and --end

Examples:
    python convert.py --amount 391000000000 --currency USD
    python convert.py --amount 100000000 --currency JPY --date 2020-03-15
    python convert.py --amount 391000000000 --currency USD --start 2024-01-01 --end 2024-12-31
    python convert.py --amount 1500000 --currency EUR --provider ECB
    python convert.py --batch '[{"amount":1000000,"currency":"USD"},{"amount":5000,"currency":"EUR","start":"2020-01-01","end":"2020-12-31"}]'

Output: JSON. The caller pastes the `inline` and `footnote` fields as they are.
The `inline` and `footnote` strings are written in Korean notation on purpose
(units such as 조, 억, 만 and 원), because the skill adds KRW figures to Korean text.
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------
API_BASE = "https://api.frankfurter.dev/v2"
TARGET_CURRENCY = "KRW"
HTTP_TIMEOUT_SEC = 30
# The API answers 403 to Python's default User-Agent, so send our own identifier
HTTP_USER_AGENT = "fx-krw-skill/1.0"

# Provider code -> name used in the citation line. Codes not listed are printed as-is
# Full list of codes: https://api.frankfurter.dev/v2/providers
PROVIDER_NAMES = {
    "ECB": "ECB",       # European Central Bank
    "FRED": "FRED",     # Federal Reserve Bank of St. Louis
    "BOE": "BOE",       # Bank of England
    "BOC": "BOC",       # Bank of Canada
    "RBA": "RBA",       # Reserve Bank of Australia
    "IMF": "IMF",       # International Monetary Fund
    "NB": "Norges Bank",
    "DNB": "DNB",       # Danmarks Nationalbank
    "MAS": "MAS",       # Monetary Authority of Singapore
    "HKMA": "HKMA",     # Hong Kong Monetary Authority
}

# Korean name of each currency. Currencies not listed are printed as their ISO code
CURRENCY_NAMES_KR = {
    "USD": "달러",
    "EUR": "유로",
    "JPY": "엔",
    "CNY": "위안",
    "GBP": "파운드",
    "HKD": "홍콩달러",
    "SGD": "싱가포르달러",
    "AUD": "호주달러",
    "CAD": "캐나다달러",
    "CHF": "스위스프랑",
    "TWD": "대만달러",
    "INR": "루피",
    "THB": "바트",
    "VND": "동",
    "IDR": "루피아",
    "MYR": "링깃",
    "PHP": "페소",
    "MXN": "멕시코페소",
    "BRL": "헤알",
    "RUB": "루블",
    "ZAR": "랜드",
    "TRY": "리라",
    "SEK": "스웨덴크로나",
    "NOK": "노르웨이크로나",
    "DKK": "덴마크크로나",
    "NZD": "뉴질랜드달러",
    "AED": "디르함",
    "SAR": "리얄",
}

# Korean digit-grouping units
THRESHOLD_JO = 1_0000_0000_0000      # 1 jo  = 10^12
THRESHOLD_EOK = 1_0000_0000          # 1 eok = 10^8
THRESHOLD_MAN = 1_0000               # 1 man = 10^4

# Within a unit, values at or above these are printed as integers (e.g. 1,514조, 3,910억, 1,500만)
INTEGER_FROM_JO = 1000
INTEGER_FROM_EOK_MAN = 100
DECIMALS_JO = 2
DECIMALS_EOK_MAN = 1

# Decimals for the rate in the citation line. Rates below 1 (e.g. VND/KRW 0.05246)
# would be flattened by 2 decimals, so they keep 4
RATE_DECIMALS_DEFAULT = 2
RATE_DECIMALS_SMALL = 4

METHOD_SPOT = "spot"
METHOD_AVERAGE = "average"


class NoRateDataError(Exception):
    """Raised when the requested period has no rate values at all"""


def _format_decimal(value: float, max_decimals: int) -> str:
    """Round to at most max_decimals and drop trailing zeros

    e.g. 1312.00 -> '1,312', 1381.50 -> '1,381.5', 9.10 -> '9.1'
    """
    rounded = round(value, max_decimals)
    if rounded == int(rounded):
        return f"{int(rounded):,}"
    formatted = f"{rounded:,.{max_decimals}f}"
    return formatted.rstrip("0").rstrip(".")


def format_korean_amount(amount: float, unit_name: str) -> str:
    """Write an amount with Korean units 조, 억, 만 (e.g. '3,910억 달러', '540조 원')"""
    abs_amt = abs(amount)
    sign = "-" if amount < 0 else ""

    if abs_amt >= THRESHOLD_JO:
        value = abs_amt / THRESHOLD_JO
        decimals = 0 if value >= INTEGER_FROM_JO else DECIMALS_JO
        return f"{sign}{_format_decimal(value, decimals)}조 {unit_name}"

    if abs_amt >= THRESHOLD_EOK:
        value = abs_amt / THRESHOLD_EOK
        decimals = 0 if value >= INTEGER_FROM_EOK_MAN else DECIMALS_EOK_MAN
        return f"{sign}{_format_decimal(value, decimals)}억 {unit_name}"

    if abs_amt >= THRESHOLD_MAN:
        value = abs_amt / THRESHOLD_MAN
        decimals = 0 if value >= INTEGER_FROM_EOK_MAN else DECIMALS_EOK_MAN
        return f"{sign}{_format_decimal(value, decimals)}만 {unit_name}"

    return f"{sign}{abs_amt:,.0f} {unit_name}"


def format_rate(rate: float) -> str:
    """Build the rate string for the citation line"""
    decimals = RATE_DECIMALS_DEFAULT if rate >= 1 else RATE_DECIMALS_SMALL
    return _format_decimal(rate, decimals)


def get_currency_name_kr(currency_code: str) -> str:
    """Return the Korean currency name, or the ISO code if it is not listed"""
    return CURRENCY_NAMES_KR.get(currency_code.upper(), currency_code.upper())


def _get_json(url: str):
    """Call an API URL and return the parsed JSON"""
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": HTTP_USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_api_url(currency: str, date: Optional[str], provider: Optional[str]) -> str:
    """Build the API URL for a single date rate"""
    path = f"{API_BASE}/rate/{urllib.parse.quote(currency.upper())}/{TARGET_CURRENCY}"
    params = {}
    if date:
        params["date"] = date
    if provider:
        params["providers"] = provider
    if params:
        path += "?" + urllib.parse.urlencode(params)
    return path


def build_series_url(currency: str, start: str, end: str, provider: Optional[str]) -> str:
    """Build the API URL for the daily rates of a period"""
    params = {"from": start, "to": end, "base": currency.upper(), "quotes": TARGET_CURRENCY}
    if provider:
        params["providers"] = provider
    return f"{API_BASE}/rates?" + urllib.parse.urlencode(params)


def fetch_rate(currency: str, date: Optional[str] = None,
               provider: Optional[str] = None) -> dict:
    """Fetch one date rate

    Returns e.g. {"date": "YYYY-MM-DD", "rate": 1234.56, "method": "spot", "_url": "..."}
    """
    url = build_api_url(currency, date, provider)
    data = _get_json(url)
    data["method"] = METHOD_SPOT
    data["_url"] = url
    return data


def fetch_average(currency: str, start: str, end: str,
                  provider: Optional[str] = None) -> dict:
    """Fetch the daily rates of a period and take their simple mean

    The API sometimes prepends the last value before the period as the first item,
    so only dates between start and end go into the mean.
    Returns e.g. {"date": "2024-12-31", "rate": 1364.4, "method": "average",
                  "start": "2024-01-01", "end": "2024-12-31", "observations": 366, "_url": "..."}
    """
    if start > end:
        raise ValueError(f"start ({start}) is later than end ({end})")
    url = build_series_url(currency, start, end, provider)
    series = _get_json(url)
    points = [p for p in series if start <= p["date"] <= end]
    if not points:
        raise NoRateDataError(f"no {currency}/KRW rate values from {start} to {end}")
    rates = [p["rate"] for p in points]
    first_date = points[0]["date"]
    last_date = points[-1]["date"]
    return {
        "date": last_date,
        "rate": sum(rates) / len(rates),
        "method": METHOD_AVERAGE,
        "start": first_date,
        "end": last_date,
        "observations": len(rates),
        "_url": url,
    }


def build_result(amount: float, currency: str, provider: Optional[str],
                 rate_data: dict) -> dict:
    """Compute the KRW amount from a fetched rate and build the inline text and citation line"""
    rate = rate_data["rate"]
    rate_date = rate_data["date"]
    krw_amount = amount * rate

    currency_name_kr = get_currency_name_kr(currency)
    foreign_formatted = format_korean_amount(amount, currency_name_kr)
    krw_formatted = format_korean_amount(krw_amount, "원")

    # Citation format: "Source(year), title(link)"
    # Without a provider the value is Frankfurter's blend of many sources, so cite Frankfurter
    if provider:
        source_name = PROVIDER_NAMES.get(provider.upper(), provider.upper())
    else:
        source_name = "Frankfurter"
    year = rate_date.split("-")[0]
    if rate_data["method"] == METHOD_AVERAGE:
        # Show the first and last dates that actually went into the mean
        rate_label = f"{rate_data['start']} - {rate_data['end']} {currency}/KRW 일별 평균 환율"
    else:
        rate_label = f"{rate_date} {currency}/KRW 환율"
    footnote = (
        f"> {source_name}({year}), "
        f"{rate_label} {format_rate(rate)}원"
        f"({rate_data['_url']})"
    )

    result = {
        "amount_foreign": amount,
        "currency": currency,
        "currency_name_kr": currency_name_kr,
        "foreign_formatted": foreign_formatted,
        "rate": rate,
        "rate_method": rate_data["method"],
        "rate_date": rate_date,
        "provider": provider or "blended",
        "source_name": source_name,
        "krw_amount": krw_amount,
        "krw_formatted": krw_formatted,
        "inline": f"{foreign_formatted}(약 {krw_formatted})",
        "footnote": footnote,
        "source_url": rate_data["_url"],
    }
    if rate_data["method"] == METHOD_AVERAGE:
        result["period_start"] = rate_data["start"]
        result["period_end"] = rate_data["end"]
        result["observations"] = rate_data["observations"]
    return result


def get_rate_data(currency: str, date: Optional[str], start: Optional[str],
                  end: Optional[str], provider: Optional[str]) -> dict:
    """Pick the rate method that matches the arguments and fetch it"""
    if (start is None) != (end is None):
        raise ValueError("give start and end together")
    if start and date:
        raise ValueError("date cannot be combined with start/end")
    if start:
        return fetch_average(currency, start, end, provider)
    return fetch_rate(currency, date, provider)


def convert_single(amount: float, currency: str,
                   date: Optional[str] = None,
                   provider: Optional[str] = None,
                   start: Optional[str] = None,
                   end: Optional[str] = None) -> dict:
    """Look up and convert one amount"""
    currency = currency.upper()
    rate_data = get_rate_data(currency, date, start, end, provider)
    return build_result(amount, currency, provider, rate_data)


def describe_error(exc: Exception) -> dict:
    """Turn an exception into a JSON error the caller can read"""
    if isinstance(exc, urllib.error.HTTPError):
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code == 404:
            hint = "No rate for that date. The date may be in the future or before the currency's data start date"
        else:
            hint = "Check the currency code (ISO 4217), the date (YYYY-MM-DD) and the provider code"
        return {"error": "HTTPError", "status": exc.code, "message": body, "hint": hint}
    if isinstance(exc, NoRateDataError):
        return {"error": "NoRateData", "message": str(exc),
                "hint": "The whole period may be in the future or before the currency's data start date"}
    if isinstance(exc, urllib.error.URLError):
        return {"error": "URLError", "message": str(exc.reason),
                "hint": "Check the network connection and whether the API is up"}
    return {"error": type(exc).__name__, "message": str(exc)}


def convert_batch(items: list) -> list:
    """Convert several amounts

    Each (currency, date, period, provider) combination is fetched once.
    If one item fails, the other results are still returned and the failed item carries an error field.
    """
    cache = {}
    results = []
    for item in items:
        try:
            amount = float(item["amount"])
            currency = str(item["currency"]).upper()
            date = item.get("date")
            start = item.get("start")
            end = item.get("end")
            provider = item.get("provider")
            key = (currency, date, start, end, provider.upper() if provider else None)
            if key not in cache:
                cache[key] = get_rate_data(currency, date, start, end, provider)
            results.append(build_result(amount, currency, provider, cache[key]))
        except Exception as exc:  # handled per item so one failure does not block the rest
            error = describe_error(exc)
            error["input"] = item
            results.append(error)
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Convert foreign currency amounts to KRW (Frankfurter API)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--amount", type=float,
                        help="Foreign amount as a full number, no unit suffix (e.g. 1000000000)")
    parser.add_argument("--currency", type=str,
                        help="ISO 4217 currency code (e.g. USD, EUR, JPY)")
    parser.add_argument("--date", type=str, default=None,
                        help="Rate date YYYY-MM-DD; omit for the latest value")
    parser.add_argument("--start", type=str, default=None,
                        help="First day of the averaging period YYYY-MM-DD; use with --end")
    parser.add_argument("--end", type=str, default=None,
                        help="Last day of the averaging period YYYY-MM-DD; use with --start")
    parser.add_argument("--provider", type=str, default=None,
                        help="Provider code (e.g. ECB, FRED); omit for the blended value")
    parser.add_argument("--batch", type=str, default=None,
                        help='Several items as a JSON array, e.g. [{"amount":1000,"currency":"USD"}]')
    args = parser.parse_args()

    if args.batch:
        try:
            items = json.loads(args.batch)
        except json.JSONDecodeError as exc:
            print(json.dumps(describe_error(exc), ensure_ascii=False, indent=2), file=sys.stderr)
            sys.exit(1)
        print(json.dumps(convert_batch(items), ensure_ascii=False, indent=2))
        return

    if args.amount is None or args.currency is None:
        parser.error("give --amount together with --currency, or use --batch")

    try:
        result = convert_single(args.amount, args.currency, args.date, args.provider,
                                args.start, args.end)
    except Exception as exc:
        print(json.dumps(describe_error(exc), ensure_ascii=False, indent=2), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
