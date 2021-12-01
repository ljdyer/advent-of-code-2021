from helper import *

lines = get_lines_from_file("data.txt")

# Get data
lines = [int(l) for l in lines]

# Part 1
count = 0
for i in range(len(lines)-1):
    if lines[i] < lines[i+1]:
        count+=1
print(count)

# Part 2
count = 0
for i in range(len(lines)-2):
    if sum(lines[i:i+3]) < sum(lines[i+1:i+4]):
        count+=1
print(count)