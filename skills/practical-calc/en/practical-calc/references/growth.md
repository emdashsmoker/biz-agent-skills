# Growth Rate and Real-Price Conversion

Both tools work on yearly values. CAGR measures the average yearly growth between two points in time. Real-price conversion removes price changes so that amounts from different years sit at the same price level.

## CAGR

CAGR (compound annual growth rate) is the yearly rate at which the start value, growing by the same rate each year, would reach the end value.

```
CAGR = (end value / start value) ^ (1 / n) - 1
n = end year - start year
```

- n is the number of years between the two points. Comparing 2020 with 2024 uses five observations and n = 4.
- CAGR has no definition when the start value is 0 or below or the end value is negative. The script stops and reports the cause in those cases.
- For spacing other than whole years, set the period with `--years`. Thirty months is 2.5.
- With a series file, the script uses the earliest and latest years and also prints year-over-year changes.

### Input Collection Order

1. Start value and end value
2. Start year and end year

A full series comes as a CSV or XLSX with the columns `year` and `value`. Set other column names with `--year-col` and `--value-col`.

### Run Examples

```
python scripts/cagr.py --start-value 1200 --end-value 1820 --start-year 2020 --end-year 2024
python scripts/cagr.py --input examples/series.csv --chart cagr.png
```

### Reporting

Show the calculation table first, then give the result as a percentage in its own code block so the user can copy it.

## Real-Price Conversion

A nominal value is measured at the prices of its own year. A real value is the same amount measured at the prices of the price base year. Nominal values in years of rising prices overstate the change in volume, so comparisons across years use real values.

```
real value(t) = nominal value(t) x price index(price base year) / price index(t)
```

- Pick a price index that matches the nature of the amounts. Article 49 of Korea's General Guidelines for Conducting Preliminary Feasibility Studies uses the construction investment GDP deflator for costs and the consumer price index for benefits, and asks for a stated reason when another index is used.
- Korean price indices and deflators are available from the Bank of Korea Economic Statistics System (ECOS).
- If the input lacks the index for the price base year, the script stops and reports it.
- The output lists nominal CAGR and real CAGR. (1 + nominal CAGR) / (1 + real CAGR) - 1 equals the average yearly rise of the price index over the same period.

### Input Format

A CSV or XLSX with the columns `year`, `nominal` and `index`. Set other column names with `--year-col`, `--value-col` and `--index-col`.

```
year,nominal,index
2024,121,106.0
2025,130,108.3
```

### Run Example

```
python scripts/deflate.py --input examples/nominal.csv --base-year 2025 --chart real.png
```

## Sources

> Ministry of Planning and Budget, Republic of Korea(2026), 예비타당성조사 수행 총괄지침 (General Guidelines for Conducting Preliminary Feasibility Studies) Article 49(https://www.law.go.kr/행정규칙/예비타당성조사수행총괄지침)

> Bank of Korea, Economic Statistics System(https://ecos.bok.or.kr)
