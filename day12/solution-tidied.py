from helper import *
import time

# Get data
lines = get_lines_from_file("data.txt")
lines = [l.split('-') for l in lines]

paths = {0: [['start']]}
finished_paths = []
i = 1

# === Part 1 ===

while True:
    paths[i] = []
    for p in paths[i-1]:
        last_node = p[-1]
        next_nodes = [x[1] for x in lines if x[0] == last_node] + \
                     [x[0] for x in lines if x[1] == last_node]
        # Don't visit lowercase nodes twice
        next_nodes = [n for n in next_nodes if not (n.islower() and n in p)]
        
        for next_node in next_nodes:
            if next_node == 'end':
                finished_paths.append(p + ['end'])
            else:
                paths[i].append(p + [next_node])

    # If there are no more unfinished paths, exit
    if paths[i] == []:
        break
    # Otherwise, go to next step
    else:
        i += 1

print(len(finished_paths))

# === Part 2 ===

paths = {0: [['start']]}
finished_paths = []
i = 1

while True:
    paths[i] = []
    for p in paths[i-1]:
        last_node = p[-1]
        next_nodes = [x[1] for x in lines if x[0] == last_node] + \
                     [x[0] for x in lines if x[1] == last_node]
        # Don't go back to start
        next_nodes = [n for n in next_nodes if not n == 'start']

        for next_node in next_nodes:
            if next_node == 'end':
                finished_paths.append(p + ['end'])
            else:
                path_to_be = p + [next_node]
                # Can only visit 'start' and one other lowercase node twice
                double_visits = [x for x in path_to_be if x.islower() and path_to_be.count(x) > 1]
                if len(double_visits) <= 2:
                    paths[i].append(p + [next_node])

    # If there are no more unfinished paths, exit
    if paths[i] == []:
        break
    # Otherwise, go to next step
    else:
        i += 1

print(len(finished_paths))