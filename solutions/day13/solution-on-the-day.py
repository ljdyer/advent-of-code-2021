from tabulate import tabulate

with open("data.txt", encoding='utf-8') as file:
    lines = file.read().splitlines()

lines = [l.split('-') for l in lines]
blank_line = lines.index([''])
dots = lines[:blank_line]

dots = [l[0].split(',') for l in dots]
for i in range(len(dots)):
    dots[i] = tuple((int(dots[i][0]), int(dots[i][1])))

instructions = lines [blank_line+1:]

m_max = max([int(x[0]) for x in dots])
n_max = max([int(x[1]) for x in dots])
# My method needs odd numbers of rows and columns to work
if m_max % 2 == 0:
    m_max = m_max + 1
else:
    m_max = m_max + 2
if n_max % 2 == 0:
    n_max = n_max + 1
else:
    n_max = n_max + 2

matrix = [['.' for m in range(m_max)] for n in range(n_max)]
print(len(matrix))
print(len(matrix[0]))

for x,y in dots:
    matrix[y][x] = '#'


def fold_y(y_fold, matrix):
    
    lines_above_fold = matrix[:y_fold]
    lines_below_fold = matrix[len(matrix):y_fold:-1]
    lines_without = [i for i in range(len(matrix)) if not '#' in matrix[i]]
    print("Y", len(lines_above_fold), len(lines_below_fold))
    for i in range(len(lines_below_fold)):
        for y in range(len(lines_above_fold[i])):
            if lines_below_fold[i][y] == '#':
                lines_above_fold[i][y] = '#'
    return lines_above_fold

def fold_x(x_fold, matrix):

    lines_left_fold = [l[:x_fold] for l in matrix]
    lines_right_fold = [l[len(l):x_fold:-1] for l in matrix]
    fold_column = [l[x_fold] for l in matrix]
    print("X", len(lines_left_fold[0]), len(lines_right_fold[0]))
    if '#' in fold_column:
        print(x_fold, 'warning')
    for row in range(len(lines_right_fold)):
        for column in range(len(lines_left_fold[row])):
            if lines_right_fold[row][column] == '#':
                lines_left_fold[row][column] = '#'
    return lines_left_fold

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                print("X", end='')
            else:
                print(" ", end = '')
        print()

# y_fold = int(instructions[0][0].partition('=')[2])
# matrix = fold_y(y_fold, matrix)
matrix = fold_x(655,matrix)
matrix = fold_y(447,matrix)
matrix = fold_x(327,matrix)
matrix = fold_y(223,matrix)
matrix = fold_x(163,matrix)
matrix = fold_y(111,matrix)
matrix = fold_x(81,matrix)
matrix = fold_y(55,matrix)
matrix = fold_x(40,matrix)
matrix = fold_y(27,matrix)
matrix = fold_y(13,matrix)
matrix = fold_y(6,matrix)
print_matrix(matrix)


# print(tabulate(matrix))

all = [i for x in matrix for i in x if i == '#']
print(len(all))
# print(tabulate(lines_below_fold))

# # x_fold = int(instructions[1][0].partition('=')[2])
# print(y_fold)

# num_put = 0
# y_bottom = n_max
# # for x in range(y_bottom, y_fold,-1):
# #     # print(x)
# #     for y in range(len(matrix[x])):
# #         # print(y)
# #         if matrix[x][y] == '#':
# #             new_x = y_fold - (x - y_fold)
# #             print(x,y,new_x,y)
# #             num_put += 1
# #             if matrix[new_x][y] == '#':
# #                 print('overlapping')


# # new_x = 7 - (14 - 14)

# # # x_bottom = x_fold*2 + 1
# # # for y in range(x_bottom, x_fold,-1):
# # #     print(y)
# # #     for x in range(len(matrix)):
# # #         if matrix[x][y] == '#':
# # #             new_y = x_bottom - y - 1
# # #             print(x,y,new_x,y)
# # #             matrix[x][new_y] = '#'

# # # # 15 -> 1
# # # # 14 -> 2
# # # # 13 -> 3

    
# # print(tabulate(matrix[0:2]))
# visible_lines = [matrix[m] for m in range(y_fold)]
# invisible_lines = [matrix[m] for m in range(y_fold,y_bottom)]
# all = [i for x in visible_lines for i in x if i == '#']
# print(len(all))
# all = [i for x in invisible_lines for i in x if i == '#']
# print(len(all))
