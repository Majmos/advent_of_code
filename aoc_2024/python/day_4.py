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
    def search_from(row: int, column: int, direction: tuple[int, int]) -> bool:
        for i in range(len(word)):
            nx, ny = row + i * direction[0], column + i * direction[1]
            if not in_bounds(nx, ny, len(grid), len(grid[0])) or grid[nx][ny] != word[i]:
                return False
        return True

    count: int = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            for direction in DIRECTIONS:
                if search_from(row, column, direction):
                    count += 1
    return count


def part_1(input: list[str]) -> int:
    grid: list[list[str]] = [list(line) for line in input]
    return search_word(grid, SEARCHED_WORD)


def search_x_mas(grid: list[list[str]]) -> int:
    def check_x_mas_pattern(row_index: int, column_index: int) -> bool:
        pattern: tuple[str, str, str, str] = (grid[row_index-1][column_index-1], grid[row_index+1][column_index-1],
                                              grid[row_index-1][column_index+1], grid[row_index+1][column_index+1])

        if pattern in [('M', 'S', 'M', 'S'), ('S', 'M', 'S', 'M'), ('M', 'M', 'S', 'S'), ('S', 'S', 'M', 'M')]:
            return True
        return False

    def search_x_mas_from(row_index: int, column_index: int) -> bool:
        if (grid[row_index][column_index] != 'A'):
            return False

        if not in_bounds(row_index, column_index, len(grid) - 1, len(grid[0]) - 1):
            return False

        return check_x_mas_pattern(row_index, column_index)

    count: int = 0
    for row_index in range(1, len(grid) - 1):
        for column_index in range(1, len(grid[0]) - 1):
            if search_x_mas_from(row_index, column_index):
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
