filename = "passes.txt"

with open(filename) as f:
    passes = [line.strip() for line in f]

max_seat_id = -1  # row 70, column 7, seat ID 567.
seat_ids = []
for p in passes:
    row_id = p[:7]
    col_id = p[-3:]

    row = int(row_id.replace('B', '1').replace('F', '0'), 2)
    col = int(col_id.replace('R', '1').replace('L', '0'), 2)
    seat_id = (row * 8) + col

    seat_ids.append(seat_id)
    if max_seat_id == -1 or seat_id > max_seat_id:
        max_seat_id = seat_id

print(f'Anser part 1: {max_seat_id}')

last_seat_id = -1
for seat_id in sorted(seat_ids):
    if last_seat_id != -1 and seat_id - last_seat_id == 2:
        print(f'Anser part 2: {seat_id - 1}')

    last_seat_id = seat_id
