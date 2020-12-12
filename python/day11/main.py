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


def get_adjecent_occupied(grid, coord):
    occupied = 0
    for adjacent_seat in adjacent:
        new_coords = (coord[0] + adjacent_seat[0], coord[1] + adjacent_seat[1])
        if grid.get(new_coords, NO_SEAT) == OCCUPIED:
            occupied += 1
    return occupied


def get_visible_occupied(grid, coord):
    occupied = 0
    for seat in adjacent:
        new_coords = coord
        while True:
            new_coords = (new_coords[0] + seat[0], new_coords[1] + seat[1])
            if new_coords[0] < 0 or new_coords[1] < 0:
                break
            if new_coords[0] == num_rows or new_coords[1] == num_cols:
                break

            adj_state = grid.get(new_coords, NO_SEAT)
            if adj_state == EMPTY:
                break

            if adj_state == OCCUPIED:
                occupied += 1
                break
    return occupied


def run_simulation(seats, tolerance, occupied_fn):
    old_seats_grid = seats.copy()
    while True:
        new_seats_grid = {}
        for coord, seat in old_seats_grid.items():
            if seat == NO_SEAT:
                new_seats_grid[coord] = seat

            occupied = occupied_fn(old_seats_grid, coord)

            if occupied == 0 and seat == EMPTY:
                new_seats_grid[coord] = OCCUPIED
            elif occupied >= tolerance and seat == OCCUPIED:
                new_seats_grid[coord] = EMPTY
            else:
                new_seats_grid[coord] = seat

        if old_seats_grid == new_seats_grid:
            return new_seats_grid
        old_seats_grid = new_seats_grid


part1_seats = run_simulation(seats_dict, 4, get_adjecent_occupied)
part2_seats = run_simulation(seats_dict, 5, get_visible_occupied)
print(f'Answer for part 1: {sum(1 for value in part1_seats.values() if value == OCCUPIED)}')
print(f'Answer for part 2: {sum(1 for value in part2_seats.values() if value == OCCUPIED)}')
