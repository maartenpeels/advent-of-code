# advent of code 2022
# https://adventofcode.com/2022
# day 01

def parse_input(lines):
    d = []
    elve = {
        'total': 0,
        'items': []
    }
    for line in lines:
        if line.strip() == '':
            elve['total'] = sum(elve['items'])
            d.append(elve)
            elve = {
                'total': 0,
                'items': []
            }
            continue
        elve['items'].append(int(line.strip()))
    elve['total'] = sum(elve['items'])
    d.append(elve)
    d.sort(key=lambda x: x['total'], reverse=True)
    return d


def part1(d):
    return d[0]['total']


def part2(d):
    return sum([x['total'] for x in d[:3]])


data = parse_input(open('input.txt').readlines())
print(part1(data))
print(part2(data))
