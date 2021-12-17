from helper import *
import time

# Get data
lines = get_lines_from_file("data.txt")
# lines = get_lines_from_file("data.txt")

lines = [l.split('-') for l in lines]
nodes = list(set([l for x in lines for l in x]))

# def get_paths(nodes_visited, remaining_nodes):

#     print(nodes_visited)
#     print(remaining_nodes)
#     time.sleep(1)
#     current_node = nodes_visited[-1]
#     if current_node.islower():
#         remaining_nodes = [x for x in remaining_nodes if x != current_node]
#     if current_node == 'end':
        
#     else:
#         for n in [x for x in remaining_nodes if x != current_node]:
#             if [current_node, n] in lines:
#                 nodes_visited.append(n)        
#                 remaining_nodes.extend(get_paths(nodes_visited, remaining_nodes))
#     return(nodes_visited)


# def get_paths(this_node, nodes_remaining):

#     paths_so_far = []
#     next_nodes = [x[1] for x in lines if x[0] == this_node and x[1] in nodes_remaining]
#     print(next_nodes)
#     for n in next_nodes:
#         print(n)
#         if n == 'end':
            
#         else:
#             if n.islower():
#                 nodes_remaining = [p for p in nodes_remaining if p!=n]
#             paths_so_far.extend([[n] + p for p in get_paths(n, nodes_remaining)])
#     return paths_so_far


# def get_paths(this_path):

#     all_paths = []

#     this_node = this_path[-1]
#     print(this_node)
#     print(x for x in this_path)
#     cannot_visit = [this_node] + [x for x in this_path if x.islower()]
#     next_nodes = [x[1] for x in lines if x[0] == this_node and x[1] not in cannot_visit]
    
#     for n in next_nodes:
#         print(n)
#         this_path += this_node
#         return all_paths.extend([[this_path.append(n)] for n in get_paths([this_path])])
#     else:
#         return all_paths
#     # return ([[this_node] + [n] for n in next_nodes])



paths = {0: [['start']]}
this_path = paths[0][0]
last_node = this_path[-1]

finished_paths = []
i = 1

while True:

# Step 1

    paths[i] = []

    for p in paths[i-1]:
        last_node = p[-1]
        next_nodes = [x[1] for x in lines if x[0] == last_node] + [x[0] for x in lines if x[1] == last_node]
        next_nodes = [n for n in next_nodes if n != last_node]
        # Cannot visit a lowercase node twice
        next_nodes = [n for n in next_nodes if not n == 'start']
        for next_node in next_nodes:
            if next_node == 'end':
                finished_paths.append(p + ['end'])
            else:
                path_to_be = p + [next_node]
                double_visits = [x for x in path_to_be if x.islower() and path_to_be.count(x) > 1]
                if len(double_visits) > 2:
                    pass
                else:
                    paths[i].append(p + [next_node])

    if paths[i] == []:
        break
    else:
        i += 1

print(len(finished_paths))