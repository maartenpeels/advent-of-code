from collections import defaultdict

values = [int(number.strip()) for number in open(f"input.txt").readlines()[0].split(',')]


def run(stop_at_turn):
    seen_at_turns = defaultdict(lambda: [])

    turn = 1
    for value in values:
        seen_at_turns[value].append(turn)
        turn += 1

    last_spoken_value = values[-1]
    while turn <= stop_at_turn:
        result = -1
        if len(seen_at_turns[last_spoken_value]) == 1:
            result = 0
            seen_at_turns[result].append(turn)
        elif len(seen_at_turns[last_spoken_value]) > 1:
            result = seen_at_turns[last_spoken_value][-1] - seen_at_turns[last_spoken_value][-2]
            seen_at_turns[result].append(turn)

        last_spoken_value = result
        turn += 1

    return last_spoken_value


print(f'Answer for part 1: {run(2020)}')
print(f'Answer for part 2: {run(30000000)}')  # Would be better to optimize, takes 15secs now..
