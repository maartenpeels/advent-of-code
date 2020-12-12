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


def move(cmd, amount):
    global current_north, current_east, current_facing

    if cmd == NORTH:
        current_north += amount
    if cmd == EAST:
        current_east += amount
    if cmd == SOUTH:
        current_north -= amount
    if cmd == WEST:
        current_east -= amount
    if cmd == LEFT:
        current_facing = (current_facing - amount) % 360
    if cmd == RIGHT:
        current_facing = (current_facing + amount) % 360


def rotate(degrees):
    global current_north, current_east, waypoint_north, waypoint_east

    if degrees == 90:
        waypoint_east, waypoint_north = waypoint_north, -waypoint_east
    if degrees == 180:
        waypoint_east, waypoint_north = -waypoint_east, -waypoint_north
    if degrees == 270:
        waypoint_east, waypoint_north = -waypoint_north, waypoint_east


# Part 1
current_north = 0
current_east = 0
current_facing = 90

for direction in directions:
    cmd = direction[0]
    amount = direction[1]

    move(cmd, amount)
    if cmd == FORWARD:
        move(degrees_to_direction[current_facing], amount)

print(f'Answer for part 1: {abs(current_north) + abs(current_east)}')

# Part 2
current_north = 0
current_east = 0
waypoint_north = 1
waypoint_east = 10

for direction in directions:
    cmd = direction[0]
    amount = direction[1]

    if cmd == NORTH:
        waypoint_north += amount
    if cmd == SOUTH:
        waypoint_north -= amount
    if cmd == EAST:
        waypoint_east += amount
    if cmd == WEST:
        waypoint_east -= amount
    if cmd == LEFT:
        rotate(-amount + 360)
    if cmd == RIGHT:
        rotate(amount)
    if cmd == FORWARD:
        current_north += amount * waypoint_north
        current_east += amount * waypoint_east

print(f'Answer for part 2: {abs(current_north) + abs(current_east)}')
