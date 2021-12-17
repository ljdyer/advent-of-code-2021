
from collections import Counter
import itertools

# Get data
with open("test.txt", encoding='utf-8') as file:
# with open("data.txt", encoding='utf-8') as file:
    lines = file.read().splitlines()
pt = lines[0]
rules = {}
for i in range(2,len(lines)):
    from_, to = lines[i].split(" -> ")
    rules[from_] = to
rules = {k: k[0] + v + k[1] for k,v in rules.items()}
alphabet = set(list(''.join(rules.keys())))
print(alphabet)
letter_rules = {letter: {k:v for k,v in rules.items() if k[0] == letter} for letter in alphabet}
print(letter_rules)

def next_step(p_template):
    if len(p_template) < 2:
        return p_template
    if p_template in letter_rules[p_template[0]].keys():
        return letter_rules[p_template[0]][p_template]
    else:
        mid_point = round(len(p_template)/2)
        letter = p_template[0]
        if len(p_template) < 3000:
            letter_rules[letter][p_template] = next_step(p_template[:mid_point])[:-1] + next_step(p_template[mid_point-2:][1:])
            return letter_rules[letter][p_template]
        else:
            return next_step(p_template[:mid_point])[:-1] + next_step(p_template[mid_point-2:][1:])


for l in range(3,25):
    for c in itertools.permutations(alphabet, l):
        j = ''.join(list(c))
        next_step(j)

for i in range(25):
    print(i)
    pt = next_step(pt)
    # print(pt)
# # Generate polymer template after 10 steps
# for i in range(10):
#     n = 0
#     while n < len(pt)-1:
#         this_pair = pt[n:n+2]
#         if this_pair in rules.keys():
#             pt = pt[:n+1] + \
#                 rules[this_pair] + pt[n+1:]
#             n += 2
#         else:
#             n += 1

# What do you get if you take the quantity of the most common element and
# subtract the quantity of the least common element?
common = Counter(pt).most_common()
print(common)
print(common[0][1] - common[-1][1])


