from collections import defaultdict

filename = "./passwords.txt"

with open(filename) as f:
    lines = [line.rstrip() for line in f]

def parse_line(line):
    line_parts = [part.strip() for part in line.split(':')]
    password = line_parts[1]

    policy = line_parts[0]
    policy_parts = policy.split(' ')

    min_amount = int(policy_parts[0].split('-')[0])
    max_amount = int(policy_parts[0].split('-')[1])
    letter = policy_parts[1]

    return min_amount, max_amount, letter, password

# Part 1
valid_passwords = 0
for line in lines:
    min_amount, max_amount, letter, password = parse_line(line)

    occ = defaultdict(lambda: 0) 
    for char in password:
        occ[char] += 1
    
    if occ[letter] >= min_amount and occ[letter] <= max_amount:
        valid_passwords += 1

print(f'Valid passwords part 1: {valid_passwords}')

# Part 2
valid_passwords = 0
for line in lines:
    pos_1, pos_2, letter, password = parse_line(line)

    matches = 0
    matches += 1 if password[pos_1-1] == letter else 0
    matches += 1 if password[pos_2-1] == letter else 0

    if matches == 1:
        valid_passwords += 1

print(f'Valid passwords part 2: {valid_passwords}')