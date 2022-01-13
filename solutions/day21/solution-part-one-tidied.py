# from itertools import islice

FIRST_TEST = {'start': 7, 'rolls': [2, 2, 1], 'total': 2}
SECOND_TEST = {'p1_start': 4, 'p2_start': 8, 'answer': 739785}
ACTUAL = {'p1_start': 5, 'p2_start': 10}

# # === TESTS ===


# # ====================
# def first_test():
#     print('=== first_test ===')

#     pos = FIRST_TEST['start']
#     pos = move(pos, FIRST_TEST['rolls'])
#     try:
#         assert pos == FIRST_TEST['total']
#         print('Passed.')
#     except AssertionError:
#         print('Failed!')
#     print()


# # ====================
# def test_die_1_to_100():
#     print('=== test_die_1_to_100 ===')

#     die = die_1_to_100()
#     first_1000_actual = list(islice(die, 1000))
#     first_1000_expected = list(range(1, 101)) * 10
#     try:
#         assert first_1000_expected == first_1000_actual
#         print('Passed.')
#     except AssertionError:
#         print('Failed!')
#     print()


# # ====================
# def second_test():
#     print('=== second_test ===')

#     answer_actual = play_game(SECOND_TEST['p1_start'], SECOND_TEST['p2_start'])
#     answer_expected = SECOND_TEST['answer']

#     try:
#         assert answer_actual == answer_expected
#         print('Passed.')
#     except AssertionError:
#         print('Failed!')
#     print()


# # === MAIN FUNCTIONS ===

# # ====================
# def move(start: int, rolls: list) -> int:
#     """Move forward based on list of rolls"""

#     total = sum(rolls)
#     end = (start + total) % 10
#     return end


# # ====================
# def score(pos: int) -> int:

#     if pos == 0:
#         return 10
#     else:
#         return pos


# # ====================
# def die_1_to_100():
#     """Generate rolls of a die that counts up by 1 each time and loops back to
#     1 when it exceeds 100"""

#     x = 1
#     while True:
#         yield x
#         x = (x % 100) + 1


# # ====================
# def play_game(p1_pos, p2_pos):
#     """Play game until one player reaches 1000"""

#     p1_score = 0
#     p2_score = 0
#     die = die_1_to_100()
#     num_rolls = 0
#     next_three_rolls = []

#     while True:
#         next_three_rolls = []
#         for _ in range(3):
#             next_three_rolls.append(next(die))
#         p1_pos = move(p1_pos, next_three_rolls)
#         num_rolls += 3
#         p1_score += score(p1_pos)
#         if p1_score >= 1000:
#             # Player 1 wins
#             loser_score = p2_score
#             break

#         next_three_rolls = []
#         for _ in range(3):
#             next_three_rolls.append(next(die))
#         p2_pos = move(p2_pos, next_three_rolls)
#         num_rolls += 3
#         p2_score += score(p2_pos)
#         if p2_score >= 1000:
#             # Player 2 wins
#             loser_score = p1_score
#             break

#     answer = loser_score * num_rolls
#     return answer


# # === MAIN PART OF PROGRAM ===

# first_test()
# test_die_1_to_100()
# second_test()

# answer = play_game(ACTUAL['p1_start'], ACTUAL['p2_start'])
# print('Answer:', answer)


# === Part One ===

p1_score = 0
p2_score = 0
p1_pos = ACTUAL['p1_start']
p2_pos = ACTUAL['p2_start']
next_player = 1
die = 1
num_rolls = 0

while True:
    three_rolls = (die + (die % 100) + 1 + (die % 100) + 2)
    die = (die % 100) + 1
    num_rolls += 3
    if next_player == 1:
        p1_pos = ((p1_pos - 1 + three_rolls) % 10) + 1
        p1_score += p1_pos
        if p1_score >= 1000:
            # Player 1 wins
            loser_score = p2_score
            break
    elif next_player == 2:
        p2_pos = ((p2_pos - 1 + three_rolls) % 10) + 1
        p2_score += p2_pos
        if p2_score >= 1000:
            # Player 1 wins
            loser_score = p1_score
            break

print('Part One answer:', loser_score * num_rolls)


# === Part Two ===

# Pre-calculated possible total values from three rolls of the die
poss_totals = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

# Initialise empty counter dictionary for games
games = {
    p1_score: {
        p2_score: {
            p1_pos: {
                p2_pos: 0 for p2_pos in range(1, 11)}
            for p1_pos in range(1, 11)}
        for p2_score in range(21)}
    for p1_score in range(21)
}
# Add starting game state
games[0][0][ACTUAL['p1_start']][ACTUAL['p2_start']] = 1

p1_wins = 0
p2_wins = 0
next_player = 1

for _ in range(100):

    # Initialise new counter dictionary
    new_games = {
        p1_score: {
            p2_score: {
                p1_pos: {
                    p2_pos: 0 for p2_pos in range(1, 11)}
                for p1_pos in range(1, 11)}
            for p2_score in range(21)}
        for p1_score in range(21)
    }

    # Loop over existing games
    for p1_score in games.keys():
        for p2_score in games[p1_score].keys():
            for p1_pos in games[p1_score][p2_score].keys():
                for p2_pos in games[p1_score][p2_score][p1_pos].keys():
                    num_games = games[p1_score][p2_score][p1_pos][p2_pos]
                    # Simulate next turn
                    if num_games > 0:
                        if next_player == 1:
                            for amt, times in poss_totals.items():
                                new_pos = ((p1_pos - 1 + amt) % 10) + 1
                                new_score = p1_score + new_pos
                                if new_score >= 21:
                                    p1_wins += num_games * times
                                else:
                                    new_games[new_score][p2_score] \
                                        [new_pos][p2_pos] \
                                        += num_games * times
                        elif next_player == 2:
                            for amt, times in poss_totals.items():
                                new_pos = ((p2_pos - 1 + amt) % 10) + 1
                                new_score = p2_score + new_pos
                                if new_score >= 21:
                                    p2_wins += num_games * times
                                else:
                                    new_games[p1_score][new_score] \
                                        [p1_pos][new_pos] \
                                        += num_games * times

    if next_player == 1:
        next_player = 2
    else:
        next_player = 1
    games = new_games

print(p1_wins)
print(p2_wins)
