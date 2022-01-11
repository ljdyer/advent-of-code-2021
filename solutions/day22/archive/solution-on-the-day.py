from helper import *

regex = r"(on|off) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)"
lines = get_lines_from_file("test.txt")
lines = get_lines_from_file("test2.txt")
# lines = get_lines_from_file("data.txt")

# ====================
def parse_groups(groups):

    return [groups[0], (normalize(groups[1]), normalize(groups[2])), (normalize(groups[3]), normalize(groups[4])), (normalize(groups[5]), normalize(groups[6]))]

# ====================
def normalize(coord):

    coord = int(coord)
    coord += 500000
    return coord

lines = [parse_groups(get_groups(regex, l)) for l in lines]

print(lines)
# CODE
# SOLUTION

# def test_1(test_file):

#     assert x == y

three_d_matrix = [[[False for x in range(1000001)] for y in range(1000001)] for z in range(1000001)]

def count_on(three_d_matrix):

    all_cubes = [z for x in three_d_matrix for y in x for z in y]
    return all_cubes.count(True)


# print(count_on(three_d_matrix))

for line in lines:
    if line[0] == 'on':
        new_val = True
    else:
        new_val = False
    x1, x2 = line[1]
    y1,y2 = line[2]
    z1, z2 = line[3]
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                three_d_matrix[x][y][z] = new_val

print(count_on(three_d_matrix))


