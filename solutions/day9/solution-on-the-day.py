from helper import *

# Get data
lines = get_lines_from_file("test.txt")

lines = [[int(x) for x in l] for l in lines]

def in_range(i,j):
    try:
        if i>-1 and j >-1 and lines[i][j] > -1:
            return True
        else:
            return False
    except:
        return False

def get_compare_points(i,j):

    return [(x,y) for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if in_range(x,y)]


def get_basin(i,j, basin):
    
    compare_points = get_compare_points(i,j)

    for x,y in compare_points:
        if (x,y) not in basin:
            this = lines[x][y]    
            new_compare_points = [(a,b) for (a,b) in get_compare_points(x,y) if not (a,b) in basin and lines[a][b] < 9]
            if all([lines[a][b] >= this for (a,b) in new_compare_points]):
                basin.extend(get_basin(x,y,basin+[(x,y)]))


    return list(set(basin))


def print_basin(this_basin):

    print()
    for p in range(len(lines)):
        print()
        for q in range(len(lines[0])):
            if (p,q) in this_basin:
                print(lines[p][q], end='')
            else:
                print('-', end='')

risk = []
basin_sizes = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        this = lines[i][j]
        compare_points = get_compare_points(i,j)
        if all([lines[x][y] > this for x,y in compare_points]):
            risk.append(this+1)
            this_basin = get_basin(i,j,[(i,j)])
            this_basin_size = len([(x,y) for x,y in this_basin if lines[x][y]<9])
            # if this_basin_size > 70:
            #     print_basin(this_basin)
            # print_basin(this_basin)
                    

            basin_sizes.append(this_basin_size)

        
    
print(sum(risk))
x = list(sorted(basin_sizes))
print(x)
print(x[-3] * x[-2] * x[-1])
