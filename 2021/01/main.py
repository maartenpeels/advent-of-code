numbers = [int(line) for line in open('01/input.txt').readlines()]
part1_larger_measerments = 0
part2_larger_measerments = 0

for i in range(len(numbers)):
  if i >= 1 and numbers[i] > numbers[i - 1]:
    part1_larger_measerments += 1
  if i >= 3 and numbers[i] + numbers[i - 1] + numbers[i - 2] > numbers[i - 1] + numbers[i - 2] + numbers[i - 3]:
    part2_larger_measerments += 1

print('Larger measurements part 1:', part1_larger_measerments)
print('Larger measurements part 2:', part2_larger_measerments)