import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'utils')))
if True:
    from utils import input_reader


def part_1(reports: list[list[int]]) -> int:
    safe_reports_number: int = 0

    for report in reports:
        safe_reports_number += is_report_safe(report)

    return safe_reports_number


def is_report_safe(report: list[int]) -> bool:
    is_safely_increasing: bool = False
    is_safely_decreasing: bool = False

    for index in range(len(report) - 1):
        if (is_safely_increasing & is_safely_decreasing):
            break

        difference = report[index] - report[index + 1]
        if 1 <= difference <= 3:
            is_safely_decreasing = True
        elif -3 <= difference <= -1:
            is_safely_increasing = True
        else:
            is_safely_increasing = False
            is_safely_decreasing = False
            break

    if (is_safely_increasing != is_safely_decreasing):
        return 1

    return 0


def part_2(reports: list[list[int]]) -> int:
    safe_reports_number: int = 0
    potentially_unsafe_reports: list[list[int]] = []

    for report in reports:
        if (is_report_safe(report)):
            safe_reports_number += 1
        else:
            potentially_unsafe_reports.append(report)

    for report in potentially_unsafe_reports:
        for index in range(len(report)):
            if is_report_safe_without_level(report, index):
                safe_reports_number += 1
                break

    return safe_reports_number


def is_report_safe_without_level(report: list[int], level_index: int) -> bool:
    report_without_level: list[int] = report.copy()
    report_without_level.pop(level_index)

    return is_report_safe(report_without_level)


def parse_input(reports: list[str]) -> list[list[int]]:
    return [list(map(int, report.split())) for report in reports]


def main():
    start_time: float = time.time()

    input: list[str] = input_reader.read_input_for_day(2)
    parsed_input: list[list[str]] = parse_input(input)

    result_part_1: int = part_1(parsed_input)
    print(f'result part_1: {result_part_1}')

    result_part_2: int = part_2(parsed_input)
    print(f'result part_2: {result_part_2}')

    end_time: float = time.time()
    print(f"main execution time: {end_time - start_time:.4f} seconds")


if __name__ == '__main__':
    main()
