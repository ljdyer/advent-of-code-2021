from collections import Counter

# Get data
with open("data.txt", encoding='utf-8') as file:
    lines = file.read().splitlines()
polymer_template = lines[0]
rules = {}
for i in range(2,len(lines)):
    from_, to = lines[i].split(" -> ")
    rules[from_] = to

# Generate polymer template after 10 steps
for i in range(10):
    n = 0
    while n < len(polymer_template)-1:
        this_pair = polymer_template[n:n+2]
        if this_pair in rules.keys():
            polymer_template = polymer_template[:n+1] + \
                rules[this_pair] + polymer_template[n+1:]
            n += 2
        else:
            n += 1

# What do you get if you take the quantity of the most common element and
# subtract the quantity of the least common element?
common = Counter(polymer_template).most_common()
print(common[0][1] - common[-1][1])



