lines = [line.strip() for line in open('10/input.txt').readlines()]
matching = {'{': '}', '[': ']', '(': ')', '<': '>'}
points1 = {'}': 1197, ']': 57, ')': 3, '>': 25137}
points2 = {'}': 3, ']': 2, ')': 1, '>': 4}
part1 = []
part2 = []

import math

for line in lines:
  stack = []
  for char in line:
    if char in matching:
      stack.append(matching[char])
    elif char != stack.pop():
      part1.append(points1[char])
      break
  else:
    score = 0
    while stack:
      score = score * 5 + points2[stack.pop()]
    part2.append(score)

print('Part 1:', sum(part1))
print('Part 2:', sorted(part2)[math.floor(len(part2) / 2)])