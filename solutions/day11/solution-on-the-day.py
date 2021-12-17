from helper import *


# ====================
def get_surrounding_points(i,j):
    """Return a list of up to four points surrounding the point i, j"""

    return [
        (x,y) for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1), (i+1, j+1), (i-1, j-1), (i+1,j-1), (i-1,j+1)]
        if is_in_range(x,y)
    ]

# ====================
def is_in_range(i,j):
    """Find out if an i, j is a valid address in a list of lists"""
    try:
        if i>-1 and j >-1 and octopi[i][j] > -1:
            return True
        else:
        # i < 0 or j < 0
            return False
    except:
        # lines[i][j] threw an error
        return False

# Get data
lines = get_lines_from_file("data.txt")

octopi = [[int(n) for n in sublist] for sublist in lines]

i = len(octopi)
j = len(octopi[0])
total_flashes = 0

def flash_point(x,y):
    global points_flashed
    points_flashed.append((x,y))
    perimeter = get_surrounding_points(x,y)
    for a,b in perimeter:
        octopi[a][b] += 1
        if octopi[a][b] > 9 and (a,b) not in points_flashed:
            flash_point(a,b)


for t in range(500):
    # First, the energy level of each octopus increases by 1.
    octopi = [[n+1 for n in sublist] for sublist in octopi]

    points_flashed = []
    continue_this = True

    while continue_this:
        for x in range(i):
            for y in range(j):
                flashed_this_time = 0
                if (x,y) not in points_flashed and octopi[x][y] > 9:
                    flash_point(x,y)
                    flashed_this_time += 1
                if flashed_this_time < 1:
                    continue_this = False

    for x,y in points_flashed:
        total_flashes += 1
        octopi[x][y] = 0

    if(len(points_flashed)) == 100:
        print(t+1)
        exit(-1)

print_first_n(100, octopi)
print(total_flashes)



        

# Then, any octopus
# with an energy level greater than 9 flashes. This increases the energy level
# of all adjacent octopuses by 1, including octopuses that are diagonally
# adjacent. If this causes an octopus to have an energy level greater than 9,
# it also flashes. This process continues as long as new octopuses keep having
# their energy level increased beyond 9. (An octopus can only flash at most
# once per step.)
# 
# Finally, any octopus that flashed during this step has its
# energy level set to 0, as it used all of its energy to flash.
# lines = [l for l in lines]


# print_last_n(100, lines)
# write_lines_to_file("new.txt", lines)










# === REGEX ===
# # Get instances of 'foo', 'bar' from string
# alpha = "foo|bar"
# subs = get_substrings(alpha, my_str)

# Parse string into parts
# reg = r'(.*)-(.*) (.*): (.*)'
# parts = get_groups(reg, my_str)



