positions = [int(position) for position in open('07/input.txt').read().split(',')]
positions.sort()
mid = positions[len(positions) // 2]

fuel_consumption_1 = 0
fuel_consumption_2 = 999999999999999

for pos in positions:
  fuel_consumption_1 += abs(pos - mid)

for i in range(min(positions), max(positions) + 1):
  temp = 0
  for pos in positions:
    temp += abs(pos - i) * (abs(pos - i) + 1) / 2
  if temp < fuel_consumption_2:
    fuel_consumption_2 = temp

print('Part 1:', fuel_consumption_1)
print('Part 2:', fuel_consumption_2)
