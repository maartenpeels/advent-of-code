import re

min_x, max_x, min_y, max_y = [int(i) for i in re.findall(r'-?\d+', open('17/input.txt').readline())]

part_1 = (min_y + 1) * min_y // 2

print('Part 1: ', part_1)


def is_possible(start_x, start_y, vel_x, vel_y):
    if (vel_x >= 0 and max_x < start_x) or (vel_x <= 0 and min_x > start_x):
        return False
    elif vel_y < 0 and min_y > start_y:
        return False
    return True


def step(x, y, vel_x, vel_y):
    x += vel_x
    y += vel_y

    if vel_x > 0:
        vel_x -= 1
    if vel_x < 0:
        vel_x += 1

    vel_y -= 1

    return x, y, vel_x, vel_y


def fire(vel_x, vel_y):
    possible_x = [0]
    possible_y = [0]

    while is_possible(possible_x[-1], possible_y[-1], vel_x, vel_y):
        pos_x, pos_y, vel_x, vel_y = step(possible_x[-1], possible_y[-1], vel_x, vel_y)
        possible_x.append(pos_x)
        possible_y.append(pos_y)

    return possible_x, possible_y


def is_hit(vel_x, vel_y):
    list_x, list_y = fire(vel_x, vel_y)

    if any(min_x <= x <= max_x and min_y <= y <= max_y for (x, y) in zip(list_x, list_y)):
        return True
    return False


po = []
part_2 = 0
for velocity_x in range(max_x + 1):
    for velocity_y in range(min_y - 1, 200):
        if is_hit(velocity_x, velocity_y):
            part_2 += 1
            po.append((velocity_x, velocity_y))

print('Part 2: ', part_2)
