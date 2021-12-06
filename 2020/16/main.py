import numpy as np

lines = [line.strip() for line in open(f'input.txt').readlines()]
rules = {}
my_ticket = []
other_tickets = []

step = 1
for line in lines:
    if line == '':
        step += 1
        continue

    if step == 1:
        rule_name, rule_string = line.split(': ')
        rule_ranges = rule_string.split(' or ')
        rules[rule_name] = [[int(val) for val in rule_range.split('-')] for rule_range in rule_ranges]

    if step == 2:
        if 'your ticket' in line:
            continue
        my_ticket = [int(val) for val in line.split(',')]

    if step == 3:
        if 'nearby tickets' in line:
            continue
        other_tickets.append([int(val) for val in line.split(',')])


def is_valid(name, value):
    rule = rules.get(name, [])

    valid = False
    for rule_range in rule:
        if rule_range[0] <= value <= rule_range[1]:
            valid = True

    return valid


def find_invalid_values():
    invalid_values = []
    for ticket in other_tickets:
        for value in ticket:
            result = [is_valid(rule, value) for rule in rules.keys()]
            if not any(result):
                invalid_values.append(value)
    return invalid_values


def remove_invalids(invalid_values, tickets):
    new_tickets = tickets.copy()
    tickets_to_remove = []
    for index, ticket in enumerate(tickets):
        is_valid = True
        for value in ticket:
            if value in invalid_values:
                is_valid = False
        if not is_valid:
            tickets_to_remove.append(index)

    for index in reversed(tickets_to_remove):
        del new_tickets[index]

    return new_tickets


def find_possible_matches(tickets):
    grid = np.empty(shape=(len(rules.keys()), len(tickets[0])))
    grid.fill(True)

    for ticket in tickets:
        for i, value in enumerate(ticket):
            for j, rule in enumerate(rules.keys()):
                if not is_valid(rule, value):
                    grid[i][j] = False

    while not is_done(grid):
        grid = step(grid)
        # debug_print(grid)
    return grid


def step(grid):
    row_occurrences = np.count_nonzero(grid == 1, axis=1)
    col_occurrences = np.count_nonzero(grid == 1, axis=0)

    for row_index, amount in enumerate(row_occurrences):
        if amount == 1:
            col_index = np.where(grid[row_index] == 1)[0][0]
            grid[:, col_index] = 0
            grid[row_index][col_index] = 1

    for col_index, amount in enumerate(col_occurrences):
        if amount == 1:
            row_index = np.where(grid[:, col_index] == 1)[0][0]
            grid[row_index] = 0
            grid[row_index][col_index] = 1

    return grid


def is_done(grid):
    row_occurrences = np.count_nonzero(grid == 1, axis=1)
    col_occurrences = np.count_nonzero(grid == 1, axis=0)

    done = True
    res = np.concatenate([row_occurrences, col_occurrences])
    for amount in res:
        if amount > 1:
            done = False

    return done


def calculate_result(grid, ticket):
    result = 1

    for col_index in range(6):
        row_index = np.where(grid[:, col_index] == 1)[0][0]
        result *= ticket[row_index]

    return result


def debug_print(grid):
    for a in grid:
        for b in a:
            print('1 ', end='') if b else print('0 ', end='')
        print('')
    print('')


invalid_values = find_invalid_values()
print(f'Answer for part 1: {sum(invalid_values)}')

tickets_purged = remove_invalids(invalid_values, other_tickets)
possible_matches = find_possible_matches(tickets_purged)
answer_part_2 = calculate_result(possible_matches, my_ticket)
print(f'Answer for part 2: {answer_part_2}')
