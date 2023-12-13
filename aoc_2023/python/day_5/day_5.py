import sys
import re

def find_map(input: str):
    return map_source_to_destination(input.split(':\n')[1].strip().split('\n'))

def map_source_to_destination(list_to_map: list[str]):
    mapped_list = {}
    for line in list_to_map:
        (destination, source, length) = line.split()
        for i in range(int(length)):
            key = str(int(source) + i)
            value = str(int(destination) + i)
            mapped_list.setdefault(key, value)

    return mapped_list

def find_seed_location(seed: str, 
                       seed_to_soil_map: dict[str, str],
                       soil_to_fertilizer_map: dict[str, str],
                       fertilizer_to_water_map: dict[str, str],
                       water_to_light_map: dict[str, str],
                       light_to_temperature_map: dict[str, str],
                       temperature_to_humidity_map: dict[str, str],
                       humidity_to_location_map: dict[str, str]):
    soil = seed_to_soil_map.setdefault(seed, seed)
    fertilizer = soil_to_fertilizer_map.setdefault(soil, soil)
    water = fertilizer_to_water_map.setdefault(fertilizer, fertilizer)
    light = water_to_light_map.setdefault(water, water)
    temperature = light_to_temperature_map.setdefault(light, light)
    humidity = temperature_to_humidity_map.setdefault(temperature, temperature)
    return humidity_to_location_map.setdefault(humidity, humidity)
    

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
        temp = find_seed_location(seed,
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

    print(part_1(input))

if __name__ == "__main__":
    main()