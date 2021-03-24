card_key, door_key = [int(key.strip()) for key in list(open('input.txt').readlines())]

amount_of_transformations = 0
value = 1
while value != card_key:
    amount_of_transformations += 1
    value = (value * 7) % 20201227

encryption_key = 1
for _ in range(amount_of_transformations):
    encryption_key = (encryption_key * door_key) % 20201227

if __name__ == '__main__':
    answer_part1 = encryption_key
    print(f'Answer for part 1: {answer_part1}')
