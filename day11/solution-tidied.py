from helper import *
import itertools as it

# ====================
def get_surrounding_points(i,j):

    return [
        (x,y) for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),
                            (i+1, j+1),(i-1, j-1),(i+1,j-1),(i-1,j+1)]
        if is_in_range(x,y)
    ]

# ====================
def is_in_range(i,j):
    """Find out if an i, j is a valid address in octopus list"""
    try:
        if i>-1 and j >-1 and octopi[i][j] > -1:
            return True
        else:
        # i < 0 or j < 0
            return False
    except:
        # lines[i][j] threw an error
        return False


# ====================
def flash_point(x,y):
    points_flashed.append((x,y))
    perimeter = get_surrounding_points(x,y)
    for a,b in perimeter:
        octopi[a][b] += 1
        if octopi[a][b] > 9 and (a,b) not in points_flashed:
            flash_point(a,b)


# ====================
# Get data
lines = get_lines_from_file("data.txt")
octopi = [[int(n) for n in sublist] for sublist in lines]
i = len(octopi)
j = len(octopi[0])


# === Part 1 ===

total_flashes = 0
num_steps = 100

for t in range(1,num_steps+1):

    # First, the energy level of each octopus increases by 1.
    octopi = [[n+1 for n in sublist] for sublist in octopi]

    # Then, any octopus with an energy level greater than 9 flashes. This
    # increases the energy level of all adjacent octopuses by 1, including
    # octopuses that are diagonally adjacent. If this causes an octopus to
    # have an energy level greater than 9, it also flashes. This process
    # continues as long as new octopuses keep having their energy level
    # increased beyond 9. (An octopus can only flash at most once per step.)
    points_flashed = []
    no_more_flashes = False
    while not no_more_flashes:
        no_more_flashes = True
        for x, y in it.product(range(i), range(j)):
            if (x,y) not in points_flashed and octopi[x][y] > 9:
                flash_point(x,y)
                no_more_flashes = False

    # Finally, any octopus that flashed during this step has its energy level
    # set to 0, as it used all of its energy to flash.
    for x,y in points_flashed:
        total_flashes += 1
        octopi[x][y] = 0

print(total_flashes)


# === Part 2 ===

# Same as Part 1, but continue until all points are synchronized.

octopi = [[int(n) for n in sublist] for sublist in lines]
t = 0

while True:

    # Same as Part 1...
    octopi = [[n+1 for n in sublist] for sublist in octopi]
    points_flashed = []
    no_more_flashes = False
    while not no_more_flashes:
        no_more_flashes = True
        for x, y in it.product(range(i), range(j)):
            if (x,y) not in points_flashed and octopi[x][y] > 9:
                flash_point(x,y)
                no_more_flashes = False
    for x,y in points_flashed:
        total_flashes += 1
        octopi[x][y] = 0
    t += 1

    # Print t if all points flashed in last iteration
    if(len(points_flashed)) == 100:
        print(t)
        exit(-1)

