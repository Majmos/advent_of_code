import sys
import re

def find_map(input: str):
    return map_source_to_destination(input.split(':\n')[1].strip().split('\n'))


def map_source_to_destination(list_to_map: list[str]):
    mapped_list = []
    for line in list_to_map:
        (destination, source, length) = line.split()
        mapped_list.append((int(destination), int(source), int(length)))

    return mapped_list


def find_seed_location(seed: int, 
                       seed_to_soil_map: list[tuple[str, str, str]],
                       soil_to_fertilizer_map: list[tuple[str, str, str]],
                       fertilizer_to_water_map: list[tuple[str, str, str]],
                       water_to_light_map: list[tuple[str, str, str]],
                       light_to_temperature_map: list[tuple[str, str, str]],
                       temperature_to_humidity_map: list[tuple[str, str, str]],
                       humidity_to_location_map: list[tuple[str, str, str]]):
    soil = seed
    for destination, source, length in seed_to_soil_map:
        if seed in range(source, source + length):
            soil = destination - source + seed
    
    fertilizer = soil
    for destination, source, length in soil_to_fertilizer_map:
        if soil in range(source, source + length):
            fertilizer = destination - source + soil

    water = fertilizer
    for destination, source, length in fertilizer_to_water_map:
        if fertilizer in range(source, source + length):
            water = destination - source + fertilizer

    light = water
    for destination, source, length in water_to_light_map:
        if water in range(source, source + length):
            light = destination - source + water

    temperature = light
    for destination, source, length in light_to_temperature_map:
        if light in range(source, source + length):
            temperature = destination - source + light

    humidity = temperature
    for destination, source, length in temperature_to_humidity_map:
        if temperature in range(source, source + length):
            humidity = destination - source + temperature    

    location = humidity
    for destination, source, length in humidity_to_location_map:
        if humidity in range(source, source + length):
            location = destination - source + humidity

    return location


def part_1(input: str):
    groups = input.split('\n\n')

    seeds = re.search('(?<=seeds: ).*', groups[0]).group().split()

    seed_to_soil_map = find_map(groups[1])

    soil_to_fertilizer_map = find_map(groups[2])

    fertilizer_to_water_map = find_map(groups[3])

    water_to_light_map = find_map(groups[4])

    light_to_temperature_map = find_map(groups[5])

    temperature_to_humidity_map = find_map(groups[6])

    humidity_to_location_map = find_map(groups[7])

    answer = sys.maxsize
    for seed in seeds:
        temp = find_seed_location(int(seed),
                           seed_to_soil_map,
                           soil_to_fertilizer_map,
                           fertilizer_to_water_map,
                           water_to_light_map,
                           light_to_temperature_map,
                           temperature_to_humidity_map,
                           humidity_to_location_map)
        if int(temp) < answer:
            answer = int(temp)
    
    return answer


def part_2_brute_force(input: str):
    groups = input.split('\n\n')

    seeds = re.search('(?<=seeds: ).*', groups[0]).group().split()

    seed_to_soil_map = find_map(groups[1])

    soil_to_fertilizer_map = find_map(groups[2])

    fertilizer_to_water_map = find_map(groups[3])

    water_to_light_map = find_map(groups[4])

    light_to_temperature_map = find_map(groups[5])

    temperature_to_humidity_map = find_map(groups[6])

    humidity_to_location_map = find_map(groups[7])

    answer = sys.maxsize
    for i in range(0, len(seeds), 2):
        for j in range(int(seeds[i + 1])):
            temp = find_seed_location(int(seeds[i]) + j,
                                      seed_to_soil_map,
                                      soil_to_fertilizer_map,
                                      fertilizer_to_water_map,
                                      water_to_light_map,
                                      light_to_temperature_map,
                                      temperature_to_humidity_map,
                                      humidity_to_location_map)
            if int(temp) < answer:
                answer = int(temp)
    
    return answer


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