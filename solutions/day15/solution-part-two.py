from timebudget import timebudget
from helper import *
import heapq as hq

# ====================
def get_matrix(filename):
    """Get matrix from file"""

    with open(filename, encoding='utf-8') as file:
        lines = file.read().splitlines()
    matrix = [[int(x) for x in l] for l in lines]
    return matrix


# ====================
def make_big_matrix(matrix):

    def increase(num):
        if num == 9:
            return 1
        else:
            return num+1

    def add_one(matrix):
        new_matrix = [[increase(x) for x in l] for l in matrix]
        return new_matrix

    def append_right(matrix1, matrix2):
        new_matrix = [matrix1[i] + matrix2[i] for i in range(len(matrix1))]
        return new_matrix

    def append_below(matrix1, matrix2):
        return matrix1 + matrix2

    append_matrix = matrix
    for _ in range(4):
        append_matrix = add_one(append_matrix)
        matrix = append_right(matrix, append_matrix)
    append_matrix = matrix
    for _ in range(4):
        append_matrix = add_one(append_matrix)
        matrix = append_below(matrix, append_matrix)

    return matrix


# ====================
def djikstra(matrix):
    """Implementation of Djikstra's algorithm based on
    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
    
    Use priority queue"""

    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    nodes = [(x, y) for x in range(matrix_height) for y in range(matrix_width)]
    # Use an arbitrarily large number for infinity
    dist = {n:1000000 for n in nodes}
    dist[(0,0)] = 0
    prev = {n:'' for n in nodes}
    # Initiate heap
    h = []
    hq.heappush(h, (0, (0,0)))

    while True:
        # Remove and return best vertex
        _, u = hq.heappop(h)
        i,j = u
        if u == (matrix_height - 1, matrix_width - 1):
            return dist[u]
        for x,y in [(i-1,j), (i,j-1), (i+1, j), (i,j+1)]:
            if x > -1 and y > -1 and x < matrix_height and y < matrix_width:
                alt = dist[u] + matrix[x][y]           
                if alt < dist[(x,y)]:
                    dist[(x,y)] = alt
                    prev[(x,y)] = u
                    hq.heappush(h, (alt, (x,y)))


# === MAIN PROGRAM ===

# Run tests
matrix = get_matrix("test.txt")
test_result = djikstra(matrix)
assert test_result == 40
matrix = get_matrix("data.txt")
with timebudget('Part One'):
    test_result = djikstra(matrix)
assert test_result == 390
print("Tests passed.")
print()

# Run on actual data
matrix = get_matrix("data.txt")
big_matrix = make_big_matrix(matrix)
with timebudget('Part Two'):
    answer = djikstra(big_matrix)
print(answer)

