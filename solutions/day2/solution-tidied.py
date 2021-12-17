from helper import *

# Get data
lines = get_lines_from_file("data.txt")

# Parse input strings
reg = r'(\w*) (\d*)'
dir_amt = [get_groups(reg, x) for x in lines]

# Part 1
h_pos = 0
depth = 0
aim = 0
for dir, amt in dir_amt:
    amt = int(amt)
    if dir == 'forward':
        h_pos += int(amt)
    if dir == 'down':
        depth += int(amt)
    if dir == 'up':
        depth -= int(amt)
print(h_pos * depth)

# Part 2
h_pos = 0
depth = 0
aim = 0
for dir, amt in dir_amt:
    amt = int(amt)
    if dir == 'forward':
        h_pos += int(amt)
        depth += int(amt) * aim
    if dir == 'down':
        aim += int(amt)
    if dir == 'up':
        aim -= int(amt)
print(h_pos * depth)
