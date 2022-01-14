from helper import get_lines_from_file, get_groups

REGEX = \
    r"(on|off) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)"


# ====================
def parse_line(line: str):
    """Read a line from the problem data and return a list of 4 elements

    0: 'on' or 'off'
    1: tuple (start, end) of x coordinates
    2: tuple (start, end) of y coordinates
    3: tuple (start, end) of z coordinates"""

    groups = get_groups(REGEX, line)

    return [
        groups[0],
        (normalize(groups[1]), normalize(groups[2])),
        (normalize(groups[3]), normalize(groups[4])),
        (normalize(groups[5]), normalize(groups[6]))
    ]


# ====================
def normalize(coord: str) -> int:
    """Convert to integer and add 50 to make every value positive"""

    coord = int(coord)
    coord += 50
    return coord


# ====================
def count_on(instructions: list) -> int:
    """Carry out initialization procedure and return number of cubes that are
    on at the end"""

    # Reactor core is a 3D matrix of booleans representing cube on or off
    # states
    reactor_core = [[[False for x in range(101)]
                     for y in range(101)]
                    for z in range(101)]

    # Loop over instructions toggling elements (cubes) in reactor core
    for on_or_off, x_range, y_range, z_range in instructions:
        if on_or_off == 'on':
            new_val = True
        else:
            new_val = False
        x, X = x_range
        y, Y = y_range
        z, Z = z_range
        for x_ in range(x, X + 1):
            for y_ in range(y, Y + 1):
                for z_ in range(z, Z + 1):
                    reactor_core[x_][y_][z_] = new_val

    # Flatten matrix of reactor core states and return number of cubes
    # that are on
    all_cubes = [z for x in reactor_core for y in x for z in y]
    return all_cubes.count(True)


# ====================
if __name__ == "__main__":

    lines = get_lines_from_file("../data/data.txt")[:20]
    instructions = [parse_line(line) for line in lines]
    print(count_on(instructions))
