# Takes around 95 seconds to run

from timebudget import timebudget
from copy import deepcopy
from tabulate import tabulate
import os
import time
import random

EMPTY_BURROW = [
    list('...........'),
    list('##.#.#.#.##'),
    list('##.#.#.#.##'),
    list('##.#.#.#.##'),
    list('##.#.#.#.##')
]

HALLWAY_POSITIONS = [0, 1, 3, 5, 7, 9, 10]
SIDE_ROOM_POSITIONS = [2, 4, 6, 8]
SIDE_ROOM_FIRST_ROW = 1
SIDE_ROOM_LAST_ROW = 4
SIDE_ROOM_ROWS = list(range(SIDE_ROOM_FIRST_ROW, SIDE_ROOM_LAST_ROW + 1))
SIDE_ROOM_ROWS_REVERSED = list(reversed(SIDE_ROOM_ROWS))
LETTER_TO_POS = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
POS_TO_LETTER = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
AMPHIPOD_WEIGHT = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


# ====================
class BurrowState:

    # ====================
    def __init__(self, rows: list):
        """Elements of list 'row' are strings like 'ADCB', 'CABD' that specify
        the order in which the amphipods start on each row"""

        burrow = []
        burrow.append(list('...........'))
        for row in rows:
            burrow.append(list('##' + '#'.join(list(row)) + '##'))
        self.burrow = burrow
        self.move_log = []
        self.total_energy = 0

    # ====================
    def __str__(self):

        return '\n'.join(''.join(row) for row in self.burrow)

    # ====================
    def finished(self):
        """Return True if all amphipods are in their finishing state"""

        arrangements = [''.join(self.burrow[row]).replace('#', '')
                        for row in SIDE_ROOM_ROWS]
        if all([a == 'ABCD' for a in arrangements]):
            return True

    # ====================
    def move(self, start: tuple, end: tuple):

        start_row, start_col = start
        end_row, end_col = end
        # Calculate energy required and add to total energy
        energy = self.energy(start, end)
        self.total_energy += energy
        # Move the amphipod
        self.burrow[end_row][end_col] = self.burrow[start_row][start_col]
        self.burrow[start_row][start_col] = '.'
        self.move_log.append((start, end))

    # ====================
    def energy(self, start: tuple, end: tuple) -> int:
        """Calculate the amount of energy required to move from start to
        end"""

        start_row, start_col = start
        end_row, end_col = end
        amphipod_type = self.burrow[start_row][start_col]
        v_dist = vertical_distance(start_row, end_row)
        h_dist = abs(end_col - start_col)
        raw_dist = v_dist + h_dist
        weighted_dist = raw_dist * AMPHIPOD_WEIGHT[amphipod_type]
        return weighted_dist

    # ====================
    def hallway_empty(self, start_row, end_row) -> bool:
        """Return true if all the spaces in the hallway between the start
        and end rows are empty"""

        if all([self.burrow[0][b] == '.'
                for b in between(start_row, end_row)]):
            return True
        else:
            return False

    # ====================
    def next_moves(self):
        """Return all optimal or all possible next moves for the current
        state"""

        # Generate a list of tuples containing positions of amphipods
        # that can move
        movables = []
        for pos in HALLWAY_POSITIONS:
            # Amphipods in the hallway
            if self.burrow[0][pos] != '.':
                movables.append((0, pos, self.burrow[0][pos]))
        for pos in SIDE_ROOM_POSITIONS:
            # Amphipods in side rooms that are not obstructed or already in
            # their finishing position
            if all(self.burrow[row][pos] == POS_TO_LETTER[pos]
                   or self.burrow[row][pos] == '.'
                   for row in SIDE_ROOM_ROWS):
                pass
            elif row := next(
                (row for row in SIDE_ROOM_ROWS
                 if self.burrow[row][pos].isalpha()), None):
                movables.append((row, pos, self.burrow[row][pos]))

        # Can we move any amphipods into their finishing position?
        for row, pos, a_type in movables:
            target_pos = LETTER_TO_POS[a_type]
            if pos != target_pos and self.hallway_empty(pos, target_pos):
                for row_ in SIDE_ROOM_ROWS_REVERSED:
                    # Move to lowest empty row provided that every other
                    # amphipod in that side room is in their finishing position
                    if all(self.burrow[r][target_pos] == '.'
                           for r in range(row_, SIDE_ROOM_FIRST_ROW-1, -1)) \
                       and all(self.burrow[r][target_pos] == a_type
                               for r in range(row_+1, SIDE_ROOM_LAST_ROW+1)):
                        return [((row, pos), (row_, target_pos))]

        # If not, consider all possible moves out of rooms into the hallway
        possible_moves = []
        for row, pos, a_type in movables:
            if row != 0:
                if LETTER_TO_POS[a_type] == pos \
                   and all(self.burrow[row_][pos] == LETTER_TO_POS[a_type]
                           for row_ in range(row, SIDE_ROOM_LAST_ROW)):
                    pass
                else:
                    for target_pos in HALLWAY_POSITIONS:
                        if self.hallway_empty(pos, target_pos):
                            possible_moves.append(
                                ((row, pos), (0, target_pos)))
        return possible_moves


# === HELPER FUNCTIONS FOR BurrowState CLASS ===

def vertical_distance(start_row: int, end_row: int) -> int:
    """Return the number of spaces that need to be moved in the vertical
    direction (up or down) to get from a space in row1 to a space in row2"""

    if start_row == 0:
        return end_row
    elif end_row == 0:
        return start_row
    else:
        return start_row + end_row


# ====================
def between(start: int, end: int) -> list:
    """Get all positions in the hallway between start and end"""

    if start < end:
        return list(range(start + 1, end + 1))
    else:
        return list(range(end, start))


# === TESTS & VISUALISATIONS ===

# ====================
def animate_steps(state: BurrowState, steps: list):

    # Print starting state
    os.system('cls')
    print(state)

    # Print each step
    for start, end in steps:
        time.sleep(0.5)
        os.system('cls')
        energy = state.energy(start, end)
        state.move(start, end)
        print(state)
        print("Energy used in last step:", energy)
        print("Total energy used:", state.total_energy)
        print(state.next_moves())
        print()


# ====================
def test_energy(state: BurrowState, steps: list, expected_energy: int):

    for start, end in steps:
        state.move(start, end)
    try:
        assert state.total_energy == expected_energy
        print('test_energy passed.')
    except AssertionError:
        print('!!! test_energy failed !!!')
        quit()
    finally:
        print()


# ====================
def animate_random_steps(state: BurrowState):

    # Print start state
    os.system('cls')
    print(state)

    # Animate steps
    for _ in range(100):
        time.sleep(2)
        os.system('cls')
        try:
            start, end = random.choice(state.next_moves())
        except IndexError:
            print(state)
            print("Can't move!")
            return None
        state.move(start, end)
        print(state)
        print(state.total_energy)

        if state.finished():
            print("Finished!")
            return None


# ====================
def test_find_best(start_state: BurrowState, best_so_far: int,
                   expected_energy: int):

    print("=== test_find_best ===")
    actual = find_best(start_state, best_so_far)
    try:
        assert actual == expected_energy
        print('Test passed.')
    except AssertionError:
        print("!!! TEST FAILED !!!", actual, expected_energy)


# === SOLUTION ===

def find_best(start_state: BurrowState, best_so_far: int) -> int:
    """Print the lowest energy requirement required to get all amphipods into
    their finishing position from the starting state.

    best_so_far can be chosen as any arbitrary value. The lower it is, the
    less time calculation will take. If no better value is found, choose a
    higher value next time"""

    best_solution = None
    print(best_so_far)

    # Start with only the starting state
    states = [start_state]

    # 25 below is an arbitrary value. The search is expected to complete
    # sooner, but increase the value as necessary.
    for _ in range(25):
        # Remove any states that have exceeded the minimum energy found so far
        for b in states:
            if b.total_energy >= best_so_far:
                continue
            else:
                # Add new states for all possible (or optimal) next moves
                # for each state in the list
                new_states = []
                for state in states:
                    poss_moves = state.next_moves()
                    for m in poss_moves:
                        new_state = deepcopy(state)
                        start, end = m
                        new_state.move(start, end)
                        # If the finishing state is reached, check whether it
                        # is a new minimum
                        if new_state.finished():
                            if new_state.total_energy < best_so_far:
                                best_so_far = new_state.total_energy
                                best_solution = new_state.move_log
                        # If no more moves are possible, remove the state
                        elif not new_state.next_moves():
                            pass
                        else:
                            new_states.append(new_state)
                # If there are new unfinished states, use them for the next
                # iteration
                if new_states:
                    states = new_states
                # Otherwise, exit
                else:
                    print()
                    print(tabulate(best_solution))
                    return best_so_far
                print(len(states), best_so_far)


# === TEST DATA ===

TEST_START_STATE = BurrowState(['BCBD', 'DCBA', 'DBAC', 'ADCA'])
TEST_STEPS = [
    ((1, 8), (0, 10)),
    ((2, 8), (0, 0)),
    ((1, 6), (0, 9)),
    ((2, 6), (0, 7)),
    ((3, 6), (0, 1)),
    ((1, 4), (3, 6)),
    ((2, 4), (2, 6)),
    ((3, 4), (0, 5)),
    ((4, 4), (0, 3)),
    ((0, 5), (4, 4)),
    ((0, 7), (3, 4)),
    ((0, 9), (2, 4)),
    ((3, 8), (1, 6)),
    ((4, 8), (0, 9)),
    ((0, 3), (4, 8)),
    ((1, 2), (1, 4)),
    ((2, 2), (3, 8)),
    ((3, 2), (0, 3)),
    ((0, 1), (3, 2)),
    ((0, 0), (2, 2)),
    ((0, 3), (2, 8)),
    ((0, 9), (1, 2)),
    ((0, 10), (1, 8))
]
TEST_EXPECTED_ENERGY = 44169


# === ACTUAL DATA ===

ACTUAL_START_STATE = BurrowState(['DADC', 'DCBA', 'DBAC', 'CABB'])


# ====================
# animate_steps(TEST_START_STATE, TEST_STEPS)
with timebudget('find_best'):
    find_best(ACTUAL_START_STATE, 50000)
