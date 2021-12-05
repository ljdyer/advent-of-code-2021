from helper import *
from tabulate import tabulate

# Get data
# lines = get_lines_from_file("test.txt")
lines = get_lines_from_file("data.txt")

def get_vals(l):
    l = l.split(" -> ")
    l = [int(x) for lin in l for x in lin.split(",")]
    return l

def is_h_or_v(l):
    if l[0] == l[2] or l[1] == l[3]:
        return True
    else:
        return False

split = [get_vals(l) for l in lines]

# grid = [[0 for n in range(10)] for n in range(10)]
grid = [[0 for n in range(1000)] for n in range(1000)]

for l in split:
    # if l[0] == l[2]:
    #     pass
    #     x = l[0]
    #     y1 = l[1]
    #     y2 = l[3]
    #     if y1 < y2:
    #         for i in range(y1, y2 + 1):
    #             grid[i][x] += 1
    #     else:
    #         for i in range(y1, y2 - 1,-1):
    #             grid[i][x] += 1
    # elif l[1] == l[3]:
    #     pass
    #     y = l[1]
    #     x1 = l[0]
    #     x2 = l[2]
    #     if x1 < x2:
    #         for i in range(x1, x2 + 1):
    #             grid[y][i] += 1
    #     else:
    #         for i in range(x1, x2 - 1,-1):
    #             grid[y][i] += 1
    # else:
    x1 = l[1]
    x2 = l[3]
    y1 = l[0]
    y2 = l[2]
    print(x1,x2,y1,y2)
    if x1 < x2:
        xrange = list(range(x1,x2+1))
    elif x1 > x2:
        xrange = list(range(x1,x2-1,-1))

    if y1 < y2:
        yrange = list(range(y1,y2+1))
    elif y1 > y2:
        yrange = list(range(y1,y2-1,-1))

    if x1==x2:
        xrange = [x1 for i in list(range(len(yrange)))]
    if y1==y2:
        yrange = [y1 for i in list(range(len(xrange)))]
    print(xrange)
    print(yrange)
    points = list(zip(xrange, yrange))
    print(points)
    print()
    
    # if x1 < x2 and y1 < y2:
    # elif x1 > x2 and y1 < y2:
    #     points = list(zip(range(x1,x2-1,-1), range(y1,y2+1)))
    # elif x1 < x2 and y1 > y2:
    #     points = list(zip(range(x1,x2+1), range(y1,y2-1,-1)))
    # elif x1 > x2 and y1 > y2:
    #     points = list(zip(range(x1,x2-1,-1), range(y1,y2-1,-1)))
    # elif x1 == x2
    # else:
    #     print("What about me???")
    #     points = []
    
    for x,y in points:
        grid[x][y] += 1

        
        


print(tabulate(grid))

print(len([x for g in grid for x in g if x > 1]))











# === REGEX ===
# # Get instances of 'foo', 'bar' from string
# alpha = "foo|bar"
# subs = get_substrings(alpha, my_str)

# Parse string into parts
# reg = r'(.*)-(.*) (.*): (.*)'
# parts = get_groups(reg, my_str)



