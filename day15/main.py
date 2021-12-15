from helper import *
from os import path
from itertools import permutations

with open("big.txt", encoding='utf-8') as file:
# with open("test.txt", encoding='utf-8') as file:
    lines = file.read().splitlines()

matrix = [[int(x) for x in l] for l in lines]

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
def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(str(num).rjust(3),end='')
        print()

# matrix = make_big_matrix(matrix)
# print_matrix(matrix)
matrix_height = len(matrix)
matrix_width = len(matrix[0])
print(matrix_height)
print(matrix_width)

nodes = []
for i in range(0, matrix_height):
    for j in range(0, matrix_width):
        nodes.append((i,j))

dist = {n:"I" for n in nodes}
prev = {n:'' for n in nodes}
dist[(0,0)] = 0

# 11      while Q is not empty:
# 12          u ← vertex in Q with min dist[u]   
# 13                                             
# 14          remove u from Q
# 15         
# 16          for each neighbor v of u still in Q:
# 17              alt ← dist[u] + length(u, v)
# 18              if alt < dist[v]:              
# 19                  dist[v] ← alt
# 20                  prev[v] ← u
# 21
# 22      return dist[], prev[]

# while nodes:
while nodes:
    _, u = min([(dist[node], node) for node in nodes if isinstance(dist[node],int)])

    nodes = [n for n in nodes if n != u]
    print(len(nodes))

    i,j = u

    for x,y in [(i-1,j), (i,j-1), (i+1, j), (i,j+1)]:
        if (x,y) in nodes:
            alt = dist[u] + matrix[x][y]
            if isinstance(dist[(x,y)], str) or alt < dist[(x,y)]:
                dist[(x,y)] = alt
                prev[(x,y)] = u

print(dist[(matrix_height-1,matrix_width-1)])


