from collections import defaultdict, deque

def can_contain(color, bag):
  if not rules[bag]:
    return False
  elif color in rules[bag]:
    return True
  else:
    return True in [can_contain(color, next_bag) for next_bag in rules[bag]]

def amount_of_bags(color):
  if not rules[color]:
    return 0
  total = 0
  for bag in rules[color]:
    total += rules[color][bag] * (amount_of_bags(bag) + 1)
  return total

rules = {}
for rule in open("rules.txt").readlines():
  rule = rule.replace('bags', 'bag').replace(' contain ', ':').strip('.\n')
  bag, contents = rule.split(':')
  rules[bag] = {}
  if contents != "no other bag":
    for content in contents.split(', '):
      amount, color = content.split(' ', 1)
      rules[bag][color] = int(amount)

print(f'Answer for part 1: {[can_contain("shiny gold bag", bag) for bag in rules].count(True)}')
print(f'Answer for part 2: {amount_of_bags("shiny gold bag")}')