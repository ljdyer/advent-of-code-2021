from helper import *


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

lines = get_lines_from_file("test.txt")
# lines = get_lines_from_file("data.txt")
matrix = [list(l) for l in lines]
NUM_ROWS = len(matrix)
NUM_COLS = len(matrix[0])

for _ in range(58):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if matrix[row][col] == '>' and not skip_next:
                new_col = (col + 1) % NUM_COLS
                if matrix[row][new_col] == '.':
                    matrix[row][col] = '.'
                    matrix[row][new_col] = '>'
                    skip_next = True
            else:
                skip_next = False
            
    points_to_skip = []
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if matrix[row][col] == 'v' and (row,col) not in points_to_skip:
                new_row = (row + 1) % NUM_ROWS
                if matrix[new_row][col] == '.':
                    matrix[row][col] = '.'
                    matrix[new_row][col] = 'v'
                    points_to_skip.append((new_row,col))

print_matrix(matrix)