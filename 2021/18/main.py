import json
import re

number_arrays = [json.loads(line) for line in open('18/test.txt')]


def add(num_1, num_2):
    reduced = str([num_1, num_2])
    if '[[[[' in reduced or ']]]]' in reduced:
        print('explode')
    elif re.match('\\d{2,}', reduced):
        print('split')
    return 1


total = 0
for i in range(0, len(number_arrays), 2):
    total += add(number_arrays[i], number_arrays[i+1])

print('break')
