import sys


def read_input_lines_for_day(day: int) -> list[str]:
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = f'../input/day_{day}/day_{day}.txt'

    with open(f'{input_file}', 'r') as f:
        return f.readlines()


def read_strip_input_lines_for_day(day: int) -> list[str]:
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = f'../input/day_{day}/day_{day}.txt'

    with open(f'{input_file}', 'r') as f:
        return [line.strip() for line in f.readlines()]


def read_input_for_day(day: int) -> str:
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = f'../input/day_{day}/day_{day}.txt'

    with open(f'{input_file}', 'r') as f:
        return f.read()
