state = [int(num) for num in open('06/input.txt').readline().strip().split(',')]
days = 80

for day in range(days):
  for i in range(len(state)):
    state[i] = state[i] - 1
    if state[i] < 0:
      state[i] = 6
      state.append(8)
print('Part 1:', len(state))