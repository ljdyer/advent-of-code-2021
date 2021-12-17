from helper import *
from tabulate import tabulate

# Get data
lines = get_lines_from_file("data.txt")
GRID_SIZE = 1000

# ====================
def get_line_coords(l):
    l = l.split(" -> ")
    l = [int(x) for lin in l for x in lin.split(",")]
    return l


# ====================
def make_square_grid(x):
    return [[0 for _ in range(x)] for _ in range(x)]


# ====================
def get_range(a, b):
    if a < b:
        return list(range(a,b+1))
    elif a > b:
        return list(range(a,b-1,-1))
    elif a == b:
        return [a for _ in range(GRID_SIZE)]


coords = [get_line_coords(l) for l in lines]


# === Part 1 ===
grid = make_square_grid(GRID_SIZE)
for l in coords:
    y1, x1, y2, x2 = l
    if x1 == x2 or y1 == y2:
        xrange = get_range(x1,x2)
        yrange = get_range(y1,y2)
        points = list(zip(xrange, yrange))
        for x,y in points:
            grid[x][y] += 1
print(len([x for g in grid for x in g if x > 1]))


# === Part 2 ===
grid = make_square_grid(GRID_SIZE)
for l in coords:
    y1, x1, y2, x2 = l
    xrange = get_range(x1,x2)
    yrange = get_range(y1,y2)
    points = list(zip(xrange, yrange))
    for x,y in points:
        grid[x][y] += 1
print(len([x for g in grid for x in g if x > 1]))