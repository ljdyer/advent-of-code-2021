from helper import *
from collections import Counter

# Get data
file = "data.txt"
lines = get_lines_from_file(file)

# === Part 1 ===
pos = range(len(lines[0]))
gamma = ''
epsilon = ''

for p in pos:
    all_bits = [l[p] for l in lines]
    bit_counter = Counter(all_bits)
    x, _ = bit_counter.most_common()[0]   # Most common
    y, _ = bit_counter.most_common()[1]   # Least common
    gamma = gamma + x
    epsilon = epsilon + y

g = int(gamma, 2)
e = int(epsilon, 2)
print(g)
print(e)
print(g*e)
print()

# === Part 2 ===

# Oxygen

next_pos = 0
num_lines = len(lines)

while num_lines > 1:
    bits = [l[next_pos] for l in lines]
    count = Counter(bits)
    x, x_count = count.most_common(2)[0]
    y, y_count = count.most_common(2)[1]
    if x_count > y_count:
        lines = [l for l in lines if l[next_pos] == x]
    else:
        lines = [l for l in lines if l[next_pos] == '1']
    num_lines = len(lines)
    next_pos += 1

oxygen = lines[0]
o = int(oxygen, 2)
print(o)

# # Co2

lines = get_lines_from_file(file)
next_pos = 0
num_lines = len(lines)

while num_lines > 1:
    bits = [l[next_pos] for l in lines]
    count = Counter(bits)
    x, x_count = count.most_common(2)[0]
    y, y_count = count.most_common(2)[1]
    if x_count > y_count:
        lines = [l for l in lines if l[next_pos] == y]
    else:
        lines = [l for l in lines if l[next_pos] == '0']
    num_lines = len(lines)
    next_pos += 1

co2 = lines[0]
c = int(co2, 2)
print(c)

print(c*o)
