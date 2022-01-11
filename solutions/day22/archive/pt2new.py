from helper import *

regex = r"(on|off) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)"

lines = get_lines_from_file("data.txt")


# ====================
def get_info(line):
    """Get necessary information from lines in text file"""

    groups = get_groups(regex, line)

    return [
        groups[0],
        (normalize(groups[1]), normalize(groups[2])),
        (normalize(groups[3]), normalize(groups[4])),
        (normalize(groups[5]), normalize(groups[6]))
    ]


# ====================
def normalize(coord: str) -> int:
    """Convert coordinates to integers and remove negative list indices
    by converting from numbers between -50 and 50 to numbers between 
    0 and 100"""

    coord = int(coord)
    coord += 50
    return coord


# ====================
def count_on(three_d_matrix):
    """Count the total number of cubes that are on in the 3D matrix"""

    all_cubes = [z for x in three_d_matrix for y in x for z in y]
    return all_cubes.count(True)


# ====================
lines = [get_info(l) for l in lines]

# === Part One ===
three_d_matrix = [ [ [False for x in range(101)] 
                      for y in range(101) ]
                      for z in range(101) ]

for line in lines:
    if line[0] == 'on':
        # Turn on
        new_val = True
    else:
        # Turn off
        new_val = False
    x1, x2 = line[1]
    y1,y2 = line[2]
    z1, z2 = line[3]
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                three_d_matrix[x][y][z] = new_val

print(count_on(three_d_matrix))