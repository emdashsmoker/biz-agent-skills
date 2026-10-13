---
name: fx-krw
description: "Adds a Korean won (KRW) equivalent next to every foreign currency amount in a text. Use this skill when the user explicitly asks with \"/fx-krw\", \"/환율병기\", \"add KRW\", \"show the won equivalent\", \"convert to Korean won\", \"원화 병기\", \"원화 환산\" or similar. Do not apply it without such a request. It finds amounts written as ISO 4217 codes, currency symbols, or Korean and English currency names, rewrites them as \"3,910억 달러(약 N조 원)\" and leaves a quote-block citation with the rate basis, currency pair, rate and lookup URL. The bundled scripts/convert.py fetches rates from the public Frankfurter API (no API key) and does the arithmetic, so the model never estimates a rate. Rates follow IAS 21 by default: period amounts (revenue) use the period's average rate, point-in-time balances (assets) use that date's rate, current values and forecasts use the latest rate. If the user asks for a period-end or year-end rate, period amounts use the last day of the period."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# fx-krw

> This English version was translated from the Korean original. It may work differently from what the original intends. Where the two disagree, follow the Korean version.

The skill writes a KRW equivalent next to each foreign currency amount. Rates come from the Frankfurter API and `scripts/convert.py` does the averaging and the multiplication. A language model that writes rates from memory tends to produce wrong numbers that look plausible, so every rate and every converted figure comes from the script output.

The script prints its results in Korean notation (units 조, 억, 만 and 원) because the skill targets Korean text. Keep that notation as it is.

## Rules

- Use only the script output for rates and KRW amounts. The model does not estimate a rate and does not do any foreign-to-KRW arithmetic itself.
- Use the rate that fits what the amount is and when it applies. Do not apply today's rate to past results.
- Leave the rate date or period, currency pair, rate and lookup URL in a quote block. Readers can open the URL to fetch the same value.

## Steps

### Step 1. Find the foreign amounts

Find every amount written in the forms below. The won sign ₩ and "원" are out of scope.

| Form | Examples |
|---|---|
| ISO 4217 code | USD, EUR, JPY, CNY, GBP, HKD, SGD, AUD, CAD, CHF, TWD, INR |
| Currency symbol | $, €, ¥, £ |
| Korean currency name | 달러, 유로, 엔, 위안, 파운드, 홍콩달러, 싱가포르달러 |
| English currency name | dollar, euro, yen, yuan, pound |
| Amount with a unit suffix | $391B, €1.5M, ¥100B |

### Step 2. Pick the rate

The default follows the foreign currency translation method of IAS 21. IAS 21 translates assets and liabilities at the rate on the reporting date and income and expenses at the rates on the transaction dates. It also allows an average rate for the period in place of transaction-date rates (IAS 21 paragraphs 39 and 40). The texts this skill handles rarely show individual transaction dates, so period amounts use the period's average rate.

Decide what kind of amount it is, then pick the rate from the table.

| Kind of amount | Examples | Rate | Script arguments |
|---|---|---|---|
| A transaction on a specific date | Contract value on 15 June 2023 | Rate on that date | `--date 2023-06-15` |
| An amount that builds up over a period | Annual revenue, quarterly costs, monthly exports, annual market size, annual investment | Average of the daily rates in that period | `--start 2022-01-01 --end 2022-12-31` |
| A balance at a point in time | Total assets at year end, debt, foreign reserves, market cap on a given date | Rate at that point. If only a year is given, the last day of that year | `--date 2022-12-31` |
| A current value, a value with no time stated, or a forecast | Current market cap, market size forecast for 2030 | Latest value | no rate arguments |

- If you cannot tell a period amount from a balance, treat it as a period amount.
- The period's start and end are the period the amount refers to. A calendar year runs from 1 January to 31 December. A month runs from its first day to its last day.
- For a company whose fiscal year does not end in December, use the first and last day of that fiscal year. FY2022 of a company closing in September runs from 2021-10-01 to 2022-09-30.
- When the period runs past today (e.g. year-to-date revenue), the script averages up to the last available day. The citation line shows the first and last days that went into the average.
- When the time is unclear, use the latest value.
- Future dates have no data and return an error. Look up forecasts without date arguments.
- Data start dates differ by currency. KRW rates are available from 2 January 1981 (checked September 2026). See `https://api.frankfurter.dev/v2/currencies` for each currency's start date.

#### Period-end rate option

When the user asks for a "period-end rate", "year-end rate", "기말 환율", "연말 환율" or similar, period amounts use `--date` with the last day of the period in place of `--start` and `--end`. The other three kinds stay as in the default.

| Kind of amount | Default | Period-end option |
|---|---|---|
| Annual revenue for 2022 | `--start 2022-01-01 --end 2022-12-31` | `--date 2022-12-31` |
| Exports in June 2023 | `--start 2023-06-01 --end 2023-06-30` | `--date 2023-06-30` |

### Step 3. Write the amount as a full number

The script cannot read unit suffixes such as B, M or 억. The model rewrites the amount as a full number for `--amount`. This step only changes the digits. No rate is applied here.

| Original | `--amount` |
|---|---|
| $391B | 391000000000 |
| €1.5M | 1500000 |
| ¥100B | 100000000000 |
| £750k | 750000 |
| $1.2T | 1200000000000 |
| 50억 달러 | 5000000000 |
| 3,000만 유로 | 30000000 |

### Step 4. Run the script

Pass the ISO 4217 code for the currency (see "Currency names and codes" below).

```bash
# One amount at the latest rate
python <skill folder>/scripts/convert.py --amount 391000000000 --currency USD

# One amount at a given date
python <skill folder>/scripts/convert.py --amount 100000000 --currency JPY --date 2020-03-15

# One amount at a period average
python <skill folder>/scripts/convert.py --amount 391000000000 --currency USD --start 2024-01-01 --end 2024-12-31

# Use one provider only (e.g. the European Central Bank)
python <skill folder>/scripts/convert.py --amount 1500000 --currency EUR --provider ECB

# Several amounts in one run
python <skill folder>/scripts/convert.py --batch '[{"amount":391000000000,"currency":"USD","start":"2024-01-01","end":"2024-12-31"},{"amount":50000000,"currency":"EUR","date":"2024-06-30"}]'
```

- Do not combine `--date` with `--start`/`--end`. Give `--start` and `--end` together.
- The period average is the simple mean of the daily values the API returns inside the period. The blended default has a value for every day including weekends. With a single provider, only the days that provider published go in.
- When a text has three or more foreign amounts, run them together with `--batch`. Amounts that share currency, date or period, and provider trigger one lookup.
- In `--batch`, one failed item does not stop the others. The failed item comes back with `error` and `hint` fields that explain why.
- Without `--provider` the script uses Frankfurter's blended value across many sources. Provider codes are listed at `https://api.frankfurter.dev/v2/providers`.

### Step 5. Insert the results

Replace the original amount with the `inline` value from the JSON output. Put the `footnote` value right after the list item or paragraph that holds the amount.

### Worked examples

Steps 2 to 5 applied to sample text. Company names and amounts are for illustration.

| Original text | `--amount` | `--currency` | Rate arguments | Why this rate |
|---|---|---|---|---|
| Company A 2023 revenue $96.8B | 96800000000 | USD | `--start 2023-01-01 --end 2023-12-31` | Builds up over a period |
| Company B total assets at end of 2023 $120B | 120000000000 | USD | `--date 2023-12-31` | Balance at a point in time |
| Market size forecast of $1.5T for 2030 | 1500000000000 | USD | none | Forecast |
| Company C market cap about $3.5T | 3500000000000 | USD | none | No time stated |
| Company D 2024 revenue $391B | 391000000000 | USD | `--start 2024-01-01 --end 2024-12-31` | Builds up over a period |
| Company E 2024 revenue €175B | 175000000000 | EUR | `--start 2024-01-01 --end 2024-12-31` | Builds up over a period |

When a text holds several amounts, as in the last two rows, run them together with `--batch`.

## Output format

In the example below, the parts in `<>` are filled from the script output.

```
- A사의 2024년 매출은 3,910억 달러(약 <KRW amount>)

> Frankfurter(2024), 2024-01-01 - 2024-12-31 USD/KRW 일별 평균 환율 <rate>원(https://api.frankfurter.dev/v2/rates?from=2024-01-01&to=2024-12-31&base=USD&quotes=KRW)

- A사의 2024년 말 총자산은 1,200억 달러(약 <KRW amount>)

> Frankfurter(2024), 2024-12-31 USD/KRW 환율 <rate>원(https://api.frankfurter.dev/v2/rate/USD/KRW?date=2024-12-31)
```

- The citation line follows the form "Source(year), title(link)". Without `--provider` the source is Frankfurter. With `--provider` it is that institution (ECB, FRED, etc.).
- A period-average citation shows the first and last days that went into the average. The year is the year of the last day.
- Write a citation line for a given date or period and currency pair once, where it first appears.
- When the date, the period or the currency pair differs, write a separate citation line and leave a blank line between blocks.
- When a citation block sits next to the source block of another statistic, separate them with a blank line.

### Number notation

The script writes amounts with the Korean units 조 (10^12), 억 (10^8) and 만 (10^4). The model uses the `inline` value as it is. The rules are below. Trailing zeros after the decimal point are dropped.

| Range | Notation | Examples |
|---|---|---|
| 1조 or more | Two decimals below 1,000조, integer from 1,000조 | 1.5조, 14.73조, 1,514조 |
| 1억 up to 1조 | One decimal below 100억, integer from 100억 | 1.5억, 14.7억, 3,910억 |
| 1만 up to 1억 | One decimal below 100만, integer from 100만 | 1.5만, 14.7만, 1,500만 |
| Below 1만 | Integer | 9,800 |

The rate in the citation line has two decimals. Rates below 1 (e.g. Vietnamese dong) keep four.

## Currency names and codes

| Name or symbol | Code | Name or symbol | Code |
|---|---|---|---|
| 달러, $ | USD | 유로, € | EUR |
| 엔, ¥ | JPY | 위안, 元 | CNY |
| 파운드, £ | GBP | 홍콩달러 | HKD |
| 싱가포르달러 | SGD | 호주달러 | AUD |
| 캐나다달러 | CAD | 스위스프랑 | CHF |
| 대만달러 | TWD | 루피 | INR |
| 바트 | THB | 동(베트남) | VND |

A bare "$" can be US, Canadian, Australian, Hong Kong or Singapore dollars. Decide from surrounding information such as the country of the source. If you cannot decide, treat it as USD and state the assumption in the text.

```
- (가정) "$" 표기는 미국 자료이므로 USD로 해석
```

The full list of supported currencies is at `https://api.frankfurter.dev/v2/currencies`.

## Exceptions

| Situation | Script signal | Handling |
|---|---|---|
| Network error or API outage | `URLError` or a 5xx error | Keep the foreign amount only and note the failed lookup at the end of the text |
| Unsupported currency (minor currencies, digital assets, etc.) | 422 error | Keep the foreign amount only and note the reason on that item |
| No rate for the date | 404 error | For a future date, look up again without date arguments. For a date before the data start, handle it like an unsupported currency |
| No rate anywhere in the period | `NoRateData` error | If the whole period is in the future, look up again without date arguments. If it is before the data start, handle it like an unsupported currency |
| Ambiguous currency unit | none | Convert with the most likely currency and state the assumption in the text |

Write lookup failures and unsupported currencies like this.

```
> (환율 조회 실패) Frankfurter API가 응답하지 않아 일부 외화의 원화 병기를 생략함. 나중에 다시 조회 필요

- (해당 외화) Frankfurter 미지원 통화로 원화 병기 생략
```

## When not to convert

- A currency symbol used for something other than an amount, such as "$" in a variable name, a regular expression or a code literal.
- An amount the user asked to leave without KRW.
- Comparisons that only make sense in the foreign currency, such as a global revenue ranking or a time series kept in foreign currency. The user may drop some or all KRW figures here.

## About the rates and the external service

- Frankfurter collects reference rates published by central banks and public institutions. These differ from the buy and sell rates banks and card networks apply to transactions.
- Without `--provider` the value is a blend of several sources. The last decimals can shift as new data arrives, so the same URL may return a slightly different value later. For figures that must stay fixed, pick one provider with `--provider`.
- Frankfurter is a public service run by a third party. It needs no API key and limits excessive requests. Rate data is subject to each provider's terms, so keep the citation lines when you publish the text.
- To use a self-hosted Frankfurter server, change `API_BASE` at the top of `scripts/convert.py` to that server's address.

## Requirements

- Python 3.8 or later
- Standard library only, nothing to install
- Internet access to `api.frankfurter.dev`
