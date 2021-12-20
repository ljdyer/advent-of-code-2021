        if len(i_s) == 3 and isinstance(e, list):
            print(f'Explode {e}')
            if index == 0:
                new_right = my_list[i_s[0]][i_s[1]][i_s[2]][0][1] + my_list[i_s[0]][i_s[1]][i_s[2]][1]
                old_left = my_list[i_s[0]][i_s[1]][i_s[2]][0][0]
                new_left = 0
                my_list[i_s[0]][i_s[1]][i_s[2]] = [new_left, new_right]
                # Find next element to left
                if i_s[2] == 1 and isinstance(my_list[i_s[0]][i_s[1]][0], int):
                    my_list[i_s[0]][i_s[1]][0] += old_left
                if i_s[2] == 1 and isinstance(my_list[i_s[0]][i_s[1]][0], list):
                    my_list[i_s[0]][i_s[1]][0][1] += old_left
                elif i_s[1] == 1 and isinstance(my_list[i_s[0]][0], int):
                    my_list[i_s[0]][0] += old_left
                elif i_s[1] == 1 and isinstance(my_list[i_s[0]][0], list):
                    my_list[i_s[0]][0][1] += old_left
                elif i_s[0] == 1 and isinstance(my_list[0], int):
                    my_list[0] += old_left
                elif i_s[0] == 1 and isinstance(my_list[0], list):
                    my_list[0][1] += old_left
                assert False
            if index == 1:
                new_left = my_list[i_s[0]][i_s[1]][i_s[2]][1][0] + my_list[i_s[0]][i_s[1]][i_s[2]][0]
                old_right = my_list[i_s[0]][i_s[1]][i_s[2]][1][1]
                new_right = 0
                my_list[i_s[0]][i_s[1]][i_s[2]] = [new_left, new_right]
                # Find next element to right
                if i_s[2] == 0 and isinstance(my_list[i_s[0]][i_s[1]][1], int):
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
            print(my_list)
            assert False