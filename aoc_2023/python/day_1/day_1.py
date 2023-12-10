import sys
import re

DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

DIGIT_REGEX = 'one|two|three|four|five|six|seven|eight|nine'
DIGIT_REGEX_REVERSED = 'one|two|three|four|five|six|seven|eight|nine'[::-1]

def combine_digits(digit_1: int, digit_2: int):
    return int(f'{digit_1}{digit_2}')

def combine_string_digits(first_digit, last_digit):
    digit_1 = DIGITS[first_digit] if first_digit in DIGITS else first_digit
    digit_2 = DIGITS[last_digit] if last_digit in DIGITS else last_digit
    return combine_digits(digit_1, digit_2)

def part_1(input):
    answer = 0
    for line in input:
        digits = re.findall('\d', line)
        answer += combine_digits(digits[0], digits[-1])
    return answer

def part_2(input: list[str]):
    answer = 0
    for line in input:
        first_digit = re.search(f'\d|{DIGIT_REGEX}', line).group()
        last_digit = re.search(f'\d|{DIGIT_REGEX_REVERSED}', line[::-1]).group()[::-1]
        answer += combine_string_digits(first_digit, last_digit)
    return answer

def main():
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = '../../input/day_1.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.readlines()
        
    print(part_2(input))


        
if __name__ == '__main__':
    main()

