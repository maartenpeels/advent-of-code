from collections import defaultdict
fish = [int(num) for num in open('06/input.txt').readline().strip().split(',')]

def run(state, days):
  born_at = defaultdict(lambda: 0)
  for i in state:
    born_at[i] += 1
  for day in range(days):
    born_at[day] = born_at[day] + born_at[day - 7] + born_at[day - 9]
  return sum(born_at.values()) + len(state)

print('Part 1:', run(fish, 80))
print('Part 2:', run(fish, 256))