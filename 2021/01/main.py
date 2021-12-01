numbers = [int(line) for line in open('input.txt').readlines()]
print(len(numbers))

larger_measurements = 0
for index, number in enumerate(numbers):
  if index > 0:
    if number > numbers[index - 1]:
      larger_measurements += 1

print('Larger measurements part 1:', larger_measurements)

sliding_window = 3
sliding_window_numbers = []

for index, number in enumerate(numbers):
  if index >= sliding_window - 1:
    sliding_window_numbers.append(number + numbers[index - 1] + numbers[index - 2])

larger_measurements = 0
for index, number in enumerate(sliding_window_numbers):
  if index > 0:
    if number > sliding_window_numbers[index - 1]:
      larger_measurements += 1

print('Larger measurements part 2:', larger_measurements)