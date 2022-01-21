from tabulate import tabulate
from copy import deepcopy
from typing import Union
import os
import time
import random

"""
Some definitions:

A BURROW consists of 3 AREAS: hallway, top_row, and bottom_row.

There are 4 ROOMS: A, B, C, and D.

Each ROOM has one place in top_row and one in bottom_row.
"""

LETTER_TO_POS = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
VERTICAL_DISTANCE = {
    ('hallway', 'top_row'): 1,
    ('hallway', 'bottom_row'): 2,
    ('bottom_row', 'hallway'): 2,
    ('bottom_row', 'top_row'): 3,
    ('bottom_row', 'bottom_row'): 4,
    ('top_row', 'hallway'): 1,
    ('top_row', 'top_row'): 2,
    ('top_row', 'bottom_row'): 3,
}
AMPHIPOD_WEIGHT = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
HALLWAY_POSITIONS = [1, 2, 4, 6, 8, 10, 11]


# ====================
class BurrowState:

    # ====================
    def __init__(self, top_state: str, bottom_state: str):
        """top_state and bottom_state are strings like 'ADCB', 'CABD' that
        specify the order in which the amphipods start on the top and bottom
        rows"""

        self.hallway = {x: '.' for x in HALLWAY_POSITIONS}
        self.top_row = {x: y for x, y in zip(list('ABCD'), top_state)}
        self.bottom_row = {x: y for x, y in zip(list('ABCD'), bottom_state)}
        self.total_energy = 0
        self.move_log = []

    # ====================
    def __str__(self):

        rows = []
        h = sorted_dict_to_list(self.hallway)
        t = sorted_dict_to_list(self.top_row)
        b = sorted_dict_to_list(self.bottom_row)
        rows.append('#' * 13)
        rows.append('#' + h[0] + '.'.join(h[1:6]) + h[6] + '#')
        rows.append('#' * 3 + '#'.join(t) + '#' * 3)
        rows.append(('#' + '#'.join(b) + '#').center(13))
        rows.append(('#' * 9).center(13))
        rows.append('')
        return '\n'.join(rows)

    # ====================
    def get(self, area: str, pos) -> str:
        """Return the current state of the position in the area (one of '.',
        'A', 'B', 'C', or 'D')"""

        return getattr(self, area)[pos]

    # ====================
    def remove_amphipod(self, area: str, pos: Union[int, str]):

        state = getattr(self, area)
        state[pos] = '.'
        setattr(self, area, state)

    # ====================
    def place_amphipod(self, area: str, pos: Union[int, str],
                       amphipod_type: str):

        state = getattr(self, area)
        state[pos] = amphipod_type
        setattr(self, area, state)

    # ====================
    def move(self, start: tuple, end: tuple):

        # Calculate energy required and add to total energy
        energy = self.energy(start, end)
        self.total_energy += energy
        # Make a record of the move in the log
        self.move_log.append((start, end, energy))
        # Move the amphipod
        start_row, start_pos = start
        end_row, end_pos = end
        a_type = self.get(start_row, start_pos)
        self.remove_amphipod(start_row, start_pos)
        self.place_amphipod(end_row, end_pos, a_type)

    # ====================
    def energy(self, start: tuple, end: tuple) -> int:
        """Calculate the amount of energy required to move from start to
        end"""

        start_row, start_pos = start
        start_pos_abs = get_abs_pos(start)
        end_row, _ = end
        end_pos_abs = get_abs_pos(end)
        amphipod_type = self.get(start_row, start_pos)
        v_dist = VERTICAL_DISTANCE[(start_row, end_row)]
        h_dist = abs(start_pos_abs - end_pos_abs)
        raw_dist = v_dist + h_dist
        weighted_dist = raw_dist * AMPHIPOD_WEIGHT[amphipod_type]
        return weighted_dist

    # ====================
    def next_moves(self):
        """Return all optimal or all possible next moves for the current
        state"""

        h = self.hallway
        t = self.top_row
        b = self.bottom_row
        hallway_occupied = [(pos, h[pos]) for pos in h.keys()
                            if h[pos] != '.']
        top_occupied = [(pos, t[pos]) for pos in t.keys()
                        if t[pos] != '.']
        bottom_occupied = [(pos, b[pos]) for pos in b.keys()
                           if b[pos] != '.']
        hallway_empty = [pos for pos in h.keys() if h[pos] == '.']

        # Can an amphipod in the hallway move into the bottom row?
        for pos, a in hallway_occupied:
            if b[a] == '.':
                positions = hallway_positions_between(('hallway', pos),
                                                      ('bottom_row', a))
                if all([h[pos] == '.' for pos in positions]):
                    return [(('hallway', pos), ('bottom_row', a))]

        # Can an amphipod in the hallway move into the top row?
        for pos, a in hallway_occupied:
            if b[a] == a and t[a] == '.':
                positions = hallway_positions_between(('hallway', pos),
                                                      ('top_row', a))
                if all([h[pos] == '.' for pos in positions]):
                    return [(('hallway', pos), ('top_row', a))]

        # Can an amphipod in the top row move to its own room?
        for pos, a in top_occupied:
            if b[a] == '.' and t[a] == '.':
                positions = hallway_positions_between(('top_row', pos),
                                                      ('top_row', a))
                if all([h[pos] == '.' for pos in positions]):
                    return [(('top_row', pos), ('bottom_row', a))]
            if b[a] == a and t[a] == '.':
                positions = hallway_positions_between(('top_row', pos),
                                                      ('top_row', a))
                if all([h[pos] == '.' for pos in positions]):
                    return [(('top_row', pos), ('top_row', a))]

        # Can an amphipod in the bottom row move to its own room?
        for pos, a in bottom_occupied:
            if pos == a:
                pass
            elif t[pos] == '.':
                if b[a] == '.' and t[a] == '.':
                    positions = hallway_positions_between(('top_row', pos),
                                                          ('top_row', a))
                    if all([h[pos] == '.' for pos in positions]):
                        return [(('bottom_row', pos), ('bottom_row', a))]
                if t[a] == '.' and b[a] == a:
                    positions = hallway_positions_between(('top_row', pos),
                                                          ('top_row', a))
                    if all([h[pos] == '.' for pos in positions]):
                        return [(('bottom_row', pos), ('top_row', a))]

        # If none of the above options are available, consider all moves out
        # of rooms into hallway
        possible_moves = []

        for pos, a in top_occupied:
            for h_pos in hallway_empty:
                # Don't move out if both are in place
                if a == pos and b[a] == pos:
                    pass
                else:
                    positions = hallway_positions_between(('top_row', pos),
                                                          ('hallway', h_pos))
                    if all([h[pos] == '.' for pos in positions]):
                        possible_moves.append((('top_row', pos),
                                               ('hallway', h_pos)))

        for pos, a in bottom_occupied:
            for h_pos in hallway_empty:
                # Don't move out if both are in place
                if a == pos:
                    pass
                elif t[pos] == '.':
                    positions = hallway_positions_between(('bottom_row', pos),
                                                          ('hallway', h_pos))
                    if all([h[pos] == '.' for pos in positions]):
                        possible_moves.append((('bottom_row', pos),
                                               ('hallway', h_pos)))

        return possible_moves

    # ====================
    def finished(self):
        """Return True if all amphipods are in their finishing state"""

        if all([k == v for k, v in self.top_row.items()]) \
           and all([k == v for k, v in self.bottom_row.items()]):
            return True
        else:
            return False


# === HELPER FUNCTIONS FOR BurrowState CLASS ===

# ====================
def hallway_positions_between(start: tuple, end: tuple) -> list:
    """Get all positions in the hallway between start and end

    Return a list of hallway positions (e.g. [4,6,8])"""

    start_abs = get_abs_pos(start)
    end_abs = get_abs_pos(end)
    if start_abs < end_abs:
        positions = [pos for pos in HALLWAY_POSITIONS
                     if pos > start_abs and pos < end_abs]
    elif start_abs > end_abs:
        positions = [pos for pos in HALLWAY_POSITIONS
                     if pos < start_abs and pos > end_abs]
    return positions


# ====================
def get_abs_pos(area_and_pos: tuple):
    """Get the absolute position of a position in an area

    E.g. position 'A' in the top row has absolute position 3."""

    area, pos = area_and_pos
    if area in ['top_row', 'bottom_row']:
        abs_pos = LETTER_TO_POS[pos]
    else:
        abs_pos = pos
    return abs_pos


# ====================
def sorted_dict_to_list(dict_: dict) -> list:
    """Return dictionary values sorted by their keys"""

    return [dict_[x] for x in sorted(dict_.keys())]


# === TESTS & VISUALISATIONS ===

# ====================
def animate_steps(state: BurrowState, steps: list):

    # Print starting state
    os.system('cls')
    print(state)

    # Print each step
    for start, end in steps:
        time.sleep(1)
        os.system('cls')
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

TEST_START_STATE = BurrowState('BCBD', 'ADCA')
TEST_STEPS = [
    (('top_row', 'C'), ('hallway', 4)),
    (('top_row', 'B'), ('top_row', 'C')),
    (('bottom_row', 'B'), ('hallway', 6)),
    (('hallway', 4), ('bottom_row', 'B')),
    (('top_row', 'A'), ('top_row', 'B')),
    (('top_row', 'D'), ('hallway', 8)),
    (('bottom_row', 'D'), ('hallway', 10)),
    (('hallway', 8), ('bottom_row', 'D')),
    (('hallway', 6), ('top_row', 'D')),
    (('hallway', 10), ('top_row', 'A'))
]
TEST_EXPECTED_ENERGY = 12521


# === ACTUAL DATA ===

ACTUAL_START_STATE = BurrowState('DADC', 'CABB')


# ====================
find_best(ACTUAL_START_STATE, 20000)
