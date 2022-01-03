from helper import *

# Get data
lines = get_lines_from_file("data.txt")

OPEN_TO_CLOSE = {"{": "}", "[": "]", "(": ")", "<": ">"}
CLOSE_TO_OPEN = {v:k for k,v in OPEN_TO_CLOSE.items()}

POINTS_CORRUPTED = {"}": 1197, "]": 57, ")": 3, ">": 25137}
POINTS_INCOMPLETE = {"}": 3, "]": 2, ")": 1, ">": 4}


# ====================
def corrupted_points(l: str, verbose=False) -> int:
    open = ""
    for i in range(len(l)):
        # If opening symbol, append to open string
        if l[i] in list('{<[('):
            open += l[i]
        if l[i] in list(']}>)'):
            # Invalid closing symbol
            if open[-1] != CLOSE_TO_OPEN[l[i]]:
                if verbose:
                    print(f'Error in line {l}: {open[-1]}{l[i]}')
                return POINTS_CORRUPTED[l[i]]
            # Valid closing symbol. Remove last entry from open string
            else:
                open = open[:-1]
    else:
        # Line is not corrupted
        return 0


# ====================
def get_completion_points(completion: str) -> int:
    score = 0
    for c in completion:
        score *= 5
        score += POINTS_INCOMPLETE[c]
    return score


# ====================
def incomplete_points(l):
    open = ""
    for i in range(len(l)):
        if l[i] in list('{<[('):
            open += l[i]
        if l[i] in list(']}>)'):
            # Line should not be corrupted
            # Raise an error if it is
            if open[-1] != CLOSE_TO_OPEN[l[i]]:
                assert(False)
            else:
                open = open[:-1]
    # Reverse and map to closing symbols
    close = ''.join([OPEN_TO_CLOSE[x] for x in open[::-1]])
    return get_completion_points(close)


# === Part 1 ===

all_corrupted_points = [corrupted_points(l) for l in lines]
print(sum(all_corrupted_points))

# === Part 2 ===

incomplete_lines = [l for l in lines if corrupted_points(l) == 0]
all_incomplete_points = sorted([incomplete_points(l) for l in incomplete_lines])
midpoint = round(len(all_incomplete_points)/2)
print(all_incomplete_points[midpoint])
