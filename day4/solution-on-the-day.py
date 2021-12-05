from helper import *

# Open test data
lines = get_lines_from_file("data.txt")

# # Open data
# lines = get_lines_from_file("data.txt")


# List comprehension 
# lines = [l for l in lines]

# Print first n

order = lines[0]
boards = []
for i in range(2,len(lines),6):
    boards.append([x for l in lines[i:i+5] for x in l.split(" ") if x])

print(boards)

order = order.split(",")
for o in order:
    this_num = int(o)


def check_board(list, nums):
    for z in range(5):
        for x in list[z:len(list):5]:
            if not x in nums:
                break
        else:
            return True
    for p in range(5):
        for x in list[0+5*p:5+5*p]:
            if not x in nums:
                break
        else:
            return True

# nums = []
# for num in order:
#     nums.append(num)
#     for b in boards:
#         if check_board(b, nums):
            
#             remain_nums = [int(x) for x in b if x not in nums]
#             print(sum(remain_nums) * int(nums[-1]))
#             print(f"Winning nums: {nums}")
#             exit(-1)

nums = []
for num in order:
    nums.append(num)
    for b in boards:
        if check_board(b, nums):
            if len(boards) == 1:
                last_board = boards[0]
                remain_nums = [int(x) for x in last_board if x not in nums]
                print(sum(remain_nums) * int(nums[-1]))
                print(sum(remain_nums))
                print(nums[-1])
                exit(-1)
            else:
                boards.pop(boards.index(b))
                continue



# # # Write to new file
# # write_lines_to_file("new.txt", lines)

# # # Print last n
# # print_last_n(100, lines)

# # === REGEX ===

# # # Get instances of 'foo', 'bar' from string
# # alpha = "foo|bar"
# # subs = get_substrings(alpha, my_str)

# # Parse string into parts
# # reg = r'(.*)-(.*) (.*): (.*)'
# # parts = get_groups(reg, my_str)



