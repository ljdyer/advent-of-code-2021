# ====================
def fold_y(y_fold, matrix):
    """Fold paper along horizontal line"""
    
    lines_above_fold = matrix[:y_fold]
    lines_below_fold = matrix[len(matrix):y_fold:-1]
    for i in range(len(lines_below_fold)):
        for y in range(len(lines_above_fold[i])):
            if lines_below_fold[i][y] == '#':
                lines_above_fold[i][y] = '#'
    return lines_above_fold


# ====================
def fold_x(x_fold, matrix):
    """Fold paper along vertical line"""

    lines_left_fold = [l[:x_fold] for l in matrix]
    lines_right_fold = [l[len(l):x_fold:-1] for l in matrix]
    for row in range(len(lines_right_fold)):
        for column in range(len(lines_left_fold[row])):
            if lines_right_fold[row][column] == '#':
                lines_left_fold[row][column] = '#'
    return lines_left_fold


# ====================
def fold(direction, position, matrix):

    """Fold the paper along either a horizontal or vertical line"""
    if direction == "x":
        return fold_x(position, matrix)
    elif direction == "y":
        return fold_y(position, matrix)


# ====================
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                print("X", end='')
            else:
                print(" ", end = '')
        print()


# === MAIN PART ===

# Get data
with open("data.txt", encoding='utf-8') as file:
    lines = file.read().splitlines()

# Parse lines
lines = [l.split('-') for l in lines]
blank_line = lines.index([''])

# Get dots
dots = lines[:blank_line]
dots = [l[0].split(',') for l in dots]
dots = [(int(x), int(y)) for x,y in dots]

# Get instructions
instructions = lines[blank_line+1:]
instructions = [i[0].partition('=') for i in instructions]
instructions = [(parts[0][-1], int(parts[2])) for parts in instructions]

# Generate paper
num_rows = max([int(x[0]) for x in dots]) + 1
num_columns = max([int(x[1]) for x in dots]) + 1
# My method needs odd numbers of rows and columns to work
if num_rows % 2 == 0:
    num_rows = num_rows + 1
if num_columns % 2 == 0:
    num_columns = num_columns + 1
matrix = [['.' for m in range(num_rows)] for n in range(num_columns)]

# Mark dots
for x,y in dots:
    matrix[y][x] = '#'

# Carry out instructions
for dir, pos in instructions:
    matrix = fold(dir,pos,matrix)

# Print result
print_matrix(matrix)