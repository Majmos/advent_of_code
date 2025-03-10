import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'utils')))
if True:
    from utils import input_reader
    from utils import timer


def part_1(input: str) -> int:
    instruction_pattern: re.Pattern[str] = r'mul\((\d{1,3}),(\d{1,3})\)'
    instructions: list[tuple[str, str]] = re.findall(
        instruction_pattern, input)

    sum: int = 0

    for instruction in instructions:
        num1, num2 = map(int, instruction)
        sum += num1 * num2

    return sum


def part_2(input: str) -> int:
    instructions_pattern: re.Pattern[str] = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    instructions: list[tuple[str, str, str]] = re.findall(
        instructions_pattern, input)

    sum: int = 0
    enabled: bool = True

    for instruction in instructions:
        if instruction[0].startswith('do()'):
            enabled = True
        elif instruction[0].startswith('don\'t()'):
            enabled = False
        elif enabled and instruction[0].startswith('mul'):
            num1, num2 = map(int, instruction[1:3])
            sum += num1 * num2

    return sum


@timer.measure_time
def main():
    input: str = input_reader.read_input_for_day(3)

    result_part_1: int = part_1(input)
    print(f'result part_1: {result_part_1}')

    result_part_2: int = part_2(input)
    print(f'result part_2: {result_part_2}')


if __name__ == '__main__':
    main()
