"""Took over an hour to complete, but got the right answer!"""

import os
import re

REGEX = \
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
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# ====================
def parse_line(line: str) -> tuple:
    """Get necessary information from lines in text file"""

    groups = re.findall(REGEX, line)[0]
    on_or_off = groups[0]
    cuboid = Cuboid(
        [int(c) for c in groups[1:]]
    )
    return (on_or_off, cuboid)


# ====================
def cuboids_overlap(cuboid1: Cuboid, cuboid2: Cuboid) -> bool:
    """Return True if the two cuboids overlap"""

    return max(cuboid1.x, cuboid2.x) <= min(cuboid1.X, cuboid2.X) \
        and max(cuboid1.y, cuboid2.y) <= min(cuboid1.Y, cuboid2.Y) \
        and max(cuboid1.z, cuboid2.z) <= min(cuboid1.Z, cuboid2.Z)


# ====================
def difference(cuboid1: Cuboid, cuboid2: Cuboid) -> list:
    """Return a list of cuboids that cover all the cubes that are included in
    cuboid1 but not in cuboid2"""

    difference = []

    if cuboid1.x < cuboid2.x:
        difference.append(
            Cuboid((cuboid1.x, cuboid2.x-1, cuboid1.y,
                    cuboid1.Y, cuboid1.z, cuboid1.Z)))
        cuboid1.x = cuboid2.x
    if cuboid1.X > cuboid2.X:
        difference.append(
            Cuboid((cuboid2.X+1, cuboid1.X, cuboid1.y,
                    cuboid1.Y, cuboid1.z, cuboid1.Z)))
        cuboid1.X = cuboid2.X
    if cuboid1.y < cuboid2.y:
        difference.append(
            Cuboid((cuboid1.x, cuboid1.X, cuboid1.y,
                    cuboid2.y-1, cuboid1.z, cuboid1.Z)))
        cuboid1.y = cuboid2.y
    if cuboid1.Y > cuboid2.Y:
        difference.append(
            Cuboid((cuboid1.x, cuboid1.X, cuboid2.Y+1,
                    cuboid1.Y, cuboid1.z, cuboid1.Z)))
        cuboid1.Y = cuboid2.Y
    if cuboid1.z < cuboid2.z:
        difference.append(
            Cuboid((cuboid1.x, cuboid1.X, cuboid1.y,
                    cuboid1.Y, cuboid1.z, cuboid2.z - 1)))
        cuboid1.z = cuboid2.z
    if cuboid1.Z > cuboid2.Z:
        difference.append(
            Cuboid((cuboid1.x, cuboid1.X, cuboid1.y,
                    cuboid1.Y, cuboid2.Z+1, cuboid1.Z)))
        cuboid1.Z = cuboid2.Z

    return(difference)


# ====================
def reduce_list(cuboids: list) -> list:
    """Reduce a list of cuboids such that each cube covered by the cuboids in
    the original list is included in exactly one cuboid"""

    for i in range(len(cuboids)):
        for j in range(len(cuboids)):
            if i != j and cuboids_overlap(cuboids[i], cuboids[j]):
                return reduce_list(
                    cuboids[:i] + cuboids[i+1:]
                    + difference(cuboids[i], cuboids[j])
                )
    else:
        return cuboids


# ====================
def turn_off(cuboids: list, cuboid: Cuboid) -> list:
    """Return a list of cuboids such that the cubes in the new cuboid are no
    longer included in any cuboid"""

    after = []

    for i in range(len(cuboids)):
        if cuboids_overlap(cuboids[i], cuboid):
            after.extend(difference(cuboids[i], cuboid))
        else:
            after.append(cuboids[i])

    return after


# ====================
def sum_volumes(cuboid_list: list) -> int:
    """Return the sum of the volumes of the cuboids in the list"""

    return sum(cuboid.volume() for cuboid in cuboid_list)


# ====================
def count_on(instructions: list) -> int:
    """Carry out initialization procedure and return number of cubes that are
    on at the end"""

    cuboids = []
    num_instructions = len(instructions)

    while instructions:
        on_or_off, cuboid = instructions.pop(0)
        if on_or_off == 'on':
            cuboids.append(cuboid)
            cuboids = reduce_list(cuboids)
        else:
            cuboids = turn_off(cuboids, cuboid)
        os.system('cls')
        completed = num_instructions - len(instructions)
        percent = \
            f'{(completed / num_instructions)*100:.1f}%'
        print(f"Carried out {completed}/{num_instructions} instructions" +
              f" ({percent})")
        print("Number of cuboids in list:", len(cuboids))

    print()
    return sum_volumes(cuboids)


# ====================
if __name__ == "__main__":

    lines = get_lines_from_file("data/data.txt")
    instructions = [parse_line(line) for line in lines]
    print("Part Two answer:", count_on(instructions))
