from helper import *
import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

# Get data
# lines = get_lines_from_file("data.txt")
# my_thing = lines[0]

# ====================
def hex_to_bin(hex):
    num_bits = len(hex)*4
    return (bin(int(hex, 16))[2:]).zfill(num_bits)

# ====================
def bin_to_dec(b):
    return int(b, 2)

# ====================
def is_valid_lit_binary(bin):
    len_ = (len(bin) // 5) * 5
    prefixes = bin[0:len_:5]
    if len(prefixes) > 0 and prefixes[-1] == '0' and prefixes[:-1].count('0') == 0:
        return True
    else:
        raise ValueError
    

# ====================
def parse_any_bin(bin):
    if len(bin) < 7:
        raise ValueError
    packet_version = bin_to_dec(bin[:3])
    packet_ID = bin_to_dec(bin[3:6])

    if packet_ID == 4:
        if len(bin) < 11:
            raise ValueError
        binary_encoding = bin[6:]
        # decimal_number = is_valid_lit_binary(binary_encoding)
        len_ = (len(binary_encoding) // 5) * 5
        prefixes = binary_encoding[0:len_:5]
        if prefixes[-1] != '0':
            raise ValueError
        elif prefixes[:-1].count('0') > 0:
            raise ValueError
        else:    
            # print('returning A')
            return packet_version
    else:
        length_type_ID = bin[6]
        if length_type_ID == '0':
            if len(bin) < 22:
                raise ValueError
            sub_packet_length = bin_to_dec(bin[7:22])
            if len(bin) < 22+sub_packet_length:
                raise ValueError
            sub_packet_info = bin[22:22+sub_packet_length]
            sub_packets = []
            n = 6
            while sub_packet_info:
                if n > len(sub_packet_info) + 1:
                    raise ValueError
                try:
                    candidate = sub_packet_info[:n]
                    sub_packet = parse_any_bin(candidate)
                    sub_packets.append(sub_packet)
                    sub_packet_info = sub_packet_info[n:]
                    n = 6
                except:
                    n += 1
            # print('returning B')
            return packet_version + sum(sub_packets)
        elif length_type_ID == '1':
            if len(bin) < 18:
                raise ValueError
            num_sub_packets = bin_to_dec(bin[7:18])
            if len(bin) < 18 + num_sub_packets * 6:
                raise ValueError
            sub_packet_info = bin[18:]
            sub_packets = []
            n = 6
            # ====================
            while len(sub_packets) < num_sub_packets and sub_packet_info.count('1')>0:
                if n > len(sub_packet_info) + 1:
                    raise ValueError
                try:
                    candidate = sub_packet_info[:n]
                    # print(candidate)
                    sub_packet = parse_any_bin(candidate)
                    # print(candidate)
                    sub_packets.append(sub_packet)
                    sub_packet_info = sub_packet_info[n:]
                    n = 6
                except:
                    n += 1
            if len(sub_packets) < num_sub_packets:
                raise ValueError
            # ====================
            # print('returning C')
            return packet_version + sum(sub_packets)


def get_packet_ver_sum(packet):
    return parse_any_bin(hex_to_bin(packet))

# Test One: lit value
tests = [
    ('D2FE28', 6),
    ('38006F45291200', 9),
    ('EE00D40C823060', 14),
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31)
]

for packet, sum_ in tests[5:6]:
    assert get_packet_ver_sum(packet) == sum_
    print()
print('tests passed.')

# MY_PACKET = "0052E4A00905271049796FB8872A0D25B9FB746893847236200B4F0BCE5194401C9B9E3F9C63992C8931A65A1CCC0D222100511A00BCBA647D98BE29A397005E55064A9DFEEC86600BD002AF2343A91A1CCE773C26600D126B69D15A6793BFCE2775D9E4A9002AB86339B5F9AB411A15CCAF10055B3EFFC00BCCE730112FA6620076268CE5CDA1FCEB69005A3800D24F4DB66E53F074F811802729733E0040E5C5E5C5C8015F9613937B83F23B278724068018014A00588014005519801EC04B220116CC0402000EAEC03519801A402B30801A802138801400170A0046A800C10001AB37FD8EB805D1C266963E95A4D1A5FF9719FEF7FDB4FB2DB29008CD2BAFA3D005CD31EB4EF2EBE4F4235DF78C66009E80293AE9310D3FCBFBCA440144580273BAEE17E55B66508803C2E0087E630F72BCD5E71B32CCFBBE2800017A2C2803D272BCBCD12BD599BC874B939004B5400964AE84A6C1E7538004CD300623AC6C882600E4328F710CC01C82D1B228980292ECD600B48E0526E506F700760CCC468012E68402324F9668028200C41E8A30E00010D8B11E62F98029801AB88039116344340004323EC48873233E72A36402504CB75006EA00084C7B895198001098D91AE2190065933AA6EB41AD0042626A93135681A400804CB54C0318032200E47B8F71C0001098810D61D8002111B228468000E5269324AD1ECF7C519B86309F35A46200A1660A280150968A4CB45365A03F3DDBAE980233407E00A80021719A1B4181006E1547D87C6008E0043337EC434C32BDE487A4AE08800D34BC3DEA974F35C20100BE723F1197F59E662FDB45824AA1D2DDCDFA2D29EBB69005072E5F2EDF3C0B244F30E0600AE00203229D229B342CC007EC95F5D6E200202615D000FB92CE7A7A402354EE0DAC0141007E20C5E87A200F4318EB0C"
# answer = get_packet_ver_sum(MY_PACKET)
# print(answer)