# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# ====================
def get_boards(lines: list) -> list:
    """Parse lines from data to generate list of bingo boards"""

    boards = []
    while lines:
        boards.append([[int(n) for n in line.split()]
                       for line in lines[:5]])
        lines = lines[6:]
    return boards


# ====================
def check_board(board: list, numbers_so_far: list):
    """Check whether a board has won"""

    # Check rows
    for row in range(5):
        if all([x in numbers_so_far for x in board[row]]):
            return True
    else:
        # Check columns
        for col in range(5):
            if all([board[row][col] in numbers_so_far for row in range(5)]):
                return True
        else:
            return False


# ====================
def get_score(board, numbers_so_far):
    """Calculate the score of a winning board"""

    all_nums = [x for row in board for x in row]
    remaining_nums = [x for x in all_nums if x not in numbers_so_far]
    return sum(remaining_nums) * numbers_so_far[-1]


# ====================
def first_winning_board_score(boards, numbers_so_far):
    """Find the score of the first winning board"""

    for board in boards:
        if check_board(board, numbers_so_far):
            return get_score(board, numbers_so_far)
    else:
        return None


# Get data
lines = get_lines_from_file("data.txt")


# === Part 1 ===

numbers = [int(n) for n in lines[0].split(",")]
boards = get_boards(lines[2:])
numbers_so_far = []

for num in numbers:
    numbers_so_far.append(num)
    first_score = first_winning_board_score(boards, numbers_so_far)
    if first_score:
        print(first_score)
        break


# === Part 2 ===

numbers = [int(n) for n in lines[0].split(",")]
boards = get_boards(lines[2:])
numbers_so_far = []
round = 1

# Remove winning boards until only one is left
while len(boards) > 1:
    round += 1
    numbers_so_far = numbers[:round]
    boards = [board for board in boards
              if not check_board(board, numbers_so_far)]

last_board = boards[0]

# Continue drawing numbers until last board wins
while not check_board(last_board, numbers_so_far):
    round += 1
    numbers_so_far = numbers[:round]

print(get_score(boards[0], numbers_so_far))
