expressions = [line.strip().replace(' ', '') for line in open('input.txt').readlines()]


def get_rpn(expression, ops):
    output = []
    operators = []

    for char in expression:
        if char == '(':
            operators.append(char)
        if char == ')':
            while True:
                op = operators.pop()
                if op == '(':
                    break
                output.append(op)
        if char in ops:
            while True:
                if not operators:
                    break
                if operators[-1] not in ops:
                    break
                if not ops[operators[-1]] >= ops[char]:
                    break
                output.append(operators.pop())
            operators.append(char)
        if char.isdigit():
            output.append(char)
    output.extend(reversed(operators))

    return ''.join(output)


def evaluate(rpn):
    ops = {
        '*': (lambda a, b: a * b),
        '+': (lambda a, b: a + b),
        '-': (lambda a, b: a - b)
    }
    tokens = list(rpn)
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


def main():
    total_sum_part_1 = 0
    total_sum_part_2 = 0

    ops_part_1 = {
        '*': 2,
        '+': 2,
        '-': 2
    }
    ops_part_2 = {
        '*': 2,
        '+': 3,
        '-': 3
    }

    for expression in expressions:
        reverse_polish_notation_part_1 = get_rpn(expression, ops_part_1)
        total_sum_part_1 += evaluate(reverse_polish_notation_part_1)

        reverse_polish_notation_part_2 = get_rpn(expression, ops_part_2)
        total_sum_part_2 += evaluate(reverse_polish_notation_part_2)

    print(f'Answer for part 1: {total_sum_part_1}')
    print(f'Answer for part 2: {total_sum_part_2}')


if __name__ == "__main__":
    main()
