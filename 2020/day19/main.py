def main():
    rules, messages = parse_file('input.txt')

    print(f"Answer for part 1: {count_valid_messages(messages, rules)}")
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    print(f"Answer for part 2: {count_valid_messages(messages, rules)}")


def parse_file(filename):
    rules = {}
    messages = []

    step = 1
    for line in [line.strip() for line in open(filename).readlines()]:
        if line == "":
            step += 1
            continue

        if step == 1:
            key, value = line.split(': ')
            if value[0] == '"':
                rules[int(key)] = value[1:-1]
            else:
                values = value.split(' | ')
                temp_v = []
                for v in values:
                    temp_v.append([int(vv) for vv in v.split(' ')])
                rules[int(key)] = temp_v
        if step == 2:
            messages.append(line)

    # print(rules)
    return rules, messages


def match_rule(message, rule, rules):
    if len(rule) > len(message):
        return False
    elif len(rule) == 0 or len(message) == 0:
        return len(rule) == 0 and len(message) == 0

    c = rule.pop()
    if isinstance(c, str):
        if message[0] == c:
            return match_rule(message[1:], rule.copy(), rules)
    else:
        for r in rules[c]:
            if match_rule(message, rule + list(reversed(r)), rules):
                return True
    return False


def count_valid_messages(messages, rules):
    total = 0
    for message in messages:
        if match_rule(message, list(reversed(rules[0][0])), rules):
            total += 1
    return total


if __name__ == '__main__':
    main()
