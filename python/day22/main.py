def main():
    sections = [line.strip() for line in open('./input.txt').read().split('\n\n')]
    p1 = []
    p2 = []

    for section in sections:
        tokens = section.split(':')
        player = int(tokens[0][7])
        cards = [int(num) for num in tokens[1][1:].split('\n')]
        if player == 1:
            p1 = cards
        if player == 2:
            p2 = cards

    while len(p1) != 0 and len(p2) != 0:
        play_round(p1, p2)

    if len(p1) == 0:
        part1 = calculate_score(p2)
    else:
        part1 = calculate_score(p1)

    print(f'Answer for part 1: {part1}')


def calculate_score(cards):
    total = 0
    for i, card in enumerate(reversed(cards)):
        total += (i+1) * card
    return total


def play_round(p1, p2):
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)

    if p1_card > p2_card:
        p1.append(p1_card)
        p1.append(p2_card)
    elif p1_card < p2_card:
        p2.append(p2_card)
        p2.append(p1_card)


if __name__ == '__main__':
    main()
