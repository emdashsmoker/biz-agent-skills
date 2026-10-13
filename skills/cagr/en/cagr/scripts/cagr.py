"""Compound annual growth rate (CAGR) calculator

A number the model works out in its head leaves no trace to check, so this script does all the math.
It uses only the Python standard library, so there is nothing to install.

Usage:
    python cagr.py <start_value> <end_value> <start_year> <end_year> [--decimals N]

Example:
    python cagr.py 1,200 1,850 2020 2025
"""

import argparse
import sys

PERCENT_FACTOR = 100
EXIT_INPUT_ERROR = 1


def parse_number(text):
    """Strip thousands separators so inputs like 1,200 are accepted."""
    return float(text.replace(",", ""))


def parse_year(text):
    """Years must be integers so the period is always counted in whole years."""
    return int(text.replace(",", ""))


def format_number(value):
    """Print whole numbers without a trailing .0 (1200 instead of 1200.0)."""
    return str(int(value)) if value.is_integer() else repr(value)


def validate(start_value, end_value, period_years):
    """Check only the conditions the formula needs to give a real number."""
    if period_years <= 0:
        return "end_year must be greater than start_year"
    if start_value <= 0:
        return "start_value must be greater than 0"
    if end_value < 0:
        return "end_value must be 0 or greater"
    return None


def compute_cagr(start_value, end_value, period_years):
    return (end_value / start_value) ** (1 / period_years) - 1


def main():
    parser = argparse.ArgumentParser(description="Compound annual growth rate (CAGR) calculator")
    parser.add_argument("start_value", help="value in the start year")
    parser.add_argument("end_value", help="value in the end year")
    parser.add_argument("start_year", help="start year")
    parser.add_argument("end_year", help="end year")
    parser.add_argument("--decimals", type=int, default=None,
                        help="decimal places to round the result to (no rounding if omitted)")
    args = parser.parse_args()

    try:
        start_value = parse_number(args.start_value)
        end_value = parse_number(args.end_value)
        start_year = parse_year(args.start_year)
        end_year = parse_year(args.end_year)
    except ValueError:
        print("Input error: values must be numbers and years must be integers", file=sys.stderr)
        sys.exit(EXIT_INPUT_ERROR)

    period_years = end_year - start_year
    error = validate(start_value, end_value, period_years)
    if error:
        print(f"Input error: {error}", file=sys.stderr)
        sys.exit(EXIT_INPUT_ERROR)

    cagr_percent = compute_cagr(start_value, end_value, period_years) * PERCENT_FACTOR
    if args.decimals is not None:
        cagr_percent = round(cagr_percent, args.decimals)

    start_text = format_number(start_value)
    end_text = format_number(end_value)
    print(f"start_value: {start_text}")
    print(f"end_value: {end_text}")
    print(f"period (years): {end_year} - {start_year} = {period_years}")
    print(f"formula: ({end_text} / {start_text}) ^ (1 / {period_years}) - 1")
    print(f"CAGR(%): {cagr_percent}")


if __name__ == "__main__":
    main()
