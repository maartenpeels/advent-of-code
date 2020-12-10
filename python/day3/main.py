filename = "./forrest.txt"
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open(filename) as f:
    forrest = [list(line.strip()) for line in f]


def count_trees(slope_x, slope_y):
    trees = 0
    x = 0
    y = 0
    while y < len(forrest):
        x = x % len(forrest[0])

        if forrest[y][x] == '#':
            trees += 1

        x += slope_x
        y += slope_y
    return trees


part_1_trees = count_trees(3, 1)
part_2_trees = 1
for slope_x, slope_y in slopes:
    part_2_trees *= count_trees(slope_x, slope_y)

print(f'Answer part 1: {part_1_trees}')
print(f'Answer part 2: {part_2_trees}')
