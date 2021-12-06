from helper import *
from collections import Counter

# Get data
lines = get_lines_from_file("data.txt")
# lines = get_lines_from_file("data.txt")

# lines = [l for l in lines]
# print_first_n(100, lines)
# print_last_n(100, lines)
# write_lines_to_file("new.txt", lines)

input_ = [int(x) for x in lines[0].split(",")]

fishes = input_
fishes = Counter(fishes)

def countdown(fishes):
    new_fishes = {}
    for i in range(8,-1,-1):
        if i+1 in fishes.keys():
            new_fishes[i] = fishes[i+1]
        else:
            new_fishes[i] = 0
    # new_fishes[0] = fishes[1]
    new_fishes[8] = fishes[0]
    new_fishes[6] += fishes[0]
    # print(new_fishes)
    return new_fishes
    
def total_fishes(fishes):
    num_fish = sum([v for k, v in fishes.items()])
    return num_fish

# def countdown(f) -> bool:
#     f=f-1
#     if f == -1:
#         return (6, True)
#     else:
#         return (f, False)

for day in range(256):
    fishes = countdown(fishes)
    # print(fishes)
#     fishes = [countdown(f) for f in fishes]
#     days = [x1 for x1,_ in fishes]
#     new_fish = [x2 for _,x2 in fishes]
#     for f in new_fish:
#         if f == True:
#             days.append(8)
#     fishes = days
#     # print(f'Day {day}: {fishes}')
#     print(len(fishes))

print(total_fishes(fishes))




# # === REGEX ===
# # # Get instances of 'foo', 'bar' from string
# # alpha = "foo|bar"
# # subs = get_substrings(alpha, my_str)

# # Parse string into parts
# # reg = r'(.*)-(.*) (.*): (.*)'
# # parts = get_groups(reg, my_str)



