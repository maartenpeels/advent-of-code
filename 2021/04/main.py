lines = [line.strip() for line in open('04/input.txt')]
numbers = None
marked = []
boards = []
board = []
first_win = None
last_win = None

for line in lines:
  if not numbers:
    numbers = [x for x in line.split(',')]
  else:
    if line:
      board.append(line.split())
    else:
      if board:
        boards.append(board)
      board = []
boards.append(board)

for board in boards:
  marked.append([[False for _ in range(5)] for _ in range(5)])

bingos = [False for _ in range(len(boards))]
for number in numbers:
  for i, board in enumerate(boards):
    for row in range(5):
      for col in range(5):
        if board[row][col] == number:
          marked[i][row][col] = True

    for row in range(5):
      full_row = True
      for col in range(5):
        if not marked[i][row][col]:
          full_row = False
      if full_row:
        bingos[i] = True

    for col in range(5):
      full_col = True
      for row in range(5):
        if not marked[i][row][col]:
          full_col = False
      if full_col:
        bingos[i] = True

    if bingos[i]:
      unmarked_sum = 0
      for row in range(5):
        for col in range(5):
          if not marked[i][row][col]:
            unmarked_sum += int(board[row][col])
      if not first_win:
        first_win = unmarked_sum * int(number)
      elif not last_win and all(bingos):
        last_win = unmarked_sum * int(number)

print('Part 1:', first_win)
print('Part 2:', last_win)