# Variance Analysis

The tool splits the gap between a budget (or the prior period) and actual results into price, mix and quantity effects. The same script measures how close forecasts came to actual results.

## Price, Mix and Quantity Effects

### Terms

| Term | Definition |
|---|---|
| Baseline (B) | Budget or prior-period actual used for comparison |
| Actual (A) | Result for the current period |
| Quantity (Q), price (P) | Volume and amount per unit for each item |
| Baseline mix | Baseline quantity of an item / total baseline quantity |
| Price effect | Gap caused by changes in unit price |
| Mix effect | Gap caused by shifts in item shares within total quantity |
| Quantity effect | Gap caused by a rise or fall in total quantity |

### Formulas

The script computes the values below for each item i and adds them across items.

```
price effect    = (actual price - baseline price) x actual quantity
mix effect      = (actual quantity - total actual quantity x baseline mix) x baseline price
quantity effect = (total actual quantity x baseline mix - baseline quantity) x baseline price
total variance  = actual price x actual quantity - baseline price x baseline quantity
```

- The three effects add up to the total variance exactly. The script checks this identity for each item and stops if it fails.
- Mix effect plus quantity effect equals `(actual quantity - baseline quantity) x baseline price`, often called the sales volume variance.
- With a single item the mix effect is 0.
- With `--basis margin`, the price columns hold unit margins and the script splits the profit variance the same way. The default `revenue` splits the revenue variance.
- A new item with baseline quantity 0 and an empty baseline price takes the actual price as its baseline price. Its variance lands in the mix effect.
- A dropped item with actual quantity 0 and an empty actual price takes the baseline price as its actual price.
- For payroll variance, enter grades or departments as items, headcount as quantity and average pay per person as price. The quantity effect then reads as the headcount effect, the mix effect as the grade mix effect and the price effect as the pay rate effect.

### Input Collection Order

1. Baseline (budget or prior period) and subject (revenue or profit)
2. Baseline quantity and baseline price for each item
3. Actual quantity and actual price for each item

### Input Format

```
item,budget_qty,budget_price,actual_qty,actual_price
Product A,1000,50,1100,48
Product B,500,80,450,82
Product C,0,,120,60
```

Set other column names with `--item-col`, `--bq-col`, `--bp-col`, `--aq-col` and `--ap-col`.

### Run Example

```
python scripts/variance.py mix --input examples/sales_variance.csv --chart variance_bridge.png
```

The chart is a waterfall from the baseline through the three effects to the actual result.

### Writing the Explanation

For each large variance, write two or three sentences covering:

- Direction (favorable or unfavorable to profit), amount and rate
- Which of the three effects drove the gap, and by how much
- The event behind the driver (a price cut, a product launch) and whether it repeats
- Follow-up actions (further investigation, forecast revision)

Put an event or variable other than the result itself in the cause position. List the largest drivers first, and mention offsetting drivers in the opposite direction.

## Forecast Accuracy

```
accuracy(period) = 1 - |actual - forecast| / |actual|
MAPE = mean of |actual - forecast| / |actual| across periods
```

- Periods with an actual of 0 have no defined ratio. The script leaves them out of MAPE and lists them.
- Input columns are `period`, `forecast` and `actual`.

```
python scripts/variance.py accuracy --input examples/forecast.csv
```

## Sources

> ACCA(2020), Examiner's report Performance Management (PM) July 2020(https://www.accaglobal.com/content/dam/acca/global/PDF-students/acca/f5/examinersreports/pm-examreport-june20.pdf)
