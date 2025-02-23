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
        is_safely_increasing: bool = False
        is_safely_decreasing: bool = False

        for index in range(len(report) - 1):
            difference = report[index] - report[index + 1]
            if (is_safely_increasing & is_safely_decreasing):
                break
            if 1 <= difference <= 3:
                is_safely_decreasing = True
            elif -3 <= difference <= -1:
                is_safely_increasing = True
            else:
                is_safely_increasing = False
                is_safely_decreasing = False
                break

        if (is_safely_increasing != is_safely_decreasing):
            safe_reports_number += 1

    return safe_reports_number


def parse_input(reports: list[str]) -> list[list[int]]:
    return [list(map(int, report.split())) for report in reports]


def main():
    start_time = time.time()

    input = input_reader.read_input_for_day(2)

    result = part_1(parse_input(input))
    print(result)

    end_time = time.time()
    print(f"main execution time: {end_time - start_time:.4f} seconds")


if __name__ == '__main__':
    main()
