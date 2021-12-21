from collections import defaultdict

grid = [list(line.strip()) for line in open('15/input.txt').readlines()]


def enlarge(_grid):
    new_grid = _grid.copy()
    for i in range(4):
        for index, row in enumerate(new_grid):
            res = list(row[-len(_grid):])
            new_grid[index].extend(['1' if x == '9' else str(int(x) + 1) for x in res])
    for j in range(4):
        res = new_grid[-len(_grid):]
        for row in res:
            new_grid.append(['1' if x == '9' else str(int(x) + 1) for x in row])
    return new_grid


def get_neighbours(risk_levels, xy):
    x, y = xy
    directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [xy for xy in directions if xy in risk_levels]


def calculate_min_cost(_grid):
    unvisited = []
    costs = defaultdict(lambda: 9999999)
    risk_levels = defaultdict(int)

    for i, row in enumerate(_grid):
        for j, val in enumerate(row):
            risk_levels[(j, i)] = int(val)

    costs[(0, 0)] = 0
    unvisited.append((0, 0))

    while len(unvisited) > 0:
        xy = unvisited.pop(0)
        neighbours = get_neighbours(risk_levels, xy)
        for n in neighbours:
            if costs[n] > costs[xy] + risk_levels[n]:
                costs[n] = costs[xy] + risk_levels[n]
                unvisited.append(n)

    return costs[(len(_grid[0]) - 1, len(_grid) - 1)]


print('Part 1:', calculate_min_cost(grid))
print('Part 2:', calculate_min_cost(enlarge(grid)))
