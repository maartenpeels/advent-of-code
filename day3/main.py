filename = "./forrest.txt"

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

print(f'Height: {len(forrest)}')
print(f'Width: {len(forrest[0])}')

trees_1_1 = count_trees(1, 1)
trees_3_1 = count_trees(3, 1)
trees_5_1 = count_trees(5, 1)
trees_7_1 = count_trees(7, 1)
trees_1_2 = count_trees(1, 2)

print(f'Right 1, Down 1: {trees_1_1}')
print(f'Right 3, Down 1: {trees_3_1}')
print(f'Right 5, Down 1: {trees_5_1}')
print(f'Right 7, Down 1: {trees_7_1}')
print(f'Right 1, Down 2: {trees_1_2}')

print(f'Answer part 1: {trees_3_1}')
print(f'Answer part 2: {trees_1_1 * trees_3_1 * trees_5_1 * trees_7_1 * trees_1_2}')