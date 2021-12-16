from collections import defaultdict

lines = [line.strip() for line in open('13/input.txt').readlines()]
grid = defaultdict(lambda: False)
instructions = []

for line in lines:
    if len(line) == 0:
        continue
    elif line[0] == 'f':
        instruction = line.split()[-1]
        instructions.append((instruction[0], int(instruction.split('=')[1])))
    else:
        i, j = line.split(',')
        grid[(int(i), int(j))] = True


def fold(_instruction, _grid):
    fold_direction, fold_at_location = _instruction
    new_grid = _grid.copy()

    for x, y in _grid.keys():
        new_x, new_y = x, y
        if fold_direction == 'x' and x > fold_at_location:
            new_x = (2 * fold_at_location) - x
        if fold_direction == 'y' and y > fold_at_location:
            new_y = (2 * fold_at_location) - y

        del new_grid[(x, y)]
        new_grid[(new_x, new_y)] = True

    return new_grid


part1_grid = grid.copy()
part2_grid = grid.copy()

# Part 1
part1_grid = fold(instructions[0], part1_grid)

# Part 2
for instruction in instructions:
    part2_grid = fold(instruction, part2_grid)

print('Part 1: ', sum(dot is True for dot in part1_grid.values()))

# Part 2 (characters in grid)
x_size = max(part2_grid.keys(), key=lambda x: x[0])[0]
y_size = max(part2_grid.keys(), key=lambda x: x[1])[1]
for y in range(y_size + 1):
    print(''.join(['#' if part2_grid[(x, y)] else '.' for x in range(x_size + 1)]))
