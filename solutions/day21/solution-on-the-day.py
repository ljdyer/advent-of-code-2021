
import math
from helper import *



START_ROLLS_ANSWER = [
    (7, [2,2,1], 2)
]

def test_forward_x():
    print('=== test_forward_x ===')
    for S, R, A in START_ROLLS_ANSWER:
        pos = S
        for r in R:
            pos = forward_x(pos, r)
        try:
            assert pos == A
        except:
            print('Failed!')
            print(S)
            print(R)
            print(pos)
            exit()
    print('Passed.')
    print()


def test_forward_rolls():
    print('=== test_forward_rolls ===')
    for S, R, A in START_ROLLS_ANSWER:
        pos = S
        pos = forward_rolls(S, R)
        try:
            assert pos == A
        except:
            print('Failed!')
            print(S)
            print(R)
            print(pos)
            exit()
    print('Passed.')
    print()


def test_file():
    print('=== test_file ===')
    p_one, p_two = positions_from_txt_file('test.txt')
    try:
        assert p_one == 4
        assert p_two == 8
    except:
        print('Failed!')
        print(p_one)
        print(p_two)
        exit()
    print('Passed.')
    print()


def forward_one(x: int) -> int:
    """Move forward one space"""

    x += 1
    if x > 11:
        assert False
    if x == 11:
        x = 1
    return x


def forward_x(start: int, x: int) -> int:
    """Move forward x spaces"""

    for _ in range(x):
        start = forward_one(start)
    return start


def forward_rolls(start: int, rolls: list) -> int:
    """Move forward based on rolls"""

    total = sum(rolls)
    start = forward_x(start, total)
    return start


def positions_from_txt_file(filename) -> tuple:

    lines = get_lines_from_file(filename)
    player_one_pos = int(lines[0].partition(':')[2])
    player_two_pos = int(lines[1].partition(':')[2])
    return (player_one_pos, player_two_pos)


def next_roll(die: int) -> int:

    die += 1
    if die > 101:
        assert False
    if die == 101:
        die = 1
    return die



# ============================================================

test_forward_x()
test_forward_rolls()
test_file()

# ============================================================

# filename = 'test.txt'

# p1_pos, p2_pos = positions_from_txt_file(filename)
# print('Player one start position:', p1_pos)
# print('Player two start position:', p2_pos)

# def play_game(p1_pos, p2_pos, rolls: list):

#     p1_score = 0
#     p2_score = 0
#     die = 1
#     num_rolls = 0
#     next_three_rolls = []
    
#     while True:
    
#         for _ in range(3):
#             next_three_rolls.append(rolls.pop(0))
#             die = next_roll(die)
#         p1_pos = forward_rolls(p1_pos, next_three_rolls)
#         num_rolls += 3
#         p1_score += p1_pos
#         if p1_score >= 1000:
#             return 1

#         next_three_rolls = []
#         for _ in range(3):
#             next_three_rolls.append(die)
#             die = next_roll(die)
#         p2_pos = forward_rolls(p2_pos, next_three_rolls)
#         num_rolls += 3
#         p2_score += p2_pos
#         if p2_score >= 1000:
#             return 2

# print(play_game(p1_pos, p2_pos))

# print('Player one:', p1_score)
# print('Player two:', p2_score)
# print('Number of rolls:', num_rolls)
# print('Answer:', num_rolls * min(p1_score, p2_score))

# ============================================================

# rolls

rolls = [1,2,3,4,5,6]
# print(len(rolls))
# print(p1_scores)
# print(p2_scores)
# print(scores)
p1_pos = 4
p2_pos = 8

def play_game(p1_pos, p2_pos, rolls):

    p1_score = 0
    p2_score = 0
    scores = [ sum(rolls[3*x:3*x+3]) for x in range(math.floor(len(rolls)/3))]
    # print(scores)
    p1_scores = [scores[x] for x in range(len(scores)) if x % 2 == 0]
    p2_scores = [scores[x] for x in range(len(scores)) if x % 2 == 1]
    while p1_scores:
        next = p1_scores.pop(0)
        p1_pos = forward_x(p1_pos, next)
        p1_score += p1_pos
    while p2_scores:
        next = p2_scores.pop(0)
        # print(next)
        p2_pos = forward_x(p2_pos, next)
        p2_score += p2_pos
    
    return (p1_score, p2_score, len(scores))
    
x = 2
while True:
    rolls = list(range(1,x))
    p1_score, p2_score, num_rolls = play_game(p1_pos, p2_pos, rolls)
    print(p1_score)
    if p1_score > 999 or p2_score > 999:
        print(num_rolls)
        exit()
        break
    x+= 1