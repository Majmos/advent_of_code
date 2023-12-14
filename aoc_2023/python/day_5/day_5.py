import sys
import re

def find_map(input: str):
    return map_source_to_destination(input.split(':\n')[1].strip().split('\n'))


def find_map_reverse(input: str):
    return map_destination_to_source(input.split(':\n')[1].strip().split('\n'))


def map_source_to_destination(list_to_map: list[str]):
    mapped_list = []
    for line in list_to_map:
        (destination, source, length) = line.split()
        mapped_list.append((int(destination), int(source), int(length)))

    return mapped_list


def map_destination_to_source(list_to_map: list[str]):
    mapped_list = []
    for line in list_to_map:
        (destination, source, length) = line.split()
        mapped_list.append((int(source), int(destination), int(length)))

    return mapped_list


def map_given_value(value: int, maps: list[list[tuple[str, str, str]]]):
    mapped_value: int = value
    for map in maps:
        temp: int = mapped_value
        for destination, source, length in map:
            if mapped_value in range(int(source), int(source) + int(length)):
                temp = int(destination) - int(source) + mapped_value
        mapped_value = temp
    
    return mapped_value


def part_1(input: str):
    groups = input.split('\n\n')

    seeds = re.search('(?<=seeds: ).*', groups[0]).group().split()

    maps = []
    for i in range(1, 8):
        maps.append(find_map(groups[i]))

    answer = sys.maxsize
    for seed in seeds:
        temp = map_given_value(int(seed), maps) 
        if int(temp) < answer:
            answer = int(temp)
    
    return answer


def part_2_brute_force(input: str):
    groups = input.split('\n\n')

    seeds = re.search('(?<=seeds: ).*', groups[0]).group().split()

    maps = []
    for i in range(1, 8):
        maps.append(find_map(groups[i]))

    answer = sys.maxsize
    for i in range(0, len(seeds), 2):
        for j in range(int(seeds[i + 1])):
            temp = map_given_value(int(seeds[i]) + j, maps)
            if int(temp) < answer:
                answer = int(temp)
    
    return answer


def part_2(input: str):
    groups = input.split('\n\n')

    seeds = re.search('(?<=seeds: ).*', groups[0]).group().split()

    maps: list[tuple[str, str, str]] = []
    for i in range(7, 0, -1):
        maps.append(find_map_reverse(groups[i]))

    location_to_humidity_map = sorted(maps[0], key = lambda a: a[1], reverse=True)

    for j in range(location_to_humidity_map[0][1]):
        seed = map_given_value(j, maps)
        for i in range(0, len(seeds), 2):
            if seed in range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])):
                return j
    
    return 0


def main():

    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = '../../input/day_5/day_5.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.read()

    print(part_2(input))

if __name__ == "__main__":
    main()