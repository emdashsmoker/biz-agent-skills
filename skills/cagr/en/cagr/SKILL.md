---
name: cagr
description: Calculates the compound annual growth rate (CAGR) from two values at two points in time. The bundled scripts/cagr.py script does all the math. Use this skill whenever the user types "/cagr", mentions "CAGR", "compound annual growth rate", "annual growth rate", "average yearly growth", or asks how much something grew per year on average given a start-year value and an end-year value. Also use it to compute CAGR for time-series figures while writing a report or analysis.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# CAGR Calculator

> This English version was translated from the Korean original. It may behave differently from what the original intended.

This skill calculates the compound annual growth rate (CAGR) from two values at two points in time. A number the model works out in its head leaves no trace, so nobody can check it. The result must come from running code.

## Inputs

The calculation needs four values.

- Start value (the value in the start year)
- End value (the value in the end year)
- Start year
- End year

Users often give these in a sentence, such as "revenue went from $1,200M in 2020 to $1,850M in 2025". Pull the four values out of the sentence. Both values must be in the same unit. If any of the four is missing, ask the user.

## Formula

```
CAGR = (end_value / start_value) ^ (1 / n) - 1
n = end_year - start_year
```

n is the difference between the two years. From 2020 to 2025, n is 5, even though the data covers six calendar years.

The formula works only when all of these conditions hold. If an input breaks one, the script prints the reason and stops.

- The end year is greater than the start year
- The start value is greater than 0
- The end value is 0 or greater

## How to calculate

If Python is available, run the bundled script. Thousands separators are fine as input.

```bash
python scripts/cagr.py <start_value> <end_value> <start_year> <end_year>
```

By default the script does not round the result. If the user asks for a number of decimal places, add the `--decimals` option. For example, `--decimals 2` rounds to two decimal places.

If Python is unavailable but another language can run, write the same formula in that language and run it. In JavaScript it looks like this.

```javascript
const startValue = START_VALUE;
const endValue = END_VALUE;
const n = END_YEAR - START_YEAR;

console.log('start_value:', startValue);
console.log('end_value:', endValue);
console.log('period (years):', n);

const cagr = Math.pow(endValue / startValue, 1 / n) - 1;
console.log('CAGR(%):', cagr * 100);
```

If no code can run at all, fill the values into the code above and print it. Tell the user to run it to get the result.

## Output format

The answer has two parts only.

- Under `# Calculation`, put the command you ran and its output in a code block.
- Under `# Result`, put the result alone, in %, in a code block, so the user can copy it as is.

Example input: 1,200 in 2020, 1,850 in 2025

````markdown
# Calculation
```
$ python scripts/cagr.py 1,200 1,850 2020 2025
start_value: 1200
end_value: 1850
period (years): 2025 - 2020 = 5
formula: (1850 / 1200) ^ (1 / 5) - 1
CAGR(%): 9.043076613444189
```

# Result
```
9.043076613444189%
```
````
