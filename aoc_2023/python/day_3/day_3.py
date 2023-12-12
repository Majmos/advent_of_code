import sys
import re

def part_1(input):
    width = input.index('\n') + 1
    num_set: set[(str, str)] = set()

    for symbol_match in re.finditer('[^\d.\n]', input):
        for number_match in re.finditer('\d+', input):
            symbol_index = symbol_match.start()
            if symbol_index <= width or symbol_index > len(input) - width or symbol_index % width == 0 and symbol_index % width == width - 1:
                break

            adjacent = [symbol_index - width - 1, symbol_index - width, 
                    symbol_index - width + 1, symbol_index - 1, 
                    symbol_index + 1, symbol_index + width - 1, 
                    symbol_index + width, symbol_index + width + 1]
            
            if any(number_match.start() <= index < number_match.end() for index in adjacent):
                num_set.add((number_match.start(), number_match.group()))

    sum = 0
    for i in num_set:
        sum += int(i[1])

    return sum

def part_2(input):
    width = input.index('\n') + 1
    answer = 0

    for symbol_match in re.finditer('\*', input):
        part_numbers = []
        for number_match in re.finditer('\d+', input):
            symbol_index = symbol_match.start()
            if symbol_index <= width or symbol_index > len(input) - width or symbol_index % width == 0 and symbol_index % width == width - 1:
                break

            adjacent = [symbol_index - width - 1, symbol_index - width, 
                    symbol_index - width + 1, symbol_index - 1, 
                    symbol_index + 1, symbol_index + width - 1, 
                    symbol_index + width, symbol_index + width + 1]
            
            if any(number_match.start() <= index < number_match.end() for index in adjacent):
                part_numbers.append(int(number_match.group()))
        
        if len(part_numbers) == 2:
            answer += part_numbers[0] * part_numbers[1]

    return answer

def main():
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = '../../input/day_3/day_3.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.read()

    print(part_2(input))

if __name__ == '__main__':
    main()