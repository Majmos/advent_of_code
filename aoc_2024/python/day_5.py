import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'utils')))
if True:
    from utils import input_reader
    from utils import timer


def is_correctly_ordered(rules: list[str], update: list[int]) -> bool:
    for i in range(1, len(update)):
        for j in range(0, i):
            violation = f'{update[i]}|{update[j]}'
            if violation in rules:
                return False
    return True


def part_1(rules: list[str], updates: list[list[int]]) -> int:
    return sum(update[len(update) // 2]
               for update in updates if is_correctly_ordered(rules, update))


def parse_updates(updates: str) -> list[list[int]]:
    return [list(map(int, update.split(','))) for update in updates.split('\n')]


def parse_rules(rules: str) -> list[str]:
    return [rule for rule in rules.split('\n')]


@timer.measure_time
def main():
    rules, updates = input_reader.read_input_for_day(5).split('\n\n')

    parsed_rules: list[str] = parse_rules(rules)
    parsed_updates: list[list[int]] = parse_updates(updates)

    result_part_1: int = part_1(parsed_rules, parsed_updates)
    print(f'result part_1: {result_part_1}')

    # result_part_2: int = part_2(input)
    # print(f'result part_2: {result_part_2}')


if __name__ == '__main__':
    main()
