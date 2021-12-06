from collections import defaultdict

lines = [line.strip() for line in open('05/input.txt')]
grid = defaultdict(lambda: 0)
grid_diagonal = defaultdict(lambda: 0)

def diagonal_enumerator(x1, y1, x2, y2):
  cur_x = x1
  cur_y = y1
  delta_x = 1 if x1 < x2 else -1
  delta_y = 1 if y1 < y2 else -1
  while cur_x != x2 or cur_y != y2:
    yield cur_x, cur_y
    cur_x += delta_x
    cur_y += delta_y
  yield cur_x, cur_y

for line in lines:
    coords = line.split(' -> ')
    x1, y1 = tuple(map(int, coords[0].split(',')))
    x2, y2 = tuple(map(int, coords[1].split(',')))

    if x1 > x2 or y1 > y2:
      x1, x2 = x2, x1
      y1, y2 = y2, y1

    if x1==x2 or y1==y2:
      for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
          grid[(x, y)] += 1
          grid_diagonal[(x, y)] += 1
    else:
      for x, y in diagonal_enumerator(x1, y1, x2, y2):
        grid_diagonal[(x, y)] += 1
    
part1_sum = len([v for v in grid.values() if v >= 2])
part2_sum = len([v for v in grid_diagonal.values() if v >= 2])

print('Part 1:', part1_sum)
print('Part 2:', part2_sum)