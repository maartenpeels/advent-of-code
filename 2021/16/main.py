hex_input = open('16/input.txt').readline()
total_version = 0
bin_input = format(int(hex_input.strip(), 16), f"0{len(hex_input.strip()) * 4}b")


def operate(packet_type, values):
    if packet_type == 0:
        return sum(values)
    if packet_type == 1:
        p = 1
        for v in values:
            p *= v
        return p
    if packet_type == 2:
        return min(values)
    if packet_type == 3:
        return max(values)
    if packet_type == 5:
        return int(values[0] > values[1])
    if packet_type == 6:
        return int(values[0] < values[1])
    if packet_type == 7:
        return int(values[0] == values[1])


def parse_packet(i, j=-1):
    if i == j:
        return None, None
    if i > len(bin_input) - 4:
        return None, None

    packet_version = int(bin_input[i:i+3], 2)
    global total_version
    total_version += packet_version

    packet_type = int(bin_input[i+3:i+6], 2)

    if packet_type == 4:
        i += 6
        literal_value = ''
        done = False
        while not done:
            if bin_input[i] == "0":
                done = True
            literal_value += bin_input[i + 1: i + 5]
            i += 5
        literal_value = int(literal_value, 2)
        return literal_value, i

    sub_packets = []
    next_start = None
    packet_length_type = bin_input[i+6]
    if packet_length_type == "0":
        number_of_bits = int(bin_input[i+7:i+22], 2)
        end = i + 22 + number_of_bits
        index = i + 22
        prev_index = None
        while index is not None:
            prev_index = index
            x, index = parse_packet(index, end)
            sub_packets.append(x)
        sub_packets = sub_packets[:-1]
        next_start = prev_index
    if packet_length_type == "1":
        remove_sub_packets = int(bin_input[i+7:i+18], 2)
        index = i + 18
        while remove_sub_packets > 0:
            x, index = parse_packet(index)
            remove_sub_packets -= 1
            sub_packets.append(x)
        next_start = index
    return operate(packet_type, sub_packets), next_start


result = parse_packet(0)
print('Part 1:', total_version)
print('Part 2:', result[0])
