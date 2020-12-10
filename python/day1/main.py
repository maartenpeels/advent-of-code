filename = "./expense-report.txt"
target_val = 2020

with open(filename) as f:
    lines = [int(line.rstrip()) for line in f]
  
lines = sorted(lines)

# Part 1
left = 0
right = len(lines) - 1

while left < right:
  result = lines[left] + lines[right]
  if result == target_val:
    print(f"{lines[left]} + {lines[right]} = {target_val}. Answer part 1: {lines[left] * lines[right]}")
    break
  elif result > target_val:
    right -= 1
  elif result < target_val:
    left += 1

# Part 2
for i in range(len(lines) - 1):
  left = i + 1
  right = len(lines) - 1

  while left < right:
    result = lines[i] + lines[left] + lines[right]
    if result == target_val:
      print(lines[i], lines[left], lines[right])
      print(f"{lines[i]} + {lines[left]} + {lines[right]} = {target_val}. Answer part 2: {lines[i] * lines[left] * lines[right]}")
      break
    elif result > target_val:
      right -= 1
    elif result < target_val:
      left += 1