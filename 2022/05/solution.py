import copy

# advent of code 2022
# https://adventofcode.com/2022
# day 05


#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

def parse_input(lines):
    stacks = {}
    moves = []

    for line in lines:
        if '[' in line:
            for i in range(0, len(line), 4):
                chunk = line[i:i + 4].strip()
                if chunk:
                    stacks.setdefault((i // 4) + 1, []).append(chunk[1:-1])
        elif 'move' in line:
            _, amount, _, from_, _, to = line.split(' ')
            moves.append((int(amount), int(from_), int(to)))

    for key, value in stacks.items():
        stacks[key] = value[::-1]

    return stacks, moves


def part1(data):
    stacks, moves = data
    for move in moves:
        amount, from_, to = move
        for _ in range(amount):
            stacks[to].append(stacks[from_].pop())

    return ''.join([stacks[i][-1] for i in range(1, len(stacks) + 1)])


def part2(data):
    stacks, moves = data
    for move in moves:
        amount, from_, to = move
        stacks[to].extend(stacks[from_][-amount:])
        stacks[from_] = stacks[from_][:-amount]

    return ''.join([stacks[i][-1] for i in range(1, len(stacks) + 1)])


d = parse_input(open('input.txt').readlines())
print(part1(copy.deepcopy(d)))
print(part2(copy.deepcopy(d)))
