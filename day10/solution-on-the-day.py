from helper import *

# Get data
lines = get_lines_from_file("data.txt")

# lines = [l for l in lines]
print_first_n(100, lines)




# {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
# [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
# [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
open_to_close = {"{": "}", "[": "]", "(": ")", "<": ">"}
close_to_open = {v:k for k,v in open_to_close.items()}
point_mapping = {"}": 1197, "]": 57, ")": 3, ">": 25137}

def get_points(completion):
    score = 0
    for c in completion:
        score *= 5
        if c == ")":
            score += 1
        elif c == "}":
            score += 3
        elif c == "]":
            score += 2
        elif c == ">":
            score += 4
    return score



def check_line(l):
    points = 0
    open = ""
    for i in range(len(l)):
        if l[i] in list('{<[('):
            open += l[i]
        if l[i] in list(']}>)'):
            if open[-1] != close_to_open[l[i]]:
                print(f'Error in line {l}: {open}{l[i]}')
                points += point_mapping[l[i]]
                return points
            else:
                open = open[:-1]
    return 0


def complete_line(l):
    points = 0
    open = ""
    for i in range(len(l)):
        if l[i] in list('{<[('):
            open += l[i]
        if l[i] in list(']}>)'):
            if open[-1] != close_to_open[l[i]]:
                assert(False)
            else:
                open = open[:-1]
    open = ''.join([open_to_close[x] for x in open])
    return open
    close = open[::-1]
    return close
    return close


# all_points = sum([check_line(l) for l in lines])
# print(all_points)

incomplete_lines = [l for l in lines if check_line(l) == 0]

x = [get_points(complete_line(l)[::-1]) for l in incomplete_lines]
x = sorted(x)
print(x)
midpoint = round(len(x)/2)
print(x[midpoint])