"""연평균 성장률(CAGR) 계산 스크립트

모델이 숫자를 직접 계산하면 오답이 섞일 수 있으므로 계산은 이 스크립트가 전담한다.
표준 라이브러리만 사용하므로 별도 설치가 필요하지 않다.

사용법:
    python cagr.py <기준연도값> <마지막연도값> <기준연도> <마지막연도> [--decimals N]

예시:
    python cagr.py 1,200 1,850 2020 2025
"""

import argparse
import sys

PERCENT_FACTOR = 100
EXIT_INPUT_ERROR = 1


def parse_number(text):
    """천 단위 쉼표가 들어간 숫자도 받기 위해 쉼표를 지운 뒤 변환한다."""
    return float(text.replace(",", ""))


def parse_year(text):
    """연도는 정수만 허용한다. 기간 계산을 연 단위로 고정하기 위해서다."""
    return int(text.replace(",", ""))


def format_number(value):
    """1200.0처럼 불필요한 소수점이 붙지 않도록 정수는 정수로 표시한다."""
    return str(int(value)) if value.is_integer() else repr(value)


def validate(start_value, end_value, period_years):
    """계산식이 실수 범위에서 성립하는 조건만 검사한다."""
    if period_years <= 0:
        return "마지막연도는 기준연도보다 커야 함"
    if start_value <= 0:
        return "기준연도값은 0보다 커야 함"
    if end_value < 0:
        return "마지막연도값은 0 이상이어야 함"
    return None


def compute_cagr(start_value, end_value, period_years):
    return (end_value / start_value) ** (1 / period_years) - 1


def main():
    parser = argparse.ArgumentParser(description="연평균 성장률(CAGR) 계산")
    parser.add_argument("start_value", help="기준연도값")
    parser.add_argument("end_value", help="마지막연도값")
    parser.add_argument("start_year", help="기준연도")
    parser.add_argument("end_year", help="마지막연도")
    parser.add_argument("--decimals", type=int, default=None,
                        help="결과 반올림 자릿수 (생략 시 반올림하지 않음)")
    args = parser.parse_args()

    try:
        start_value = parse_number(args.start_value)
        end_value = parse_number(args.end_value)
        start_year = parse_year(args.start_year)
        end_year = parse_year(args.end_year)
    except ValueError:
        print("입력 오류: 값은 숫자, 연도는 정수로 입력 필요", file=sys.stderr)
        sys.exit(EXIT_INPUT_ERROR)

    period_years = end_year - start_year
    error = validate(start_value, end_value, period_years)
    if error:
        print(f"입력 오류: {error}", file=sys.stderr)
        sys.exit(EXIT_INPUT_ERROR)

    cagr_percent = compute_cagr(start_value, end_value, period_years) * PERCENT_FACTOR
    if args.decimals is not None:
        cagr_percent = round(cagr_percent, args.decimals)

    start_text = format_number(start_value)
    end_text = format_number(end_value)
    print(f"기준연도값: {start_text}")
    print(f"마지막연도값: {end_text}")
    print(f"기간(년): {end_year} - {start_year} = {period_years}")
    print(f"계산식: ({end_text} / {start_text}) ^ (1 / {period_years}) - 1")
    print(f"CAGR(%): {cagr_percent}")


if __name__ == "__main__":
    main()
