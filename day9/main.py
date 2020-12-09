preamble = 25
xmas = [int(number.rstrip()) for number in open(f"./input.txt").readlines()]


def valid_sum(target_val, numbers):
    left = 0
    right = len(numbers) - 1
    valid = False

    while left < right:
        result = numbers[left] + numbers[right]
        if result == target_val:
            valid = True
            break
        elif result > target_val:
            right -= 1
        elif result < target_val:
            left += 1

    return valid


def find_contiguous_set(target_val):
    for size in range(2, len(xmas)):
        for pos in range(len(xmas)-size):
            result = sum(xmas[pos:pos+size])
            if result == target_val:
                return sorted(xmas[pos:pos+size])
    return []


for i in range(preamble + 1, len(xmas) - 1):
    if not valid_sum(xmas[i], sorted(xmas[i - preamble - 1:i])):
        print(f'Answer to part 1: {xmas[i]}')
        contiguous_set = find_contiguous_set(xmas[i])
        print(f'Answer to part 2: {contiguous_set[0] + contiguous_set[-1]}')
        break
