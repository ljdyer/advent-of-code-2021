import ast
import math

# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines

# ========================================

def list_to_map(lis_: list, i_s: list = None, map_: list = None) -> list:

    if i_s == None:
        i_s = []
    if map_ == None:
        map_ = []
    for count, e in enumerate(lis_):    
        if isinstance(e, int):
            map_.append((i_s+[count], e))
        else:
            map_.append(list_to_map(e, i_s+[count], map_))
    return [t for t in map_ if isinstance(t, tuple)]


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
        return [map_to_list([(ind[1:], e) for ind, e in m if ind[0] == 0]), map_to_list([(ind[1:], e) for ind, e in m if ind[0] == 1])]
    elif left:
        return [left[0][1], map_to_list([(ind[1:], e) for ind, e in m if ind[0] == 1])]
    elif right:
        return [map_to_list([(ind[1:], e) for ind, e in m if ind[0] == 0]), right[0][1]]


# =========================================

def add_int_to_ind_ent(ind_ent, num):
    return ind_ent[0], ind_ent[1] + num

def split_num(num):
    return (math.floor(num/2), math.ceil(num/2))

def reduction_step(l):
    m = list_to_map(l)
    for count, (ind, e) in enumerate(m):
        if e >= 10:
            # print(f'Split {e}')
            left, right = split_num(e)
            left = (ind + [0], left)
            right = (ind + [1], right)
            m = m[:count] + [left, right] + m[count+1:]
            # print(m)
            # print(map_to_list(m))
            return (True, map_to_list(m))
        elif len(ind) == 5 and ind[-1] == 0 and m[count+1][0][-1] == 1:
            # print(f'Explode {e, m[count+1][1]}')
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
            # print(m)
            # print(map_to_list(m))
            return (True, map_to_list(m))

        
    return (False, l)

def reduce(l):
    while True:
        do_again, l = reduction_step(l)
        # print(l)
        if not do_again:
            return l
    
# =======================================

def add(l1, l2):
    return [l1, l2]

def added_and_reduced(filename):
    lines = get_lines_from_file(filename)
    lines = [ast.literal_eval(l) for l in lines]
    x = lines[0]
    for l in lines[1:]:
        x = add(x, l)
        x = reduce(x)
    return x

# ===========================

