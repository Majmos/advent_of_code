import sys

CUBES = {'red': 12, 'green': 13, 'blue': 14}

def part_1(input: list[str]):
    answer: int = 0
    for line in input:
        (game_title, subsets) = line.strip().split(': ')
        id: int = int(game_title.split(' ')[1])
        items = subsets.replace(';', ',').split(', ')
        isGamePossible: bool = True
        for item in items:
            (quantity, colour) = item.split(' ')
            if colour in CUBES and CUBES[colour] < int(quantity):
                isGamePossible = False
                break

        if isGamePossible:
            answer += id
            
    return answer

def part_2(input: list[str]):
    answer: int = 0
    for line in input:
        (game_title, subsets) = line.strip().split(': ')
        id: int = int(game_title.split(' ')[1])
        items = subsets.replace(';', ',').split(', ')
        minimum_set = {'red': 0, 'green': 0, 'blue': 0}
        for item in items:
            (quantity, colour) = item.split(' ')
            if colour in minimum_set and minimum_set[colour] < int(quantity):
                minimum_set[colour] = int(quantity)

        power = 1
        for value in minimum_set.values():
            power *= value

        answer += power

    return answer

def main():
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = '../../input/day_2/day_2.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.readlines()
    
    print(part_2(input))
                

if __name__ == '__main__':
    main()