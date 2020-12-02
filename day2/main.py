from collections import defaultdict

filename = "./passwords.txt"

with open(filename) as f:
    lines = [line.rstrip() for line in f]

# Part 1
valid_passwords = 0
for line in lines:
    line_parts = [part.strip() for part in line.split(':')]
    password = line_parts[1]

    policy = line_parts[0]
    policy_parts = policy.split(' ')

    min_amount = int(policy_parts[0].split('-')[0])
    max_amount = int(policy_parts[0].split('-')[1])
    letter = policy_parts[1]

    occ = defaultdict(lambda: 0) 
    for char in password:
        occ[char] += 1
    
    if occ[letter] >= min_amount and occ[letter] <= max_amount:
        valid_passwords += 1

print(f'Valid passwords: {valid_passwords}')

# Part 2
