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

    part1_answer = part1(p1.copy(), p2.copy())
    part2_answer = part2(p1.copy(), p2.copy())

    print(f'Answer for part 1: {part1_answer}')
    print(f'Answer for part 2: {part2_answer}')


def part1(p1, p2):
    while len(p1) != 0 and len(p2) != 0:
        play_round(p1, p2)

    if len(p1) == 0:
        answer = calculate_score(p2)
    else:
        answer = calculate_score(p1)

    return answer


def part2(p1, p2):
    cards = recursive_combat(p1, p2, set())[1]

    return calculate_score(cards)


def play_round(p1, p2):
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)

    if p1_card > p2_card:
        p1.append(p1_card)
        p1.append(p2_card)
    elif p1_card < p2_card:
        p2.append(p2_card)
        p2.append(p1_card)


def recursive_combat(p1, p2, history):
    while len(p1) != 0 and len(p2) != 0:
        if (tuple(p1), tuple(p2)) in history:
            return 1, p1

        history.add((tuple(p1), tuple(p2)))

        p1_card = p1.pop(0)
        p2_card = p2.pop(0)

        if len(p1) >= p1_card and len(p2) >= p2_card:
            winner, _ = recursive_combat(p1[:p1_card], p2[:p2_card], set())
        else:
            winner = 1 if p1_card > p2_card else 2

        if winner == 1:
            p1.extend([p1_card, p2_card])
        elif winner == 2:
            p2.extend([p2_card, p1_card])

    return (1, p1) if len(p1) > 0 else (2, p2)


def calculate_score(cards):
    total = 0
    for i, card in enumerate(reversed(cards)):
        total += (i + 1) * card
    return total


if __name__ == '__main__':
    main()
