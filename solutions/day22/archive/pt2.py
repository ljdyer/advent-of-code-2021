from helper import *

regex = r"(on|off) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)"

lines = get_lines_from_file("test.txt")
# lines = get_lines_from_file("test2.txt")
# lines = get_lines_from_file("data.txt")

points = set({})


class Cube:
    def __init__(self, x_range, y_range, z_range):

        self.x_min, self.x_max = x_range
        self.y_min, self.y_max = y_range
        self.z_min, self.z_max = z_range

    def __str__(self):

        return f'X: {str(self.x_min).ljust(8)} {str(self.x_max).ljust(8)} |  '.ljust(20) + \
               f'Y: {str(self.y_min).ljust(8)} {str(self.y_max).ljust(8)} |  '.ljust(20) + \
               f'Z: {str(self.z_min).ljust(8)} {str(self.z_max).ljust(8)} |  '.ljust(20)

    def all_on(self):

        for x in range(self.x_min, self.x_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                for z in range(self.z_min, self.z_max + 1):
                    points.add((x,y,z))

    def all_off(self):

        for x in range(self.x_min, self.x_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                for z in range(self.z_min, self.z_max + 1):
                    if (x,y,z) in points:
                        points.remove((x,y,z))




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
    return coord


# ====================
def count_on(three_d_matrix):
    """Count the total number of cubes that are on in the 3D matrix"""

    all_cubes = [z for x in three_d_matrix for y in x for z in y]
    return all_cubes.count(True)


# ====================
lines = [get_info(l) for l in lines]


# ====================

cubes_and_statuses = [(status, Cube(x_range, y_range, z_range)) for status, x_range, y_range, z_range in lines]

for s, c in cubes_and_statuses[:1]:
    if s == 'on':
        c.all_on()
    if s == 'off':
        c.all_off()

print(len(points))
