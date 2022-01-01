import ast
from helper import *
import math



def add(l1, l2):
    return [l1, l2]
# def test_add():
#     assert add([1,2], [[3,4],5] == [[1,2],[[3,4],5]])
# test_add()
# print('SUCCESS')


def split(num) -> list:
    return [math.floor(num/2), math.ceil(num/2)]

def iterate_sublists(l, depth=1, i_s=None):

    if i_s == None:
        i_s = []

    for index, e in enumerate(l):
        # Split
        if isinstance(e, int) and e >= 10:
            # print(f'Split {e}')
            e_ = my_list
            for i in i_s:
                e_ = e_[i]
            e_[index] = split(e_[index])
            # assert False

        # Explode
        if len(i_s) == 3 and isinstance(e, list):
            # print(f'Explode {e}')
            old_left = e[0]
            old_right = e[1]
            # Find next element to left
            if index == 1 and isinstance(my_list[i_s[0]][i_s[1]][i_s[2]][0], int):
                my_list[i_s[0]][i_s[1]][i_s[2]][0] += old_left
            elif index == 1 and isinstance(my_list[i_s[0]][i_s[1]][i_s[2]][0], list):
                my_list[i_s[0]][i_s[1]][i_s[2]][0][1] += old_left
            elif i_s[2] == 1 and isinstance(my_list[i_s[0]][i_s[1]][0], int):
                my_list[i_s[0]][i_s[1]][0] += old_left
            elif i_s[2] == 1 and isinstance(my_list[i_s[0]][i_s[1]][0], list):
                if isinstance(my_list[i_s[0]][i_s[1]][0][1], list):
                    my_list[i_s[0]][i_s[1]][0][1][1] += old_left
                else:
                    my_list[i_s[0]][i_s[1]][0][1] += old_left
            elif i_s[1] == 1 and isinstance(my_list[i_s[0]][0], int):
                my_list[i_s[0]][0] += old_left
            elif i_s[1] == 1 and isinstance(my_list[i_s[0]][0], list):
                if isinstance(my_list[i_s[0]][0][1], list):
                    my_list[i_s[0]][0][1][1] += old_left
                else:
                    my_list[i_s[0]][0][1] += old_left
            elif i_s[0] == 1 and isinstance(my_list[0], int):
                my_list[0] += old_left
            elif i_s[0] == 1 and isinstance(my_list[0], list):
                if isinstance(my_list[0][1], list):
                    my_list[0][1][1] += old_left
                else:
                    my_list[0][1] += old_left
                my_list[0][1] += old_left
            # Find next element to right
            if index == 0 and isinstance(my_list[i_s[0]][i_s[1]][i_s[2]][1], int):
                my_list[i_s[0]][i_s[1]][i_s[2]][1] += old_right
            elif index == 0 and isinstance(my_list[i_s[0]][i_s[1]][i_s[2]][1], list):
                my_list[i_s[0]][i_s[1]][i_s[2]][1][0] += old_right
            elif i_s[2] == 0 and isinstance(my_list[i_s[0]][i_s[1]][1], int):
                my_list[i_s[0]][i_s[1]][1] += old_right
            elif i_s[2] == 0 and isinstance(my_list[i_s[0]][i_s[1]][1], list):
                my_list[i_s[0]][i_s[1]][1][0] += old_right
            elif i_s[1] == 0 and isinstance(my_list[i_s[0]][1], int):
                my_list[i_s[0]][1] += old_right
            elif i_s[1] == 0 and isinstance(my_list[i_s[0]][1], list):
                my_list[i_s[0]][1][0] += old_right
            elif i_s[0] == 0 and isinstance(my_list[1], int):
                my_list[1] += old_right
            elif i_s[0] == 0 and isinstance(my_list[1], list):
                my_list[1][0] += old_right
            my_list[i_s[0]][i_s[1]][i_s[2]][index] = 0
            # assert False

        if isinstance(e,list):
            iterate_sublists(e, depth+1, i_s=i_s+[index])

        else:
            pass
    

def reduce(l):
    
    global my_list
    my_list = l
    iterate_sublists(my_list)

    while True:
        try:
            iterate_sublists(my_list)
            break
        except:
            print(my_list)
            # print()
            # break
            pass
        
    return my_list

lines = get_lines_from_file("data.txt")
lines = [ast.literal_eval(l) for l in lines]
x = lines[0]
for l in lines[1:]:
    x = add(x, l)
    x = reduce(x)
print(x)

print(reduce([[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[[[5, 6], 0], [6, [15, 5]]], [[0, [17, 3]], [[6, 3], [8, 8]]]]]))