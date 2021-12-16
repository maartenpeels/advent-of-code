from collections import Counter, defaultdict

puzzle_input = open('14/input.txt').read()
polymer, rules = puzzle_input.split('\n\n')
pair_info = {}
for char_left, char_right, *_, element in rules.split('\n'):
    pair_info[char_left + char_right] = (element, char_left + element, element + char_right)


def step(pair_counts, element_count):
    _pair_counts = defaultdict(lambda: 0)
    for pair, total in pair_counts.items():
        _element, pair_left, pair_right = pair_info[pair]
        element_count[_element] += total
        _pair_counts[pair_left] += total
        _pair_counts[pair_right] += total
    return _pair_counts


def run(iterations):
    pair_counts = Counter(''.join(pair) for pair in zip(polymer, polymer[1:]))
    element_count = Counter(polymer)
    for _ in range(iterations):
        pair_counts = step(pair_counts, element_count)
    result = sorted(element_count.values())
    return result[-1] - result[0]


print('Part 1: ', run(10))
print('Part 2: ', run(40))
