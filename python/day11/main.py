seat_layout = [seat_row.strip() for seat_row in open(f"./input.txt").readlines()]
adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
num_rows = len(seat_layout)
num_cols = len(seat_layout[0])

OCCUPIED = '#'
EMPTY = 'L'
NO_SEAT = '.'

seats_dict = {}
for row in range(num_rows):
    for col in range(num_cols):
        seats_dict[(row, col)] = seat_layout[row][col]

while True:
    new_seats_grid = {}
    for coord, seat in seats_dict.items():
        if seat == NO_SEAT:
            new_seats_grid[coord] = seat

        occupied = 0
        for adjacent_seat in adjacent:
            new_coords = (coord[0] + adjacent_seat[0], coord[1] + adjacent_seat[1])
            if seats_dict.get(new_coords, NO_SEAT) == OCCUPIED:
                occupied += 1

        if occupied == 0 and seat == EMPTY:
            new_seats_grid[coord] = OCCUPIED
        elif occupied >= 4 and seat == OCCUPIED:
            new_seats_grid[coord] = EMPTY
        else:
            new_seats_grid[coord] = seat

    if seats_dict == new_seats_grid:
        break

    seats_dict = new_seats_grid

print(f'Answer for part 1: {sum(1 for value in seats_dict.values() if value == "#")}')
