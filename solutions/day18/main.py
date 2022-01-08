import ast
import math


# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# ====================
def list_to_map(lis_: list, i_s: list = None, map_: list = None) -> list:
    """Convert from a list of lists to a 'map' of the depths and elements"""

    if i_s is None:
        i_s = []
    if map_ is None:
        map_ = []
    for count, e in enumerate(lis_):
        if isinstance(e, int):
            map_.append((i_s+[count], e))
        else:
            map_.append(list_to_map(e, i_s+[count], map_))
    return [t for t in map_ if isinstance(t, tuple)]


# ====================
def map_to_list(m):

    if m == []:
        return 0
    left = [e for e in m if e[0] == [0]]
    if left:
        m = [e for e in m if e[0] != [0]]
    right = [e for e in m if e[0] == [1]]
    if right:
        m = [e for e in m if e[0] != [1]]
    if left and right:
        return [left[0][1], right[0][1]]
    elif not left and not right:
        return [
            map_to_list([(ind[1:], e) for ind, e in m if ind[0] == 0]),
            map_to_list([(ind[1:], e) for ind, e in m if ind[0] == 1])]
    elif left:
        return [left[0][1], map_to_list([(ind[1:], e)
                for ind, e in m if ind[0] == 1])]
    elif right:
        return [map_to_list([(ind[1:], e)
                for ind, e in m if ind[0] == 0]), right[0][1]]


# ====================
def add_int_to_ind_ent(ind_ent, num):
    return ind_ent[0], ind_ent[1] + num


# ====================
def split_num(num):
    """Split a number according to the rules of snailfish arithmetic"""
    return (math.floor(num/2), math.ceil(num/2))


# ====================
def reduction_step(input_list: list) -> tuple:
    """Perform either an explosion or a split, or do nothing

    The first element of the tuple returned is the resulting list

    The second element of the tuple returned is True if an explosion or split
    was performed, or False otherwise"""

    m = list_to_map(input_list)

    # Perform an explosion if possible
    for count, (ind, e) in enumerate(m):
        if len(ind) == 5 and ind[-1] == 0 and m[count+1][0][-1] == 1:
            # Add to left
            if count == 0:
                pass
            else:
                m[count-1] = add_int_to_ind_ent(m[count-1], e)
            # Add to right
            if count >= len(m) - 2:
                pass
            else:
                m[count+2] = add_int_to_ind_ent(m[count+2], m[count+1][1])
            # Convert self to 0
            m = m[:count] + [(ind[:-1], 0)] + m[count+2:]
            return (True, map_to_list(m))

    else:
        # Perform a split if possible
        for count, (ind, e) in enumerate(m):
            if e >= 10:
                left, right = split_num(e)
                left = (ind + [0], left)
                right = (ind + [1], right)
                m = m[:count] + [left, right] + m[count+1:]
                return (True, map_to_list(m))

    return (False, input_list)


# ====================
def reduce(input_list):
    """Reduce a snailfish number"""

    while True:
        do_again, input_list = reduction_step(input_list)
        if not do_again:
            return input_list


# ====================
def add(l1, l2):
    return [l1, l2]


# ====================
def added_and_reduced(filename):
    lines = get_lines_from_file(filename)
    lines = [ast.literal_eval(line) for line in lines]
    x = lines[0]
    for line in lines[1:]:
        x = add(x, line)
        x = reduce(x)
    return x


# ====================
def magnitude(snum: list) -> int:
    """Get the magnitude of a snailfish number"""

    left, right = tuple(snum)
    if not isinstance(left, int):
        left = magnitude(left)

    if not isinstance(right, int):
        right = magnitude(right)

    return 3 * left + 2 * right


# ====================
def magnitude_from_file(filename):

    lines = get_lines_from_file(filename)
    lines = [ast.literal_eval(line) for line in lines]
    x = lines[0]
    for line in lines[1:]:
        x = add(x, line)
        x = reduce(x)
    mag = magnitude(x)

    return mag


# ====================
def max_magnitude(snums: list) -> int:
    """Given a list of snailfish numbers, return the largest magnitude you can get
    from adding only two of the snailfish numbers.

    Note that snailfish addition is not commutative"""

    max = 0

    for snum1 in snums:
        for snum2 in snums:
            sum = add(snum1, snum2)
            reduced = reduce(sum)
            mag = magnitude(reduced)
            if mag > max:
                max = mag
    return max


# ====================
def max_magnitude_from_file(filename) -> int:

    lines = get_lines_from_file(filename)
    snums = [ast.literal_eval(line) for line in lines]
    return max_magnitude(snums)


# ====================
print('Part One answer:', magnitude_from_file('data.txt'))
print('Part Two answer:', max_magnitude_from_file('data.txt'))