from collections import defaultdict

grid = [list(line.strip()) for line in open('09/input.txt').readlines()]
heights = defaultdict(lambda: 10)
risk = 0
basins = []

def neighbors(xy):
  x, y = xy
  return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def calculate_basin(xy):
  if heights[xy] >= 9:
    return 0
  heights[xy] = 9 # only calculate once
  return 1 + sum(calculate_basin(n) for n in neighbors(xy))

for y, row in enumerate(grid):
  for x, val in enumerate(row):
    heights[(x, y)] = int(val)
  
for xy, val in heights.copy().items():
  val = heights[xy]
  x, y = xy
  if all(val < heights[n] for n in neighbors(xy)):
    risk += val+1
    basins.append(xy)

basin_sizes = [calculate_basin(xy) for xy in basins]
basin_sizes.sort(reverse=True)

print('Part 1:', risk)
print('Part 2:', basin_sizes[0] * basin_sizes[1] * basin_sizes[2])