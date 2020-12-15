lines = [line.strip() for line in open(f"./input.txt").readlines()]

mask = 0
mem = {}
bit_values = {}


def set_bit(position, binary):
    bit_mask = 1 << position
    return bit_mask | binary


def clr_bit(position, binary):
    bit_mask = 1 << position
    return ~bit_mask & binary


def expand_mem_ptr(mem_pointer, mask):
    pointers = []

    new_mask = list(mask)
    str_ptr = str(bin(mem_pointer)[2:])[::-1]
    for i, bit in enumerate(str_ptr):
        if str_ptr[i] == '1' and new_mask[len(mask) - i - 1] != 'X':
            new_mask[len(mask) - i - 1] = '1'
    new_mask = "".join(new_mask)

    tmp_pointers = [new_mask]
    while len(tmp_pointers) > 0:
        if 'X' not in tmp_pointers[0]:
            pointers.append(tmp_pointers[0])
            del tmp_pointers[0]
            continue

        for index, bit in enumerate(tmp_pointers[0]):
            if bit == 'X':
                pointer0 = list(tmp_pointers[0])
                pointer0[index] = '0'
                pointer0 = "".join(pointer0)
                tmp_pointers.append(pointer0)

                pointer1 = list(tmp_pointers[0])
                pointer1[index] = '1'
                pointer1 = "".join(pointer1)
                tmp_pointers.append(pointer1)

                del tmp_pointers[0]
                break

    return pointers

# Part 1
for line in lines:
    if line[:4] == "mask":
        mask = line.split(" = ")[1].strip()
    else:
        parts = line.split(" = ")
        mem_ptr = int(parts[0].split("[")[1][:-1])
        value = int(parts[1])

        new_value = value
        for index, bit in enumerate(mask):
            if bit == '1':
                new_value = set_bit(len(mask) - index - 1, new_value)
            if bit == '0':
                new_value = clr_bit(len(mask) - index - 1, new_value)

        # print(f"mem[{mem_ptr}]: {new_value}(original value: {value})")
        mem[mem_ptr] = new_value

result = 0
for address in mem:
    result += int(mem[address])
print(f'Answer for part 1: {result}')

# Part 2
mem = {}
for line in lines:
    if line[:4] == "mask":
        mask = line.split(" = ")[1].strip()
    else:
        parts = line.split(" = ")
        mem_ptr = int(parts[0].split("[")[1][:-1])
        value = int(parts[1])

        pointers = expand_mem_ptr(mem_ptr, mask)
        for pointer in pointers:
            mem[int(pointer, 2)] = value

result = 0
for address in mem:
    result += int(mem[address])
print(f'Answer for part 2: {result}')
