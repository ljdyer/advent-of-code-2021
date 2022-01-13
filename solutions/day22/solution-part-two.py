"""Took over an hour to complete, but got the right answer!"""

import re

regex = \
    r"(on|off) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)"


# ====================
class Cuboid():

    # ====================
    def __init__(self, coords):

        self.x, self.X, self.y, self.Y, self.z, self.Z = coords

    # ====================
    def __repr__(self):

        return f'[({self.x}, {self.X}), ({self.y},' + \
            f' {self.Y}), ({self.z}, {self.Z})]'

    # ====================
    def volume(self):

        return \
            (self.X - self.x + 1) \
            * (self.Y - self.y + 1) \
            * (self.Z - self.z + 1) \



# ====================
def get_groups(regex, text) -> tuple:

    return re.findall(regex, text)[0]


# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# ====================
def parse_line(line):
    """Get necessary information from lines in text file"""

    groups = get_groups(regex, line)
    instruction = groups[0]
    cuboid = Cuboid(
        [int(c) for c in groups[1:]]
    )
    return (instruction, cuboid)


# ====================
def cubes_overlap(cube1, cube2):

    return max(cube1.x, cube2.x) <= min(cube1.X, cube2.X) \
        and max(cube1.y, cube2.y) <= min(cube1.Y, cube2.Y) \
        and max(cube1.z, cube2.z) <= min(cube1.Z, cube2.Z)


# ====================
def intersection(cube1, cube2):

    intersection = []

    if cube1.x < cube2.x:
        intersection.append(
            Cuboid((cube1.x, cube2.x-1, cube1.y, cube1.Y, cube1.z, cube1.Z)))
        cube1.x = cube2.x
    if cube1.X > cube2.X:
        intersection.append(
            Cuboid((cube2.X+1, cube1.X, cube1.y, cube1.Y, cube1.z, cube1.Z)))
        cube1.X = cube2.X
    if cube1.y < cube2.y:
        intersection.append(
            Cuboid((cube1.x, cube1.X, cube1.y, cube2.y-1, cube1.z, cube1.Z)))
        cube1.y = cube2.y
    if cube1.Y > cube2.Y:
        intersection.append(
            Cuboid((cube1.x, cube1.X, cube2.Y+1, cube1.Y, cube1.z, cube1.Z)))
        cube1.Y = cube2.Y
    if cube1.z < cube2.z:
        intersection.append(
            Cuboid((cube1.x, cube1.X, cube1.y, cube1.Y, cube1.z, cube2.z - 1)))
        cube1.z = cube2.z
    if cube1.Z > cube2.Z:
        intersection.append(
            Cuboid((cube1.x, cube1.X, cube1.y, cube1.Y, cube2.Z+1, cube1.Z)))
        cube1.Z = cube2.Z

    return(intersection)


# ====================
def reduce_list(cubes):

    for i in range(len(cubes)):
        for j in range(len(cubes)):
            if i != j and cubes_overlap(cubes[i], cubes[j]):
                return reduce_list(cubes[:i] + cubes[i+1:] +
                    intersection(cubes[i], cubes[j]))
    else:
        return cubes


# ====================
def turn_off(all_cubes, cube):

    after = []
    for i in range(len(all_cubes)):
        if cubes_overlap(all_cubes[i], cube):
            after.extend(intersection(all_cubes[i], cube))
        else:
            after.append(all_cubes[i])

    return after


# ====================
def sum_volumes(cuboid_list: list) -> int:

    return sum(cuboid.volume() for cuboid in cuboid_list)


# ====================
lines = get_lines_from_file("data.txt")
lines = [parse_line(line) for line in lines]
cubes = [cube for _, cube in lines]
# lines = lines[:11]
all_cubes = []

while lines:
    on_or_off, cube = lines.pop(0)
    if on_or_off == 'on':
        all_cubes.append(cube)
        all_cubes = reduce_list(all_cubes)
    else:
        all_cubes = turn_off(all_cubes, cube)
    print(len(all_cubes), len(lines))

print(sum_volumes(all_cubes))
