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

        print(f"mem[{mem_ptr}]: {new_value}(original value: {value})")
        mem[mem_ptr] = new_value

result = 0
for address in mem:
    result += int(mem[address])
print(result)
