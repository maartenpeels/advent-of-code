from collections import Counter

adapters = sorted([int(number.rstrip()) for number in open(f"input.txt").readlines()])
adapters.insert(0, 0)
adapters.append(max(adapters) + 3)
differences = []

last_adapter = 0
for adapter in adapters:
    differences.append(adapter - last_adapter)
    last_adapter = adapter

amount = Counter(differences)
print(f'Answer of part 1: {amount[1] * amount[3]}')

sol = {0: 1}
for adapter in adapters[1:]:
    sol[adapter] = sol.get(adapter - 1, 0) + sol.get(adapter - 2, 0) + sol.get(adapter - 3, 0)

print(f'Answer of part 2: {sol[max(adapters)]}')
