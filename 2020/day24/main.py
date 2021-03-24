directions = {
    'e': [2, 0],
    'se': [1, -1],
    'sw': [-1, -1],
    'w': [-2, 0],
    'nw': [-1, 1],
    'ne': [1, 1]
}

lines = [line.strip() for line in open('input.txt').readlines()]
paths = []
for line in lines:
    instructions = []
    cur_instruction = ''
    for char in line:
        if cur_instruction + char in directions.keys():
            instructions.append(cur_instruction + char)
            cur_instruction = ''
        else:
            cur_instruction += char
    paths.append(instructions)


def init_board(data):
    flipped = set()
    for path in data:
        coords = [0, 0]
        for instruction in path:
            curr = directions[instruction]
            for i in range(len(coords)):
                coords[i] += curr[i]
        tuped = tuple(coords)
        if tuped not in flipped:
            flipped.add(tuped)
        else:
            flipped.remove(tuped)
    return flipped


def part2(data):
    black = init_board(data)
    for _ in range(100):
        neighbored = {}
        for tile in black:
            if tile not in neighbored:
                neighbored[tile] = 0
            for token in directions.keys():
                curr = list(tile)
                for j in range(len(curr)):
                    curr[j] += directions[token][j]
                curr = tuple(curr)
                if curr not in neighbored.keys():
                    neighbored[curr] = 1
                else:
                    neighbored[curr] += 1
        new_black = set()
        for tile in neighbored:
            if (tile in black and neighbored[tile] in [1,2]) or (tile not in black and neighbored[tile] == 2):
                new_black.add(tile)
        black = new_black
    return len(black)


if __name__ == '__main__':
    answer_part1 = len(init_board(paths))
    print(f'Answer for part 1: {answer_part1}')

    answer_part2 = part2(paths)
    print(f'Answer for part 2: {answer_part2}')
