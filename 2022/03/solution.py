# advent of code 2022
# https://adventofcode.com/2022
# day 03

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = {}
for i in range(26):
    priorities[lower[i]] = i + 1
    priorities[upper[i]] = i + 27


def parse_input(lines):
    bags = []

    for line in lines:
        bag_info = {}

        bag = line.strip()
        left = bag[:len(bag) // 2]
        right = bag[len(bag) // 2:]

        duplicates = list(set(item for item in left if item in right))

        bag_info['contents'] = bag
        bag_info['compartment_1'] = left
        bag_info['compartment_2'] = right
        bag_info['duplicates'] = duplicates

        bags.append(bag_info)
    return bags


def part1(data):
    total = 0
    for bag in data:
        total += sum(priorities[item] for item in bag['duplicates'])
    return total


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        bags = data[i:i+3]
        common_item = None

        for item in bags[0]['contents']:
            if item in bags[1]['contents'] and item in bags[2]['contents']:
                common_item = item
                break
        total += priorities[common_item]
    return total


d = parse_input(open('input.txt').readlines())
print(part1(d))
print(part2(d))
