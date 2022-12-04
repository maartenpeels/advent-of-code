# advent of code 2022
# https://adventofcode.com/2022
# day 04

def parse_input(lines):
    pairs = []
    for pair in lines:
        left, right = pair.split(',')
        sections1 = [i for i in range(int(left.split('-')[0]), int(left.split('-')[1])+1)]
        sections2 = [i for i in range(int(right.split('-')[0]), int(right.split('-')[1])+1)]
        pairs.append((sections1, sections2))
    return pairs


def part1(pairs):
    result = 0
    for pair in pairs:
        overlap = set(pair[0]) & set(pair[1])
        if len(overlap) == len(pair[0]) or len(overlap) == len(pair[1]):
            result += 1
    return result


def part2(pairs):
    result = 0
    for pair in pairs:
        overlap = set(pair[0]) & set(pair[1])
        if len(overlap) > 0:
            result += 1
    return result


d = parse_input(open('input.txt').readlines())
print(part1(d))
print(part2(d))
