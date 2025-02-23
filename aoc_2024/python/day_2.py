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
            safe_reports_number += 1

    return safe_reports_number


def part_2(reports: list[list[int]]) -> int:
    safe_reports_number: int = 0
    potentially_unsafe_reports: list[list[int]] = []

    for report in reports:
        is_safely_increasing: bool = False
        is_safely_decreasing: bool = False
        for index in range(len(report) - 1):
            if (is_safely_increasing & is_safely_decreasing):
                potentially_unsafe_reports.append(report)
                break

            difference = report[index] - report[index + 1]
            if 1 <= difference <= 3:
                is_safely_decreasing = True
            elif -3 <= difference <= -1:
                is_safely_increasing = True
            else:
                is_safely_increasing = False
                is_safely_decreasing = False
                potentially_unsafe_reports.append(report)
                break

        if (is_safely_increasing != is_safely_decreasing):
            safe_reports_number += 1

    print(len(potentially_unsafe_reports))

    for report in potentially_unsafe_reports:
        result = 0
        for index in range(int(len(report))):
            result = temp(report, index)
            if result == 1:
                safe_reports_number += 1
                break
        if (result == 0):
            print(report)

    return safe_reports_number


def temp(arr: list[int], index: int):
    temp_arr = []
    for i in range(len(arr)):
        if i == index:
            continue
        temp_arr.append(arr[i])
    # print(temp_arr)
    is_safely_increasing: bool = False
    is_safely_decreasing: bool = False
    for i in range(len(temp_arr) - 1):
        error = 0
        if (is_safely_increasing & is_safely_decreasing):
            break

        difference = temp_arr[i] - temp_arr[i + 1]
        if 1 <= difference <= 3 and is_safely_increasing == False:
            is_safely_decreasing = True
        elif -3 <= difference <= -1 and is_safely_decreasing == False:
            is_safely_increasing = True
        else:
            is_safely_increasing = False
            is_safely_decreasing = False
            error += 1

    if (error > 1):
        print(error)

    if (is_safely_increasing != is_safely_decreasing):
        return 1
    else:
        return 0


def parse_input(reports: list[str]) -> list[list[int]]:
    return [list(map(int, report.split())) for report in reports]


def main():
    start_time = time.time()

    input = input_reader.read_input_for_day(2)

    result = part_2(parse_input(input))
    print(result)

    end_time = time.time()
    print(f"main execution time: {end_time - start_time:.4f} seconds")


if __name__ == '__main__':
    main()
