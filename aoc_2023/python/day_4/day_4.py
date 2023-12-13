import sys

def countRecurrentCards(card: str, cards_map: dict[str, list[str]], counter: int):
    for value in cards_map.setdefault(card, []):
        counter += 1
        counter = countRecurrentCards(value, cards_map, counter)

    return counter

def part_1(input: list[str]):
    answer = 0

    for card in input:
        (card_title, win_numbers, numbers) = card.replace(':', ' |').split('| ')
        win_numbers = win_numbers.strip().split()
        numbers = numbers.strip().split()
        counter = 0

        for number in numbers:
            if number in win_numbers:
                counter += 1
        
        if counter > 0:
            answer += pow(2, counter - 1)

    return answer

def part_2(input: list[str]):
    answer = 0
    cards: list[str] = []
    cards_map: dict[str, list[str]] = {}

    for card in input:
        (card_title, win_numbers, numbers) = card.replace(':', ' |').split('| ')
        card_number = card_title.split()[1]
        win_numbers = win_numbers.strip().split()
        numbers = numbers.strip().split()
        counter = 0
        cards.append(card_number)
        
        for number in numbers:
            if number in win_numbers:
                counter += 1
                cards_map.setdefault(card_number, []).append(str(int(card_number) + counter))
                
    for card in cards:
        answer += 1
        answer += countRecurrentCards(card, cards_map, 0)

    return answer


def main():
    if len(sys.argv) == 2:
        input_file = str(sys.argv[1])
    else:
        input_file = '../../input/day_4/day_4.txt'

    with open(f'{input_file}', 'r') as f:
        input = f.read().split('\n')

    print(part_2(input))

if __name__ == "__main__":
    main()