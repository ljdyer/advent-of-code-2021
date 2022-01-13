from helper import *
from solution_p1 import count_on_method_one

regex = r"(on|off) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)"



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
    # coord += 50
    return coord


# ====================
def count_on(three_d_matrix):
    """Count the total number of cubes that are on in the 3D matrix"""

    all_cubes = [z for x in three_d_matrix for y in x for z in y]
    return all_cubes.count(True)


# ====================

# === Part One ===


def union_and_intersection(cube1, cube2):

    c1xl, c1xu = cube1[0]
    c1yl, c1yu = cube1[1]
    c1zl, c1zu = cube1[2]
    c2xl, c2xu = cube2[0]
    c2yl, c2yu = cube2[1]
    c2zl, c2zu = cube2[2]

    Uxl = max(c1xl, c2xl)
    Uxu = min(c1xu, c2xu)
    Uyl = max(c1yl, c2yl)
    Uyu = min(c1yu, c2yu)
    Uzl = max(c1zl, c2zl)
    Uzu = min(c1zu, c2zu)

    if Uxl <= Uxu and Uyl <= Uyu and Uzl <= Uzu:
        union = [((Uxl, Uxu),(Uyl, Uyu),(Uzl,Uzu))]
    else:
        return False

    intersection = []
    # X axis
    # min
    if c1xl < Uxl:
        intersection.append(((c1xl, Uxl-1), (c1yl, c1yu), (c1zl, c1zu)))
        c1xl = Uxl
    if c2xl < Uxl:
        intersection.append(((c2xl, Uxl-1), (c2yl, c2yu), (c2zl, c2zu)))
        c2xl = Uxl
    # max
    if c1xu > Uxu:
        intersection.append(((Uxu+1, c1xu), (c1yl, c1yu), (c1zl, c1zu)))
        c1xu = Uxu
    if c2xu > Uxu:
        intersection.append(((Uxu+1, c2xu), (c2yl, c2yu), (c2zl, c2zu)))
        c2xu = Uxu

    # Y axis
    if c1yl < Uyl:
        intersection.append(((c1xl, c1xu), (c1yl, Uyl-1), (c1zl, c1zu)))
        c1yl = Uyl
    if c2yl < Uyl:
        intersection.append(((c1xl, c1xu), (c2yl, Uyl-1), (c2zl, c2zu)))
        c2yl = Uyl
    # max
    if c1yu > Uyu:
        intersection.append(((c2xl, c2xu), (Uyu+1, c1yu), (c1zl, c1zu)))
        c1yu = Uyu
    if c2yu > Uyu:
        intersection.append(((c2xl, c2xu), (Uyu+1, c2yu), (c2zl, c2zu)))
        c2yu = Uyu

    # Y axis
    if c1zl < Uzl:
        intersection.append(((c1xl, c1xu), (c1yl, c1yu), (c1zl, Uzl-1)))
        c1zl = Uzl
    if c2zl < Uzl:
        intersection.append(((c1xl, c1xu), (c1yl, c1yu), (c2zl, Uzl-1)))
        c2zl = Uzl
    # max
    if c1zu > Uzu:
        intersection.append(((c2xl, c2xu), (c2yl, c2yu), (Uzu+1, c1zu)))
        c1zu = Uzu
    if c2zu > Uzu:
        intersection.append(((c2xl, c2xu), (c2yl, c2yu), (Uzu+1, c2zu)))
        c2zu = Uzu
    
    return (union, intersection)


def all_cube_sizes(cubes) -> int:

    total = 0
    for cube in cubes:
        total += cube_size(cube)
    return total


def cube_size(cube) -> int:

    x_min, x_max = cube[0]
    y_min, y_max = cube[1]
    z_min, z_max = cube[2]

    x_range = x_max - x_min + 1
    y_range = y_max - y_min + 1
    z_range = z_max - z_min + 1

    return x_range * y_range * z_range


def two_cubes(cube1, cube2):

    union, intersection = union_and_intersection(cube1,cube2)
    all = union+intersection
    return all_cube_sizes(all)


def reduce_cubes(cubes):

    for i in range(len(cubes)):
        for j in range(i+1, len(cubes)):
            if i!= j:
                if union_and_intersection(cubes[i], cubes[j]):

                    union, intersection = union_and_intersection(cubes[i], cubes[j])
                    del cubes[i]
                    del cubes[j-1]
                    cubes.extend(union + intersection)
                    return reduce_cubes(cubes)
    else:
        return(cubes)




lines = get_lines_from_file("test1.txt")
lines = [get_info(line) for line in lines]
print(lines[0])
cubes = [(x,y,z) for _,x,y,z in lines]
print(cubes[0])

print(reduce_cubes(cubes[:2]))
print(count_on_method_one(cubes[:6]))