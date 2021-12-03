lines = [line.strip() for line in open('03/input.txt').readlines()]
line_length = len(lines[0])
gamma_rate = 0
epsilon_rate = 0

def has_more_ones(lines, bit):
  result = {}
  for line in lines:
    result[line[bit]] = result.get(line[bit], 0) + 1
  return result['0'] <= result['1']

for i in range(line_length):
  more_ones = has_more_ones(lines, i)
  gamma_rate |= 1 << line_length-1-i if more_ones else 0
epsilon_rate = ~gamma_rate & (2**line_length) - 1
print('Part 1', gamma_rate*epsilon_rate)

cur_bit = 0
pos_generators = lines.copy()
while len(pos_generators) > 1 :
  more_ones_generator = has_more_ones(pos_generators, cur_bit)
  pos_generators = [pos_generator for pos_generator in pos_generators if pos_generator[cur_bit] == ('1' if more_ones_generator else '0')]
  cur_bit += 1

cur_bit = 0
pos_scrubbers = lines.copy()
while len(pos_scrubbers) > 1 :
  more_ones_scrubber = has_more_ones(pos_scrubbers, cur_bit)
  pos_scrubbers = [pos_scrubber for pos_scrubber in pos_scrubbers if pos_scrubber[cur_bit] == ('0' if more_ones_scrubber else '1')]
  cur_bit += 1
print('Part 2', int(pos_generators[0], 2)*int(pos_scrubbers[0], 2))