from helper import *
import os

# Get data
lines = get_lines_from_file("data.txt")
my_thing = lines[0]

# ====================
def hex_to_bin(hex):
    num_bits = len(hex)*4
    return (bin(int(hex, 16))[2:]).zfill(num_bits)

# ====================
def bin_to_dec(b):
    return int(b, 2)


# ====================
def get_encoding(x, as_bin=False):

    if as_bin:
        b = x
    else:
        b = hex_to_bin(x)

    if b.replace('0','') == '':
        return None

    try:
        packet_version = bin_to_dec(b[:3])
        packet_ID = bin_to_dec(b[3:6])
        remainder = b[6:]
    except:
        # Not long enough
        return None

    if packet_ID == 4:
        # Literal value
        if parse_lit_val(remainder):
            print(x, packet_version)
            return packet_version
        else:
            return None

    else:
        # Operator value
        try: 
            length_type_ID = remainder[0]
        except:
            return None
        remainder = remainder[1:]
        if length_type_ID == '0':
            # Length type ID = 0
            if len(remainder) < 15:
                return None
            try:
                total_length = bin_to_dec(remainder[:15])
                # print(total_length)
            except:
                return None
            
            sub_packets = remainder[15:15+total_length+1]
            while len(sub_packets) > 0:
                if sub_packets.replace('0','') == '':
                    break
                for i in range(1,len(sub_packets)):
                    candidate = sub_packets[:i]
                    if get_encoding(candidate, as_bin=True):
                        sub_packets = sub_packets[i:]
                        break
                else:
                    return None
            print(b, packet_version)
            return packet_version

        elif length_type_ID == '1':
            # Length type ID = 1
            if len(remainder) < 11:
                return None
            try:
                num_sps = bin_to_dec(remainder[:11])
            except:
                return None
            sub_packets = remainder[11:]
            sp_count = 0
            while len(sub_packets) > 0:
                if sp_count >= num_sps and sub_packets.replace('0','') == '':
                    break
                for i in range(1,len(sub_packets)):
                    candidate = sub_packets[:i]
                    if get_encoding(candidate, as_bin=True):
                        sp_count += 1
                        sub_packets = sub_packets[i:]
                        break
                else:
                    return None
            print(b, packet_version)
            return packet_version


# ====================
def parse_lit_val(b):
    
    chunks = []
    while len(b) > 4:
        chunks.append(b[:5])
        b = b[5:]
    if len(b) > 0:
        if '1' in b:
            return None
    try:
        if chunks[-1][0] != '0':
            return None
    except:
        return None
    all = ''.join([chunk[1:] for chunk in chunks])
    return bin_to_dec(all)
        
os.system('cls')
get_encoding('D2FE28')          # Lit
get_encoding('38006F4529120')  # Op
get_encoding('EE00D40C823060')  # Op
# print(hex_to_bin('620080001611562C8802118E34'))

# print()
# get_encoding('8A004A801A8002F478')
# print()
get_encoding('620080001611562C8802118E34')
print()
# get_encoding('C0015000016115A2E0802F182340')
# print()
get_encoding('A0016C880162017C3686B18A3D4780')
print()
