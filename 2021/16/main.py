hex_input = open('16/input.txt').readline()
total_version = 0
bin_input = format(int(hex_input.strip(), 16), f"0{len(hex_input.strip()) * 4}b")


def parse_packet(packet, count=-1):
    if packet == '' or int(packet) == 0:
        return 0
    if count == 0:
        return parse_packet(packet, count=-1)

    packet_version = int(packet[0:3], 2)
    packet_type = int(packet[3:6], 2)

    if packet_type == 4:
        index = 6
        done = False
        while not done:
            if packet[index] == "0":
                done = True
            index += 5
        return packet_version + parse_packet(packet[index:], count - 1)

    packet_length_type = int(packet[6], 2)
    if packet_length_type == 0:
        number_of_bits = int(packet[7:22], 2)
        return packet_version + parse_packet(packet[22:22+number_of_bits], -1) + parse_packet(packet[22+number_of_bits:], count - 1)
    if packet_length_type == 1:
        number_of_packets = int(packet[7:18], 2)
        return packet_version + parse_packet(packet[18:], number_of_packets)


print(parse_packet(bin_input))
