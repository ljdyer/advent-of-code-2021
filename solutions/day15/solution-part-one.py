from helper import *

# ====================
def get_matrix(filename):
    """Get matrix from file"""

    with open(filename, encoding='utf-8') as file:
        lines = file.read().splitlines()
    matrix = [[int(x) for x in l] for l in lines]
    return matrix


# ====================
def djikstra(matrix):
    """Implementation of Djikstra's algorithm based on
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode"""

    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    # create vertex set Q
    nodes = []
    for i in range(0, matrix_height):
        for j in range(0, matrix_width):
            nodes.append((i,j))
    # for each vertex v in Graph:            
        # dist[v] ← INFINITY                 
        # prev[v] ← UNDEFINED
    # add v to Q
    dist = {n:"I" for n in nodes}
    prev = {n:'' for n in nodes}
    # dist[source] ← 0
    dist[(0,0)] = 0

    # while Q is not empty:
    while nodes:
        # u ← vertex in Q with min dist[u]   
        _, u = min([(dist[node], node) for node in nodes
                if isinstance(dist[node],int)])
        # remove u from Q
        nodes = [n for n in nodes if n != u]
        # for each neighbor v of u still in Q:
        i,j = u
        # If we are only interested in a shortest path between vertices
        # source and target, we can terminate the search after line 15 if
        # u = target
        if u == (matrix_height - 1, matrix_width - 1):
            return dist[u]
        for x,y in [(i-1,j), (i,j-1), (i+1, j), (i,j+1)]:
            if (x,y) in nodes:
                # alt ← dist[u] + length(u, v)
                alt = dist[u] + matrix[x][y]
            # if alt < dist[v]:              
                if isinstance(dist[(x,y)], str) or alt < dist[(x,y)]:
                    # dist[v] ← alt
                    dist[(x,y)] = alt
                    # prev[v] ← u
                    prev[(x,y)] = u


# === MAIN PROGRAM ===

# Run test
matrix = get_matrix("test.txt")
test_result = djikstra(matrix)
assert test_result == 40
print("Test passed.")
print()

# Run on actual data
matrix = get_matrix("data.txt")
print(djikstra(matrix))

