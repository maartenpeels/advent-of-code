import sys

sys.path.append('..')
from cpu import Cpu

_code = [int(char) for char in open("input.txt").readline().strip().split(',')]


def part1():
    target = 19690720
    part1_code = _code.copy()
    cpu = Cpu(_code)
    for noun in range(100):
        for verb in range(100):
            part1_code[1] = noun
            part1_code[2] = verb
            cpu.flash(part1_code)
            memory = cpu.run()
            if memory[0] == target:
                return 100 * noun + verb


if __name__ == '__main__':
    print(f'Answer for part 1: {part1()}')

    answer_part2 = 2
    print(f'Answer for part 2: {answer_part2}')
