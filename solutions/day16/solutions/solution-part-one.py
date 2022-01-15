version_num_counter = 0

TESTS = [
    ('D2FE28', 6),
    ('38006F45291200', 9),
    ('EE00D40C823060', 14),
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31)
]


# ====================
def get_data_from_file(file: str) -> str:
    """Get data from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read()
    return lines


# ====================
def hex_to_bin(hex):
    """Convert a hexidemical string to binary, bitwise"""

    bits = ''
    for x in hex:
        bits += str(bin(int(x, 16)))[2:].zfill(4)
    return bits


# ====================
def bin_to_dec(bin: str) -> int:
    """Convert a binary string to a decimal integer"""

    return int(bin, 2)


# ====================
def parse_literal(packet: str):
    """Parse a literal packet"""

    encoded_number = packet[6:]

    while True:
        prefix = encoded_number[0]
        encoded_number = encoded_number[5:]
        # 0 signifies last group
        if prefix == "0":
            # If there is anything remaining, continue parsing
            if encoded_number:
                parse_any(encoded_number)
            break
    return


# ====================
def parse_operator(packet: str):
    """Parse an operator packet"""

    length_type_id = packet[6]

    if length_type_id == '0':
        # Information about sub-packet length is irrelevant
        # Continue parsing from start of the first sub-packet
        remainder = packet[22:]
        parse_any(remainder)

    elif length_type_id == '1':
        # Information about number of sub-packets is irrelevant
        # Continue parsing from start of the first sub-packet
        remainder = packet[18:]
        parse_any(remainder)


# ====================
def parse_any(packet):
    """Parse a packet, adding version numbers of each sub-packet parsed to
    the global variable version_num_counter"""

    if packet.count('0') == len(packet):
        return

    packet_version = bin_to_dec(packet[:3])
    packet_id = bin_to_dec(packet[3:6])

    global version_num_counter
    version_num_counter += packet_version

    if packet_id == 4:
        parse_literal(packet)
    else:
        parse_operator(packet)


# ====================
def get_version_num_sum(data: str) -> int:

    global version_num_counter
    version_num_counter = 0
    data_bin = hex_to_bin(data)
    parse_any(data_bin)
    return version_num_counter


# ====================
def test_get_version_num_sum():
    """Run tests for get_version_num_sum function"""

    print('=== test_get_version_num_sum ===')
    for data, expected in TESTS:
        actual = get_version_num_sum(data)
        try:
            assert actual == expected
        except AssertionError:
            print('Test failed for ', data, '. expected: ',
                  expected, ', actual: ', actual, sep='')
            quit()
    print('tests passed.')


# ====================
if __name__ == "__main__":

    test_get_version_num_sum()
    print()

    actual_data = get_data_from_file('../data.txt')
    answer = get_version_num_sum(actual_data)
    print('Part One answer:', answer)
