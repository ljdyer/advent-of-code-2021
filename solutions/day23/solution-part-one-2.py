from copy import deepcopy
import os
import time
import random

"""
Some definitions:

A BURROW consists of 3 AREAS: hallway, top_row, and bottom_row.

There are 4 ROOMS: A, B, C, and D.

Each ROOM has one place in top_row and one in bottom_row.
"""

EMPTY_BURROW = [
    list('...........'),
    list('##.#.#.#.##'),
    list('##.#.#.#.##')
]

LETTER_TO_POS = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
VERTICAL_DISTANCE = {
    # TODO: Convert to a function
    (0, 1): 1,
    (0, 2): 2,
    (2, 0): 2,
    (2, 1): 3,
    (2, 2): 4,
    (1, 0): 1,
    (1, 1): 2,
    (1, 2): 3,
}
AMPHIPOD_WEIGHT = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
HALLWAY_POSITIONS = [0, 1, 3, 5, 7, 9, 10]
AMPHIPOD_TYPES = list('ABCD')


# ====================
class BurrowState:

    # ====================
    def __init__(self, top_state: str, bottom_state: str):
        """top_state and bottom_state are strings like 'ADCB', 'CABD' that
        specify the order in which the amphipods start on the top and bottom
        rows"""

        burrow = EMPTY_BURROW.copy()
        burrow[1] = list('##' + '#'.join(list(top_state)) + '##')
        burrow[2] = list('##' + '#'.join(list(bottom_state)) + '##')
        self.burrow = burrow
        self.total_energy = 0
        self.move_log = []

    # ====================
    def __str__(self):

        return '\n'.join(''.join(row) for row in self.burrow)

    # ====================
    def finished(self):
        """Return True if all amphipods are in their finishing state"""

        top_row = ''.join([c for c in self.burrow[1] if c != '#'])
        bottom_row = ''.join([c for c in self.burrow[1] if c != '#'])
        if top_row == 'ABCD' and bottom_row == 'ABCD':
            return True

    # ====================
    def move(self, start: tuple, end: tuple):

        start_row, start_col = start
        end_row, end_col = end

        # Calculate energy required and add to total energy
        energy = self.energy(start, end)
        self.total_energy += energy
        # Make a record of the move in the log
        self.move_log.append((start, end, energy))
        # Move the amphipod
        self.burrow[end_row][end_col] = self.burrow[start_row][start_col]
        self.burrow[start_row][start_col] = '.'

    # ====================
    def energy(self, start: tuple, end: tuple) -> int:
        """Calculate the amount of energy required to move from start to
        end"""

        # TODO: Move outside of class to own function
        start_row, start_col = start
        end_row, end_col = end
        amphipod_type = self.burrow[start_row][start_col]
        v_dist = VERTICAL_DISTANCE[(start_row, end_row)]
        h_dist = abs(end_col - start_col)
        raw_dist = v_dist + h_dist
        weighted_dist = raw_dist * AMPHIPOD_WEIGHT[amphipod_type]
        return weighted_dist

    # ====================
    def next_moves(self):
        """Return all optimal or all possible next moves for the current
        state"""

        hallway_empty = [pos for pos, c in enumerate(self.burrow[0])
                         if c == '.']
        hallway_occupied = [pos for pos, c in enumerate(self.burrow[0])
                            if c in c.isalpha()]
        top_occupied = [pos for pos, c in enumerate(self.burrow[1])
                        if c in c.isalpha()]
        bottom_occupied = [pos for pos, c in enumerate(self.burrow[2])
                           if c in c.isalpha()]

        # Can an amphipod in the hallway move into the bottom row?
        for pos in hallway_occupied:
            a_type = self.burrow[0][pos]
            target_pos = LETTER_TO_POS[a_type]
            if self.burrow[2][target_pos] == '.':
                if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                    return [((0, pos), (2, target_pos))]

        # Can an amphipod in the hallway move into the top row?
        for pos in hallway_occupied:
            a_type = self.burrow[0][pos]
            target_pos = LETTER_TO_POS[a_type]
            if self.burrow[2][target_pos] == a_type \
               and self.burrow[1][target_pos] == '.':
                if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                    return [((0, pos), (1, target_pos))]

        # Can an amphipod in the top row move to its own room?
        for pos in top_occupied:
            a_type = self.burrow[1][pos]
            target_pos = LETTER_TO_POS[a_type]
            if pos == target_pos:
                pass
            elif self.burrow[2][target_pos] == '.':
                if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                    return [((1, pos), (2, pos))]
            elif self.burrow[2][target_pos] == a_type \
                 and self.burrow[1][target_pos] == '.':
                if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                    return [((1, pos), (1, target_pos))]

        # Can an amphipod in the bottom row move to its own room?
        for pos in bottom_occupied:
            a_type = self.burrow[2][pos]
            target_pos = LETTER_TO_POS[a_type]
            if pos == target_pos:
                pass
            elif self.burrow[1][pos] == '.':
                if self.burrow[2][target_pos] == '.':
                    if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                        return [((2, pos), (2, pos))]
                if self.burrow[2][target_pos] == a_type \
                   and self.burrow[1][target_pos] == '.':
                    if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                        return [((2, pos), (1, target_pos))]

        # If none of the above options are available, consider all moves out
        # of rooms into hallway
        possible_moves = []

        for pos in top_occupied:
            a_type = self.burrow[1][pos]
            target_pos = LETTER_TO_POS[a_type]
            if pos == target_pos and self.burrow[2][target_pos] == a_type:
                pass
            else:
                for hallway_pos in hallway_empty:
                    if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                        possible_moves.append(((1, pos), (0, hallway_pos)))

        for pos in bottom_occupied:
            a_type = self.burrow[2][pos]
            target_pos = LETTER_TO_POS[a_type]
            if pos == target_pos:
                pass
            else:
                if self.burrow[1][pos] == '.':
                    for hallway_pos in hallway_empty:
                        if all([self.burrow[0][b] == '.' for b in between(pos, target_pos)]):
                            possible_moves.append(((1, pos), (0, hallway_pos)))

        return possible_moves

    
# === HELPER FUNCTIONS FOR BurrowState CLASS ===

# ====================
def vertical_distance(start_row: int, end_row: int) -> int:
    # NEED TO TEST THIS AND SUB IN

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
        return range(start + 1, end + 1)
    else:
        return range(end + 1, start + 1)


# === TESTS & VISUALISATIONS ===

# ====================
def animate_steps(state: BurrowState, steps: list):

    # Print starting state
    # os.system('cls')
    print(state)

    # Print each step
    for start, end in steps:
        time.sleep(1)
        # os.system('cls')
        energy = state.energy(start, end)
        state.move(start, end)
        print(state)
        print("Energy used in last step:", energy)
        print("Total energy used:", state.total_energy)
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
        except:
            print(state)
            print("Can't move!")
            return None
        state.move(start, end)
        print(state)
        print(state.total_energy)
        if state.finished():
            print("Finished!")
            return None


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
        states = [b for b in states if b.total_energy < best_so_far]
        # Add new states for all possible (or optimal) next moves for each
        # state in the list
        new_states = []
        for state in states:
            poss_moves = state.next_moves()
            for m in poss_moves:
                new_state = deepcopy(state)
                start, end = m
                new_state.move(start, end)
                # If the finishing state is reached, check whether it is a new
                # minimum
                if new_state.finished():
                    if new_state.total_energy < best_so_far:
                        best_so_far = new_state.total_energy
                        best_solution = new_state.move_log
                # If no more moves are possible, remove the state
                elif not new_state.next_moves():
                    pass
                else:
                    new_states.append(new_state)
        # If there are new unfinished states, use them for the next iteration
        if new_states:
            states = new_states
        # Otherwise, exit
        else:
            print()
            print(tabulate(best_solution))
            quit()
        print(len(states), best_so_far)


# === TEST DATA ===

LETTER_TO_POS = {'A': 3, 'B': 5, 'C': 7, 'D': 9}

TEST_START_STATE = BurrowState('BCBD', 'ADCA')
TEST_STEPS = [
    ((1, 6), (0, 3)),
    ((1, 4), (1, 6)),
    ((2, 4), (0, 5)),
    ((0, 3), (2, 4)),
    ((1, 2), (1, 4)),
    ((1, 8), (0, 7)),
    ((2, 8), (0, 9)),
    ((0, 7), (2, 8)),
    ((0, 5), (1, 8)),
    ((0, 9), (1, 2))
]
TEST_EXPECTED_ENERGY = 12521


# === ACTUAL DATA ===

# ACTUAL_START_STATE = BurrowState('DADC', 'CABB')


# ====================
animate_steps(TEST_START_STATE, TEST_STEPS)
# find_best(ACTUAL_START_STATE, 20000)
