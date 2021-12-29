from helper import *

# ====================
def print_matrix(num_rows, num_cols, easties, southies):
    """For testing purposes"""

    matrix = [['.' for col in range(num_cols)] for row in range(num_rows)]
    for row, positions in easties.items():
        for p in positions:
            matrix[row][p] = '>'
    for col, positions in southies.items():
        for p in positions:
            matrix[p][col] = 'v'
    for row in matrix:
        print(''.join(row))


# Get data
lines = get_lines_from_file("data.txt")
matrix = [list(l) for l in lines]
NUM_ROWS = len(matrix)
NUM_COLS = len(matrix[0])

# Store positions of east- and south-facing cucumbers in dictionaries with
# row/column lists of positions as values
easties = {
    row: [col for col in range(NUM_COLS) if matrix[row][col] == '>']
    for row in range(NUM_ROWS)
}
southies = {
    col: [row for row in range(NUM_ROWS) if matrix[row][col] == 'v']
    for col in range(NUM_COLS)
}

steps = 0
# Whether or not any sea cucumbers moved in this step
moved = True

while moved == True:
    steps += 1
    moved = False

    # Move east-facing sea cucumbers
    for row, positions in easties.items():
        new_positions = []
        for i in range(len(positions)):
            new_pos = (positions[i] + 1) % NUM_COLS
            if new_pos not in positions and row not in southies[new_pos]:
                new_positions.append(new_pos)   # Do not move yet
                moved = True
            else:
                new_positions.append(positions[i])
        easties[row] = new_positions            # All move now

    # Move south-facing cucumbers
    for col, positions in southies.items():
        new_positions = []
        for i in range(len(positions)):
            new_pos = (positions[i] + 1) % NUM_ROWS
            if new_pos not in positions and col not in easties[new_pos]:
                new_positions.append(new_pos)   # Do not move yet
                moved = True
            else:
                new_positions.append(positions[i])
        southies[col] = new_positions           # All move now

print(steps)