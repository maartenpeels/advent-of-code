from collections import defaultdict, deque

lines = [line.strip() for line in open('12/input.txt').readlines()]
connections = defaultdict(lambda: [])

for line in lines:
    left, right = line.split('-')
    connections[left].append(right)
    connections[right].append(left)


def count_routes(_connections):
    count = 0
    routes = deque([('start', {'start'}, False)])
    while routes:
        location, seen, visited = routes.popleft()
        if location == 'end':
            count += 1
            continue

        for location in _connections[location]:
            if location not in seen:
                seen_temp = set(seen)
                if location.islower():
                    seen_temp.add(location)
                routes.append((location, seen_temp, visited))
    return count


print('Part 1: ', count_routes(connections))
