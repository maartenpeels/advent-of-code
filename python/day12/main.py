directions = [(direction.strip()[0], int(direction.strip()[1:])) for direction in open(f"./input.txt").readlines()]

NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

degrees_to_direction = {
    0: NORTH,
    90: EAST,
    180: SOUTH,
    270: WEST
}

current_north = 0
current_east = 0
current_facing = 90


def add(direction, amount):
    global current_north, current_east

    if direction == NORTH:
        current_north += amount
    if direction == EAST:
        current_east += amount
    if direction == SOUTH:
        current_north -= amount
    if direction == WEST:
        current_east -= amount


for direction in directions:
    add(direction[0], direction[1])

    if direction[0] == LEFT:
        current_facing = (current_facing - direction[1]) % 360
    if direction[0] == RIGHT:
        current_facing = (current_facing + direction[1]) % 360
    if direction[0] == FORWARD:
        add(degrees_to_direction[current_facing], direction[1])

print(f'North: {current_north}') if current_north > 0 else print(f'South: {-current_north}')
print(f'East: {current_east}') if current_east > 0 else print(f'West: {-current_east}')
print(f'Facing: {current_facing} ({degrees_to_direction[current_facing]})')
print(f'Answer for part 1: {abs(current_north) + abs(current_east)}')
