from collections import defaultdict

filename = "answers.txt"

groups = []
cur_group = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        if line == '':
            groups.append(cur_group)
            cur_group = []
        else:
            cur_group.append(line)
    groups.append(cur_group)

sum_of_anyone_counts = 0
sum_of_everyone_counts = 0
for group in groups:
    count = defaultdict(lambda: 0)
    for person in group:
        for answers in person:
            for answer in answers:
                count[answer] += 1

    sum_of_anyone_counts += len(count.keys())
    sum_of_everyone_counts += sum(1 for value in count.values() if value == len(group))

print(f'Answer for part 1: {sum_of_anyone_counts}')
print(f'Answer for part 2: {sum_of_everyone_counts}')
