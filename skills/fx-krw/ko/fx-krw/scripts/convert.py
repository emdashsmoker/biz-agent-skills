#!/usr/bin/env python3
"""
외화 금액을 원화로 환산하는 스크립트

Frankfurter API(v2)에서 환율을 조회하고 곱셈으로 원화 금액을 계산한다.
환율 숫자를 언어 모델이 추정하지 않도록 조회와 계산을 모두 이 스크립트가 맡는다.

환율 방식은 두 가지다.
- 기준일 환율: --date로 지정한 날짜의 값 (생략하면 최신 값)
- 기간 평균 환율: --start와 --end 사이 일별 값의 단순 평균

사용 예:
    python convert.py --amount 391000000000 --currency USD
    python convert.py --amount 100000000 --currency JPY --date 2020-03-15
    python convert.py --amount 391000000000 --currency USD --start 2024-01-01 --end 2024-12-31
    python convert.py --amount 1500000 --currency EUR --provider ECB
    python convert.py --batch '[{"amount":1000000,"currency":"USD"},{"amount":5000,"currency":"EUR","start":"2020-01-01","end":"2020-12-31"}]'

출력: JSON. 호출한 쪽은 inline 필드와 footnote 필드를 그대로 사용한다.
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

# ---------------------------------------------------------------------------
# 설정값
# ---------------------------------------------------------------------------
API_BASE = "https://api.frankfurter.dev/v2"
TARGET_CURRENCY = "KRW"
HTTP_TIMEOUT_SEC = 30
# 파이썬 기본 User-Agent로 호출하면 API가 403을 반환하므로 별도 식별자를 쓴다
HTTP_USER_AGENT = "fx-krw-skill/1.0"

# 제공기관 코드를 출처 표기용 이름으로 바꾸는 표. 표에 없는 코드는 코드를 그대로 쓴다
# 전체 코드 목록: https://api.frankfurter.dev/v2/providers
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

# 통화 코드별 한국어 표기. 표에 없는 통화는 ISO 코드를 그대로 쓴다
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

# 한국식 자릿수 단위
THRESHOLD_JO = 1_0000_0000_0000      # 1조
THRESHOLD_EOK = 1_0000_0000          # 1억
THRESHOLD_MAN = 1_0000               # 1만

# 단위 안에서 이 값 이상이면 소수점 없이 정수로 표기 (예: 1,514조, 3,910억, 1,500만)
INTEGER_FROM_JO = 1000
INTEGER_FROM_EOK_MAN = 100
DECIMALS_JO = 2
DECIMALS_EOK_MAN = 1

# 출처 줄의 환율 표기 자릿수. 1 미만 환율(예: VND/KRW 0.05246)은 2자리로 줄이면
# 값이 뭉개지므로 4자리까지 남긴다
RATE_DECIMALS_DEFAULT = 2
RATE_DECIMALS_SMALL = 4

METHOD_SPOT = "spot"
METHOD_AVERAGE = "average"


class NoRateDataError(Exception):
    """요청한 기간에 환율 값이 하나도 없을 때 발생"""


def _format_decimal(value: float, max_decimals: int) -> str:
    """최대 max_decimals 자리까지 반올림하고 끝자리 0은 지운다

    예: 1312.00 -> '1,312', 1381.50 -> '1,381.5', 9.10 -> '9.1'
    """
    rounded = round(value, max_decimals)
    if rounded == int(rounded):
        return f"{int(rounded):,}"
    formatted = f"{rounded:,.{max_decimals}f}"
    return formatted.rstrip("0").rstrip(".")


def format_korean_amount(amount: float, unit_name: str) -> str:
    """금액을 조, 억, 만 단위로 표기한다 (예: '3,910억 달러', '540조 원')"""
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
    """출처 줄에 넣을 환율 문자열을 만든다"""
    decimals = RATE_DECIMALS_DEFAULT if rate >= 1 else RATE_DECIMALS_SMALL
    return _format_decimal(rate, decimals)


def get_currency_name_kr(currency_code: str) -> str:
    """통화의 한국어 표기를 돌려준다. 표에 없으면 ISO 코드를 돌려준다"""
    return CURRENCY_NAMES_KR.get(currency_code.upper(), currency_code.upper())


def _get_json(url: str):
    """API 주소를 호출하고 JSON을 돌려준다"""
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": HTTP_USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_api_url(currency: str, date: Optional[str], provider: Optional[str]) -> str:
    """기준일 환율 한 건을 조회하는 API 주소를 만든다"""
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
    """기간의 일별 환율을 조회하는 API 주소를 만든다"""
    params = {"from": start, "to": end, "base": currency.upper(), "quotes": TARGET_CURRENCY}
    if provider:
        params["providers"] = provider
    return f"{API_BASE}/rates?" + urllib.parse.urlencode(params)


def fetch_rate(currency: str, date: Optional[str] = None,
               provider: Optional[str] = None) -> dict:
    """기준일 환율 한 건을 받아온다

    반환 예: {"date": "YYYY-MM-DD", "rate": 1234.56, "method": "spot", "_url": "..."}
    """
    url = build_api_url(currency, date, provider)
    data = _get_json(url)
    data["method"] = METHOD_SPOT
    data["_url"] = url
    return data


def fetch_average(currency: str, start: str, end: str,
                  provider: Optional[str] = None) -> dict:
    """기간의 일별 환율을 받아 단순 평균을 계산한다

    API는 기간 시작 전의 마지막 값을 첫 항목으로 붙여 줄 때가 있으므로
    start와 end 사이의 날짜만 평균에 넣는다.
    반환 예: {"date": "2024-12-31", "rate": 1364.4, "method": "average",
             "start": "2024-01-01", "end": "2024-12-31", "observations": 366, "_url": "..."}
    """
    if start > end:
        raise ValueError(f"start({start})가 end({end})보다 늦음")
    url = build_series_url(currency, start, end, provider)
    series = _get_json(url)
    points = [p for p in series if start <= p["date"] <= end]
    if not points:
        raise NoRateDataError(f"{start}부터 {end}까지 {currency}/KRW 환율 값 없음")
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
    """조회한 환율로 원화 금액을 계산하고 본문용 문자열과 출처 줄을 만든다"""
    rate = rate_data["rate"]
    rate_date = rate_data["date"]
    krw_amount = amount * rate

    currency_name_kr = get_currency_name_kr(currency)
    foreign_formatted = format_korean_amount(amount, currency_name_kr)
    krw_formatted = format_korean_amount(krw_amount, "원")

    # 출처 표기 형식: "기관명(연도), 자료명(링크)"
    # 제공기관을 지정하지 않으면 여러 기관 값을 합친 Frankfurter 값이므로 Frankfurter로 표기
    if provider:
        source_name = PROVIDER_NAMES.get(provider.upper(), provider.upper())
    else:
        source_name = "Frankfurter"
    year = rate_date.split("-")[0]
    if rate_data["method"] == METHOD_AVERAGE:
        # 실제로 평균에 들어간 첫날과 마지막 날을 적는다
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
    """입력 인자에 맞는 환율 방식을 골라 조회한다"""
    if (start is None) != (end is None):
        raise ValueError("start와 end는 함께 입력")
    if start and date:
        raise ValueError("date와 start/end는 함께 쓸 수 없음")
    if start:
        return fetch_average(currency, start, end, provider)
    return fetch_rate(currency, date, provider)


def convert_single(amount: float, currency: str,
                   date: Optional[str] = None,
                   provider: Optional[str] = None,
                   start: Optional[str] = None,
                   end: Optional[str] = None) -> dict:
    """한 건을 조회하고 환산한다"""
    currency = currency.upper()
    rate_data = get_rate_data(currency, date, start, end, provider)
    return build_result(amount, currency, provider, rate_data)


def describe_error(exc: Exception) -> dict:
    """예외를 호출한 쪽이 읽을 수 있는 JSON 오류로 바꾼다"""
    if isinstance(exc, urllib.error.HTTPError):
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code == 404:
            hint = "해당 날짜에 환율이 없음. 미래 날짜이거나 통화의 데이터 시작일 이전일 수 있음"
        else:
            hint = "통화 코드(ISO 4217), 날짜(YYYY-MM-DD), 제공기관 코드를 확인"
        return {"error": "HTTPError", "status": exc.code, "message": body, "hint": hint}
    if isinstance(exc, NoRateDataError):
        return {"error": "NoRateData", "message": str(exc),
                "hint": "기간 전체가 미래이거나 통화의 데이터 시작일 이전일 수 있음"}
    if isinstance(exc, urllib.error.URLError):
        return {"error": "URLError", "message": str(exc.reason),
                "hint": "네트워크 연결 또는 API 가동 여부를 확인"}
    return {"error": type(exc).__name__, "message": str(exc)}


def convert_batch(items: list) -> list:
    """여러 건을 환산한다

    같은 (통화, 날짜, 기간, 제공기관) 조합은 한 번만 조회한다.
    한 건이 실패해도 나머지 결과는 돌려주고 실패한 건에는 error 필드를 담는다.
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
        except Exception as exc:  # 한 건의 실패가 전체 결과를 막지 않도록 건별로 처리
            error = describe_error(exc)
            error["input"] = item
            results.append(error)
    return results


def main():
    parser = argparse.ArgumentParser(
        description="외화 금액을 원화로 환산 (Frankfurter API)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--amount", type=float,
                        help="외화 금액, 단위 약칭 없이 숫자 전체 (예: 1000000000)")
    parser.add_argument("--currency", type=str,
                        help="ISO 4217 통화 코드 (예: USD, EUR, JPY)")
    parser.add_argument("--date", type=str, default=None,
                        help="기준일 YYYY-MM-DD, 생략하면 최신 값")
    parser.add_argument("--start", type=str, default=None,
                        help="기간 평균의 시작일 YYYY-MM-DD, --end와 함께 사용")
    parser.add_argument("--end", type=str, default=None,
                        help="기간 평균의 종료일 YYYY-MM-DD, --start와 함께 사용")
    parser.add_argument("--provider", type=str, default=None,
                        help="제공기관 코드 (예: ECB, FRED), 생략하면 여러 기관 값을 합친 값")
    parser.add_argument("--batch", type=str, default=None,
                        help='여러 건을 JSON 배열로 입력. 예: [{"amount":1000,"currency":"USD"}]')
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
        parser.error("--amount와 --currency를 함께 입력하거나 --batch를 사용")

    try:
        result = convert_single(args.amount, args.currency, args.date, args.provider,
                                args.start, args.end)
    except Exception as exc:
        print(json.dumps(describe_error(exc), ensure_ascii=False, indent=2), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
