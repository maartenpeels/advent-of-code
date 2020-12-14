import math

lines = [line.strip() for line in open(f"./input.txt").readlines()]
earliest_possible = int(lines[0])
bus_ids = [int(bus_id) for bus_id in lines[1].split(',') if bus_id != 'x']

# Part 1
done = False
start = earliest_possible
while not done:
    for bus_id in bus_ids:
        if start % bus_id == 0:
            print(f'Answer for part 1: {bus_id * (start - earliest_possible)}')
            done = True
    start += 1


# Part 2
def lcm(a):
    result = a[0][0]
    for i in a[1:]:
        result = result * i[0] // math.gcd(result, i[0])
    return result


bus_ids = sorted([[int(bus_id), index] for index, bus_id in enumerate(lines[1].split(',')) if bus_id != 'x'])
value = 0
step_size = 1

for index in range(1, len(bus_ids)):
    done = False
    while not done:
        done = True
        for j in range(index + 1):
            if (value + bus_ids[j][1]) % bus_ids[j][0] != 0:
                done = False
                break

        if done:
            step_size = lcm(bus_ids[:j])
            break
        else:
            value += step_size

print(f'Answer for part 2: {value}')
