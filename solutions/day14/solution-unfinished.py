# Started 7:40
# Break 8:09
# Started 20:41

from collections import Counter

with open("test.txt", encoding='utf-8') as file:
    lines = file.read().splitlines()
polymer_template = lines[0]
rules = {}
for i in range(2,len(lines)):
    from_, to = lines[i].split(" -> ")
    rules[from_] = to

# === Method 1 ===

print(polymer_template)
for i in range(4):
    n = 0
    while n < len(polymer_template)-1:
        this_pair = polymer_template[n:n+2]
        if this_pair in rules.keys():
            polymer_template = polymer_template[:n+1] + rules[this_pair] + polymer_template[n+1:]
            n += 2
        else:
            n += 1
    # print(polymer_template)
    # print(polymer_template)
    # polymer_template = polymer_template.replace('CC','C')
    # polymer_template = polymer_template.replace('CN','N')
    # print(polymer_template)
    # print(polymer_template)
    print(len(polymer_template))
    print(Counter(polymer_template))


# # set_poly = set(polymer_template)
# # counts = {l: polymer_template.count(l) for l in set_poly}
# # print(counts)
# print()

# # === Method 2 ===

# # polymer_template = lines[0]
# # print(polymer_template)

# # pairs = [polymer_template[n:n+2] for n in range(len(polymer_template)-1)]

# # for i in range(4):
# #     new_pairs = []
# #     for pair in pairs:
# #         new_pairs.append(pair[0] + rules[pair])
# #         new_pairs.append(rules[pair] + pair[1])
# #     pairs = new_pairs
# #     print(pairs)
# #         # triples.append(pair[0] + rules[pair] + pair[1])
# #     # polymer_template = triples[0] + ''.join([t[1:] for t in triples[1:]])
# #     # print(polymer_template)
# #     polymer_template = pairs[0] + ''.join(p[1] for p in pairs[1:])
# #     print(Counter(polymer_template))
# # print(len(pairs))


# # === Method 3 ===

# polymer_template = lines[0]
# print(polymer_template)

# pairs = Counter([polymer_template[n:n+2] for n in range(len(polymer_template)-1)])
# print(pairs)

# for i in range(4):
#     new_pairs = Counter([])
#     for pair, count in pairs.items():
#         new_pair_1 = pair[0] + rules[pair]
#         new_pair_2 = pair[1] + rules[pair]
#         new_pairs.update([new_pair_1, new_pair_2])
#     pairs = new_pairs
#     print(pairs)
#     my_dic = {'N': 0, 'C': 0, 'B': 0, 'H': 0}
#     for pair, count in pairs.items():
#         try: 
#             my_dic[pair[1]] += count
#         except:
#             print(pair)
#     print(my_dic)