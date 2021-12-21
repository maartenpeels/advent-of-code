from collections import defaultdict
from queue import Queue

grid = [list(line.strip()) for line in open('11/input.txt').readlines()]
w = len(grid[0])
h = len(grid)
energy = defaultdict(lambda: 0)
part1 = 0
part2 = 0

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        energy[(x, y)] = int(val)


def neighbours(xy):
    x, y = xy
    n = []
    for i in range(max(0, x - 1), min(x + 2, h)):
        for j in range(max(0, y - 1), min(y + 2, w)):
            n.append((i, j))
    return n


step = 0
while True:
    q = Queue()
    visited = defaultdict(lambda: False)

    for xy in energy.keys():
        energy[xy] += 1
        if energy[xy] > 9:
            visited[xy] = True
            q.put(xy)

    while not q.empty():
        xy = q.get()
        part1 += 1

        for nxy in neighbours(xy):
            energy[nxy] += 1
            if energy[nxy] > 9 and not visited[nxy]:
                visited[nxy] = True
                q.put(nxy)

    in_sync = True
    for xy in energy.keys():
        if xy in visited:
            energy[xy] = 0
        else:
            in_sync = False

    if in_sync:
        print('Part 2:', part2 + 1)
        break

    part2 += 1

    if step == 99:
        print('Part 1:', part1)
    step += 1
