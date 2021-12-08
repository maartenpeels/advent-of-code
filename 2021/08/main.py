lines = [line.strip().split(' | ') for line in open('08/input.txt', 'r')]
easy_digits = {2: 1, 3: 7, 4: 4, 7: 8}
part1_sum = 0
part2_results = []

for patterns, values in lines:
    patterns = patterns.split()
    values = values.split()

    digits = {}
    result = ''

    for value in values:
      if len(value) in [2, 3, 4, 7]:
        part1_sum += 1
    
    while len(digits.keys()) < 10:
      for inp in patterns:
        inp = ''.join(sorted(inp))
        length = len(inp)
        if length in easy_digits:
          digits[easy_digits[length]] = inp
        if length == 5:
          # Numbers 2, 3 and 5 all use 5 segments so we need to find the correct number
          if len(set(inp).intersection(set(digits.get(1, ())))) == 2:
            digits[3] = inp
          elif len(set(inp).intersection(set(digits.get(6, ())))) == 5:
            digits[5] = inp
          else:
            digits[2] = inp
        if length == 6:
          # Numbers 0, 6 and 9 all use 6 segments so we need to find the correct number
          if len(set(inp).intersection(set(digits.get(4, ())))) == 4:
            digits[9] = inp
          elif len(set(inp).intersection(set(digits.get(1, ())))) == 2:
            digits[0] = inp
          else:
            digits[6] = inp
    
    for value in values:
      value = ''.join(sorted(value))
      for number, segments in digits.items():
        if segments == value:
            result += str(number)
    part2_results.append(int(result))
      
print('Part 1:', part1_sum)
print('Part 2:', sum(part2_results))