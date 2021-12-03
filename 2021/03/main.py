lines = [line.strip() for line in open('test.txt').readlines()]
line_length = len(lines[0])
gamma_rate = 0
epsilon_rate = 0

for i in range(line_length):
  bit_count = {}
  for line in lines:
    bit_count[line[i]] = bit_count.get(line[i], 0) + 1
  
  more_ones = bit_count['0'] < bit_count['1']
  gamma_rate |= 1 << line_length-1-i if more_ones else 0

epsilon_rate = ~gamma_rate & (2**line_length) - 1

print('Part 1', gamma_rate*epsilon_rate)