import sys


def read_input_for_day(day: int) -> list[str]:
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = f'../input/day_{day}/day_{day}.txt'

    with open(f'{input_file}', 'r') as f:
        return f.readlines()
