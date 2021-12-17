from helper import *

# Get data
lines = get_lines_from_file("data.txt")


# ====================
def check_board(board, numbers_so_far):
    for row in board:
        if all([x in numbers_so_far for x in row]):
            return True
    else:
        inverted_board = list(map(list, zip(*board)))
        for column in inverted_board:
            if all([x in numbers_so_far for x in column]):
                return True
        else:
            return False


# ====================
def get_score(board, numbers_so_far):
    all_nums = [x for row in board for x in row]
    remaining_nums = [x for x in all_nums if x not in numbers_so_far]
    return sum(remaining_nums) * numbers_so_far[-1]


# ====================
def first_winning_board(boards, numbers_so_far):
    for board in boards:
        if check_board(board, numbers_so_far):
            return get_score(board, numbers_so_far)
    else:
        return None


# === Part 1 ===
numbers = [int(n) for n in lines[0].split(",")]
board_lines = list(map(lambda x: [int(e) for e in x.split(" ") if e], lines[2:]))
boards = [board_lines[i:i+5] for i in range(0,len(lines),6)]
numbers_so_far = []

for num in numbers:
    numbers_so_far.append(num)
    first_score = first_winning_board(boards, numbers_so_far)
    if first_score:
        print(first_score)
        break
    else:
        continue


# === Part 2 ===
numbers = [int(n) for n in lines[0].split(",")]
board_lines = list(map(lambda x: [int(e) for e in x.split(" ") if e], lines[2:]))
boards = [board_lines[i:i+5] for i in range(0,len(lines)-1,6)]
numbers_so_far = []
round = 1

# Remove winning boards until only one is left
while len(boards) > 1:
    round += 1
    numbers_so_far = numbers[:round]
    boards = [board for board in boards if not check_board(board, numbers_so_far)]
last_board = boards[0]

# Continue drawing numbers until last board wins
while not check_board(last_board, numbers_so_far):
    round += 1
    numbers_so_far = numbers[:round]
    
print(get_score(boards[0], numbers_so_far))