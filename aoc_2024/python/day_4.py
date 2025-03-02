from functools import lru_cache
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'utils')))
if True:
    from utils import input_reader
    from utils import timer


SEARCHED_WORD: str = "XMAS"
DIRECTIONS: tuple[int, int] = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
    (1, 1),  # down-right
    (1, -1),  # down-left
    (-1, 1),  # up-right
    (-1, -1)  # up-left
]


@lru_cache
def in_bounds(row_index: int, column_index: int, rows_num: int, columns_num: int) -> bool:
    return 0 <= row_index < rows_num and 0 <= column_index < columns_num


def search_word(grid: list[list[str]], word: str) -> int:
    def search_from(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny, len(grid), len(grid[0])) or grid[nx][ny] != word[i]:
                return False
        return True

    count: int = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in DIRECTIONS:
                if search_from(x, y, dx, dy):
                    count += 1
    return count


def part_1(input: list[str]) -> int:
    grid: list[list[str]] = [list(line) for line in input]
    return search_word(grid, SEARCHED_WORD)


def search_x_mas(grid: list[list[str]]) -> int:
    def check_x_mas_pattern(x, y):
        patterns = [
            (grid[x-1][y-1], grid[x+1][y+1], grid[x-1][y+1], grid[x+1][y-1]),
            (grid[x+1][y-1], grid[x-1][y+1], grid[x+1][y+1], grid[x-1][y-1]),
            (grid[x-1][y-1], grid[x+1][y+1], grid[x+1][y-1], grid[x-1][y+1]),
            (grid[x+1][y+1], grid[x-1][y-1], grid[x-1][y+1], grid[x+1][y-1])
        ]
        for pattern in patterns:
            if pattern == ('M', 'S', 'M', 'S'):
                return True
        return False

    def search_x_mas_from(x, y):
        if (grid[x][y] != 'A'):
            return False

        if not all(in_bounds(nx, ny, len(grid), len(grid[0])) for nx, ny in [(x-1, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1)]):
            return False

        if (check_x_mas_pattern(x, y)):
            return True
        return False

    count: int = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if search_x_mas_from(x, y):
                count += 1
    return count


def part_2(input: list[str]) -> int:
    grid: list[list[str]] = [list(line) for line in input]
    return search_x_mas(grid)


@timer.measure_time
def main():
    input: list[str] = input_reader.read_strip_input_lines_for_day(4)

    result_part_1: int = part_1(input)
    print(f'result part_1: {result_part_1}')

    result_part_2: int = part_2(input)
    print(f'result part_2: {result_part_2}')


if __name__ == '__main__':
    main()
