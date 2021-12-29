from helper import *

# lines = get_lines_from_file("test.txt")
lines = get_lines_from_file("data.txt")
matrix = [list(l) for l in lines]
NUM_ROWS = len(matrix)
NUM_COLS = len(matrix[0])
coords = [(x,y) for x in range(NUM_ROWS) for y in range(NUM_COLS)]

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

# print_matrix(matrix)

def move_east(coord):

    x,y = coord
    return (x, (y + 1) % NUM_COLS)

def move_south(coord):

    x,y = coord
    return ((x + 1) % NUM_ROWS, y)

def attempt_move_east(coord, matrix):

    new_x, new_y = move_east(coord)
    if matrix[new_x][new_y] == '.':
        return (new_x, new_y)
    else:
        return coord


def attempt_move_south(coord, matrix):

    new_x, new_y = move_south(coord)
    if matrix[new_x][new_y] == '.':
        return (new_x, new_y)
    else:
        return coord


def generate_matrix(east_facing, south_facing, num_cols, num_rows):

    new_matrix = [['.' for col in range(num_cols)] for row in range(num_rows)]
    for x,y in east_facing:
        new_matrix[x][y] = '>'
    for x,y in south_facing:
        new_matrix[x][y] = 'v'
    return new_matrix

# ====================
def step_forward(matrix):

    num_moved = 0
    # Get current positions
    old_east_facing = [(x,y) for x,y in coords if matrix[x][y] == '>']
    old_south_facing = [(x,y) for x,y in coords if matrix[x][y] == 'v']

    # East-facing sea cucumbers move
    new_east_facing = [attempt_move_east((x,y), matrix) for x,y in old_east_facing]
    num_moved += len([x for x in new_east_facing if x not in old_east_facing])
    matrix = generate_matrix(new_east_facing, old_south_facing, NUM_COLS, NUM_ROWS)

    # South-facing sea cucumbers move
    new_south_facing = [attempt_move_south((x,y), matrix) for x,y in old_south_facing]
    num_moved += len([x for x in new_south_facing if x not in old_south_facing])
    matrix = generate_matrix(new_east_facing, new_south_facing, NUM_COLS, NUM_ROWS)

    return (matrix, num_moved)
    # return matrix

x = 0
while True:
    matrix, num_moved = step_forward(matrix)
    x += 1
    if num_moved == 0:
        break
    
print(x)