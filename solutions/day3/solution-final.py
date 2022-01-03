from collections import Counter


# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# Get data
file = "data/data.txt"
lines = get_lines_from_file(file)


# === Part 1 ===
pos = range(len(lines[0]))
gamma_binary = ''
epsilon_binary = ''

for p in pos:
    all_bits = [line[p] for line in lines]
    bit_counter = Counter(all_bits)
    x, _ = bit_counter.most_common()[0]   # Most common
    y, _ = bit_counter.most_common()[1]   # Least common
    gamma_binary = gamma_binary + x
    epsilon_binary = epsilon_binary + y

gamma = int(gamma_binary, 2)
epsilon = int(epsilon_binary, 2)
print(gamma * epsilon)


# === Part 2 ===

# Oxygen
next_pos = 0
num_lines = len(lines)

while num_lines > 1:
    bits = [line[next_pos] for line in lines]
    count = Counter(bits)
    x, x_count = count.most_common(2)[0]
    y, y_count = count.most_common(2)[1]
    if x_count > y_count:
        lines = [line for line in lines if line[next_pos] == x]
    else:
        lines = [line for line in lines if line[next_pos] == '1']
    num_lines = len(lines)
    next_pos += 1

oxygen_binary = lines[0]
oxygen = int(oxygen_binary, 2)


# Co2
# Reinitialise lines
lines = get_lines_from_file(file)
next_pos = 0
num_lines = len(lines)

while num_lines > 1:
    bits = [line[next_pos] for line in lines]
    count = Counter(bits)
    x, x_count = count.most_common(2)[0]
    y, y_count = count.most_common(2)[1]
    if x_count > y_count:
        lines = [line for line in lines if line[next_pos] == y]
    else:
        lines = [line for line in lines if line[next_pos] == '0']
    num_lines = len(lines)
    next_pos += 1

co2_binary = lines[0]
co2 = int(co2_binary, 2)

print(co2 * oxygen)
