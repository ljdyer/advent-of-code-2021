from math import prod

all_packets = {}
open_packets = []
next_id = 1

TESTS = [
    ('C200B40A82', 3),
    ('04005AC33890', 54),
    ('880086C3E88112', 7),
    ('CE00C43D881120', 9),
    ('D8005AC2A8F0', 1),
    ('F600BC2D8F', 0),
    ('9C005AC2F8F0', 0),
    ('9C0141080250320F1802104A08', 1)
]


# ====================
def get_data_from_file(file: str) -> str:
    """Get data from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read()
    return lines


# ====================
def hex_to_bin(hex: str) -> str:
    """Convert a hexidemical string to binary, bitwise"""

    bits = ''
    for x in hex:
        bits += str(bin(int(x, 16)))[2:].zfill(4)
    return bits


# ====================
def bin_to_dec(bin: str) -> int:
    """Convert a binary string to a decimal integer"""

    return int(bin, 2)


# =====
def close_completed_packets():
    """Remove ID of any open packets for whose requirement has been satisfied
    from open_packets"""

    while open_packets:

        last_open_packet_id = open_packets[-1]
        last_open_packet = all_packets[last_open_packet_id]
        children = [packet for packet in all_packets.values()
                    if packet['parent'] == last_open_packet_id]
        total_length = sum([packet['length'] for packet in children])

        # Length-type operator
        if last_open_packet['operator_type'] == 'len':
            if last_open_packet['required'] == total_length:
                all_packets[last_open_packet_id]['length'] += total_length
                open_packets.pop()
            elif last_open_packet['required'] < total_length:
                raise RuntimeError(
                    'Length requirement exceeded for packet ' +
                    f'{last_open_packet_id}'
                )
            else:
                break

        # Number-type operator
        elif last_open_packet['operator_type'] == 'num':
            num_children = len(children)
            if last_open_packet['required'] == num_children:
                all_packets[last_open_packet_id]['length'] += total_length
                open_packets.pop()
            elif last_open_packet['required'] < num_children:
                raise RuntimeError(
                    'Number requirement exceeded for packet ' +
                    f'{last_open_packet_id}'
                )
            else:
                break


# ====================
def handle_new_packet(packet: dict):
    """Add a new packet to all_packets and close any completed packets"""

    global all_packets
    global open_packets
    global next_id

    # Find the most recently opened packet in the queue and make it the parent
    # of the current packet
    if open_packets:
        parent = open_packets[-1]
    else:
        parent = None
    packet['parent'] = parent

    # Open current packet if it is an operator packet
    if 'required' in packet:
        open_packets.append(next_id)

    # Add current packet to all_packets
    all_packets[next_id] = packet

    # Close any packets that are complete
    close_completed_packets()

    # Increment ID by 1
    next_id += 1


# ====================
def parse_literal(packet: str):
    """Parse a literal packet"""

    encoded_number = packet[6:]
    number_bin = ''
    len_packet = 6

    while True:
        prefix = encoded_number[0]
        number_bin += encoded_number[1:5]
        len_packet += 5
        encoded_number = encoded_number[5:]
        # 0 signifies last group
        if prefix == "0":
            # Add packet to all_packets
            handle_new_packet({
                'type_id': 4,
                'value': bin_to_dec(number_bin),
                'length': len_packet
            })
            # If there is anything remaining, continue parsing
            if encoded_number:
                parse_any(encoded_number)
            break
    return


# ====================
def parse_operator(packet: str):
    """Parse an operator packet"""

    packet_id = bin_to_dec(packet[3:6])
    length_type_id = packet[6]

    if length_type_id == '0':
        # Length-type operator
        length_sub_packets = bin_to_dec(packet[7:22])
        handle_new_packet(
            {
                'type_id': packet_id, 'length': 22,
                'operator_type': 'len', 'required': length_sub_packets
            },
        )
        remainder = packet[22:]
        # Continue parsing
        parse_any(remainder)

    elif length_type_id == '1':
        # Number-type operator
        num_sub_packets = bin_to_dec(packet[7:18])
        handle_new_packet(
            {
                'type_id': packet_id, 'length': 18,
                'operator_type': 'num', 'required': num_sub_packets
            },
        )
        remainder = packet[18:]
        # Continue parsing
        parse_any(remainder)


# ====================
def parse_any(data: str):
    """Parse next packet"""

    if data.count('0') == len(data):
        return

    packet_id = bin_to_dec(data[3:6])

    global all_packets

    if packet_id == 4:
        parse_literal(data)
    else:
        parse_operator(data)


# ====================
def parse_data(data: str) -> int:
    """Parse all data"""

    global all_packets
    global open_packets
    global next_id

    all_packets = {}
    open_packets = []
    next_id = 0

    data_bin = hex_to_bin(data)
    parse_any(data_bin)
    return all_packets


# ====================
def evaluate_packet(data: str):

    packets = parse_data(data)

    while len(packets.keys()) > 1:

        # Remove evaluated packets and add their values to the list of
        # sub-packet values of their parent packet
        packet_items = [(id_, packet) for id_, packet in packets.items()]
        for id_, packet in packet_items:
            if 'value' in packet:
                if 'sub_packet_values' in packets[packet['parent']]:
                    packets[packet['parent']]['sub_packet_values'] += \
                        [packet['value']]
                else:
                    packets[packet['parent']]['sub_packet_values'] = \
                        [packet['value']]
                packets.pop(id_)

        # Evaluate packets that have no remaining children
        for id_, packet in packets.items():
            children = [packet_ for packet_ in packets.values()
                        if packet_['parent'] == id_]
            if not children:
                if packet['type_id'] == 0:
                    packets[id_]['value'] = sum(packet['sub_packet_values'])
                elif packet['type_id'] == 1:
                    packets[id_]['value'] = prod(packet['sub_packet_values'])
                elif packet['type_id'] == 2:
                    packets[id_]['value'] = min(packet['sub_packet_values'])
                elif packet['type_id'] == 3:
                    packets[id_]['value'] = max(packet['sub_packet_values'])
                elif packet['type_id'] >= 5:
                    num_sp_values = len(packet['sub_packet_values'])
                    if num_sp_values != 2:
                        raise RuntimeError(
                            f'Sub-packet {id_} ' +
                            f'requires 2 sub-packets but has {num_sp_values}'
                        )
                    else:
                        x, y = packet['sub_packet_values']
                        if packet['type_id'] == 5:
                            if x > y:
                                packets[id_]['value'] = 1
                            else:
                                packets[id_]['value'] = 0
                        elif packet['type_id'] == 6:
                            if x < y:
                                packets[id_]['value'] = 1
                            else:
                                packets[id_]['value'] = 0
                        elif packet['type_id'] == 7:
                            if x == y:
                                packets[id_]['value'] = 1
                            else:
                                packets[id_]['value'] = 0

    return packets[0]['value']


# ====================
def test_evaluate_packet():
    """Run tests for evaluate_packet function"""

    print('=== test_evaluate_packet ===')
    for data, expected in TESTS:
        actual = evaluate_packet(data)
        try:
            assert actual == expected
        except AssertionError:
            print('Test failed for ', data, '. expected: ',
                  expected, ', actual: ', actual, sep='')
            quit()
    print('tests passed.')


# ====================
if __name__ == "__main__":

    test_evaluate_packet()
    print()

    actual_data = get_data_from_file('../data.txt')
    answer = evaluate_packet(actual_data)

    print('Part One answer:', answer)
