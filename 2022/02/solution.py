# advent of code 2022
# https://adventofcode.com/2022
# day 02

hand_points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

hand_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


def calculate_won(elf_move, my_move):
    if elf_move == 'rock' and my_move == 'scissors':
        return False
    if elf_move == 'paper' and my_move == 'rock':
        return False
    if elf_move == 'scissors' and my_move == 'paper':
        return False

    return True


def parse_input(lines):
    game = []
    for line in lines:
        left, right = line.strip().split(' ')
        game.append((hand_map[left], hand_map[right]))
    return game


def part1(data):
    points = 0
    for elf_move, my_move in data:
        if elf_move == my_move:
            points += 3 + hand_points[my_move]
            continue

        if calculate_won(elf_move, my_move):
            points += 6
        points += hand_points[my_move]

    return points


def part2(data):
    points = 0
    for elf_move, needed_result in data:
        my_move = None
        if needed_result == 'paper':  # draw
            my_move = elf_move
        elif needed_result == 'rock':  # lose
            if elf_move == 'rock':
                my_move = 'scissors'
            elif elf_move == 'paper':
                my_move = 'rock'
            elif elf_move == 'scissors':
                my_move = 'paper'
        elif needed_result == 'scissors':  # win
            if elf_move == 'rock':
                my_move = 'paper'
            elif elf_move == 'paper':
                my_move = 'scissors'
            elif elf_move == 'scissors':
                my_move = 'rock'

        if elf_move == my_move:
            points += 3 + hand_points[my_move]
            continue

        if calculate_won(elf_move, my_move):
            points += 6

        points += hand_points[my_move]

    return points


d = parse_input(open('input.txt').readlines())
print(part1(d))
print(part2(d))
