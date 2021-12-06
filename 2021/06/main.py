from collections import defaultdict
fish = [int(num) for num in open('06/input.txt').readline().strip().split(',')]

def run(fish, days):
  born_at = defaultdict(lambda: 0)
  for i in fish:
    born_at[i] += 1
  for day in range(days):
    # If you want to know how many fish will be born at day 10,
    # You only need to lookup how may were born at day 3 and 1.
    # This way you wont have 12376 quadrillion fish in an array tracking time.
    born_at[day] = born_at[day] + born_at[day - 7] + born_at[day - 9]
  return sum(born_at.values()) + len(fish)

print('Part 1:', run(fish, 80))
print('Part 2:', run(fish, 256))