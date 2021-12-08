from helper import *

# ALL
# 0 6
# 1 2
# 2 5
# 3 5
# 4 4
# 5 5
# 6 6
# 7 3
# 8 7
# 9 6

# UNIQUE
# 1 2
# 4 4
# 7 3
# 8 7

digit_maps = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
char_maps = {v:k for k,v in digit_maps.items()}

lines = get_lines_from_file("data.txt")

parts = [l.split(" |") for l in lines]
first_parts = [l[0] for l in parts]
second_parts = [l[1] for l in parts]
all_digits = [(l1 + l2).split(" ") for l1,l2 in zip(first_parts, second_parts)]


# Return 'digits' that have len l in line x
def return_with_len(my_len, line):
    return list(set(([digit for digit in line if len(digit) == my_len])))

def first_with_len(my_len, line):
    return return_with_len(my_len, line)[0][0]


def get_mapping(line):

    line = [''.join(sorted(x)) for x in line]
    mapping = {}
    one = return_with_len(2,line)[0]
    seven = return_with_len(3,line)[0]

    cf = list(set([x for x in seven if x in one]))
    mapping['c'] = cf
    mapping['f'] = cf
    mapping['a'] = [x for x in seven if x not in one][0]

    four = return_with_len(4,line)[0]
    bd = list(set([x for x in four if not x in cf]))
    mapping['b'] = bd
    mapping['d'] = bd
    
    eight = return_with_len(7,line)[0]
    eg = list(set([x for x in eight if not (x in bd or x in cf or x == mapping['a'])]))
    mapping['e'] = eg
    mapping['g'] = eg

    five_signals = return_with_len(5,line)
    dg = [x for x in five_signals[0] if x in five_signals[1] and x in five_signals[2] and x != mapping['a']]

    mapping['d'] = [x for x in mapping['d'] if x in dg][0]
    mapping['g'] = [x for x in mapping['g'] if x in dg][0]

    for key, val in mapping.items():
        if isinstance(mapping[key], list):
            mapping[key] = [x for x in val if x not in mapping.values()]
            if len(mapping[key]) == 1:
                mapping[key] = mapping[key][0]

    dist_to_orig = {v:k for k,v in mapping.items() if isinstance(v,str)}

    for l in line:
        remaining_unknowns = [x for x in l if x not in dist_to_orig.keys()]
        if len(l) == 6 and len(remaining_unknowns) == 1:
            mapping['f'] = remaining_unknowns[0]

    for key, val in mapping.items():
        if isinstance(mapping[key], list):
            mapping[key] = [x for x in val if x not in mapping.values()]
            if len(mapping[key]) == 1:
                mapping[key] = mapping[key][0]    
    

    dist_to_orig = {v:k for k,v in mapping.items() if isinstance(v,str)}

    def decode(l):
        return ''.join(dist_to_orig[x] for x in l)
    def get_number(l):
        return char_maps[''.join(sorted(l))]

    decoded = [get_number(decode(l)) for l in line][-4:]

    return ''.join([str(d) for d in decoded])



answers = [int(get_mapping(line)) for line in all_digits]
answer = sum(answers)
print(answer)
# # print(twos)
# # print(sum(num_uniques))


# # print_last_n(100, lines)
# # write_lines_to_file("new.txt", lines)




# # def num_unique(l):
# #     return sum([1 for x in l if len(x) in [2,3,4,7]])









# # === REGEX ===
# # # Get instances of 'foo', 'bar' from string
# # alpha = "foo|bar"
# # subs = get_substrings(alpha, my_str)

# # Parse string into parts
# # reg = r'(.*)-(.*) (.*): (.*)'
# # parts = get_groups(reg, my_str)



