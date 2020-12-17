lines = [line.strip() for line in open('./input.txt').readlines()]
grid = {(i, j, 0, 0): lines[i][j] for i in range(len(lines)) for j in range(len(lines[0]))}


def step(_grid, dimensions=3):
    new_grid = {}

    for cell in _grid:
        active_neighbours = get_active_neighbour_count(cell, _grid, dimensions)
        if _grid[cell] == '#':
            if active_neighbours == 2 or active_neighbours == 3:
                new_grid[cell] = '#'
            else:
                new_grid[cell] = '.'

            neighbours = get_neighbours(cell, dimensions)
            for _cell in neighbours:
                if _cell not in _grid:
                    _active_neighbours = get_active_neighbour_count(_cell, _grid, dimensions)
                    if _active_neighbours == 3:
                        new_grid[_cell] = '#'
        elif _grid[cell] == '.':
            if active_neighbours == 3:
                new_grid[cell] = '#'
            else:
                new_grid[cell] = '.'

    return new_grid


def get_neighbours_3d(cell):
    neighbours = [(cell[0] + x, cell[1] + y, cell[2] + z, 0)
                  for x in range(-1, 2)
                  for y in range(-1, 2)
                  for z in range(-1, 2)
                  if not (x == 0 and y == 0 and z == 0)]

    return neighbours


def get_neighbours_4d(cell):
    neighbours = [(cell[0] + x, cell[1] + y, cell[2] + z, cell[3] + w)
                  for x in range(-1, 2)
                  for y in range(-1, 2)
                  for z in range(-1, 2)
                  for w in range(-1, 2)
                  if not (x == 0 and y == 0 and z == 0 and w == 0)]

    return neighbours


def get_active_neighbour_count_3d(cell, _grid):
    neighbours = get_neighbours_3d(cell)
    return len([x for x in neighbours if _grid.get(x) == "#"])


def get_active_neighbour_count_4d(cell, _grid):
    neighbours = get_neighbours_4d(cell)
    return len([x for x in neighbours if _grid.get(x) == "#"])


def get_neighbours(cell, dimensions):
    if dimensions == 3:
        return get_neighbours_3d(cell)
    elif dimensions == 4:
        return get_neighbours_4d(cell)


def get_active_neighbour_count(cell, _grid, dimensions):
    if dimensions == 3:
        return get_active_neighbour_count_3d(cell, _grid)
    elif dimensions == 4:
        return get_active_neighbour_count_4d(cell, _grid)


grid_3d = grid.copy()
grid_4d = grid.copy()

for i in range(6):
    grid_3d = step(grid_3d, dimensions=3)
    grid_4d = step(grid_4d, dimensions=4)

print(f"Answer for part 1: {list(grid_3d.values()).count('#')}")
print(f"Answer for part 2: {list(grid_4d.values()).count('#')}")
