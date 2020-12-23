inp = [int(num) for num in list(open('./input.txt').readline())]


def part1(cups):
    for _ in range(100):
        in_hand = cups[1: 4]
        without = cups[:1] + cups[4:]

        destination_cup = None
        pointer = cups[0] - 1
        while destination_cup is None:
            if pointer <= 0:
                pointer = 9
            elif pointer in in_hand:
                pointer -= 1
            else:
                destination_cup = without.index(pointer)

        without[destination_cup + 1:destination_cup + 1] = in_hand
        cups = without[1:] + without[:1]

    return ''.join(str(x) for x in (cups[cups.index(1)+1:] + cups[:cups.index(1)]))


if __name__ == '__main__':
    answer_part1 = part1(inp.copy())

    print(f'Answer for part 1: {answer_part1}')
