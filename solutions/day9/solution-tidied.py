from helper import *

# Get data
lines = get_lines_from_file("data.txt")
# Parse points into list of lists
lines = [[int(x) for x in l] for l in lines]


# ====================
def is_in_range(i,j):
    """Find out if an i, j is a valid address in a list of lists"""
    try:
        if i>-1 and j >-1 and lines[i][j] > -1:
            return True
        else:
        # i < 0 or j < 0
            return False
    except:
        # lines[i][j] threw an error
        return False


# ====================
def get_surrounding_points(i,j):
    """Return a list of up to four points surrounding the point i, j"""

    return [
        (x,y) for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        if is_in_range(x,y)
    ]


# ====================
def get_basin(i,j, basin):
    """Get a list of the points in the basin around a point i, j"""

    surrounding_points = get_surrounding_points(i,j)

    for x,y in surrounding_points:
        # If the point is not already in the list
        if (x,y) not in basin:
            this = lines[x][y]    
            # If this point is lower than all surrounding points
            # not already in basin, add this point to basin and
            # check surrounding points that have height less than 9
            new_surrounding_points = [
                (a,b) for (a,b) in get_surrounding_points(x,y)
                if (a,b) not in basin and lines[a][b] < 9
            ]
            if all([lines[a][b] >= this for (a,b) in new_surrounding_points]):
                basin.append((x,y))
                basin.extend(get_basin(x,y,basin))

    return list(set(basin))


# ====================
def print_basin(this_basin):
    """Print a basin to the terminal"""

    print()
    for p in range(len(lines)):
        print()
        for q in range(len(lines[0])):
            if (p,q) in this_basin:
                print(lines[p][q], end='')
            else:
                print('-', end='')


# ====================
risk = []
basin_sizes = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        this = lines[i][j]
        surrounding_points = get_surrounding_points(i,j)
        # If i,j is a low point
        if all([lines[x][y] > this for x,y in surrounding_points]):
            risk.append(this+1)
            this_basin = get_basin(i,j,[(i,j)])
            this_basin_size = len([(x,y) for x,y in this_basin if lines[x][y]<9])
            basin_sizes.append(this_basin_size)


# === Part 1 ===        

print(sum(risk))

# === Part 2 ===

basin_sizes_sorted = list(sorted(basin_sizes))
print(basin_sizes_sorted[-3] * basin_sizes_sorted[-2] * basin_sizes_sorted[-1])
