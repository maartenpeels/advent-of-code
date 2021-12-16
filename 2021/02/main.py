movements = [(line.split(' ')[0], int(line.split(' ')[1])) for line in open('02/input.txt').readlines()]

horizontal = 0
depth = 0
for movement in movements:
    if movement[0] == 'forward':
        horizontal += movement[1]
    elif movement[0] == 'up':
        depth -= movement[1]
    elif movement[0] == 'down':
        depth += movement[1]

print("Part 1:", horizontal * depth)

horizontal = 0
depth = 0
aim = 0
for movement in movements:
    if movement[0] == 'forward':
        horizontal += movement[1]
        depth += (aim * movement[1])
    elif movement[0] == 'up':
        aim -= movement[1]
    elif movement[0] == 'down':
        aim += movement[1]

print("Part 2:", horizontal * depth)