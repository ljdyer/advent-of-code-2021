# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# ====================
lines = get_lines_from_file("data/data.txt")

# Get data
lines = [int(line) for line in lines]

# Part 1
count = 0
for i in range(len(lines)-1):
    if lines[i] < lines[i+1]:
        count += 1
print(count)

# Part 2
count = 0
for i in range(len(lines)-2):
    if sum(lines[i:i+3]) < sum(lines[i+1:i+4]):
        count += 1
print(count)
