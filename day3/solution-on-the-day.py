from helper import *

# Open test data
file = "data.txt"
lines = get_lines_from_file(file)

from collections import Counter

# # Open data
# lines = get_lines_from_file("data.txt")


# List comprehension 
# lines = [l for l in lines]

# Print first n
# print_first_n(100, lines)

# bits = range(len(lines[0]))
# gamma = ''
# epsilon = ''

# Oxygen
my_len=len(lines)
b = 0
while my_len > 1:

    first_bits = [l[b] for l in lines]
    first_count = Counter(first_bits)
    x1,x1_count = first_count.most_common(2)[0]
    x2,x2_count = first_count.most_common(2)[1]
    if x1_count > x2_count:
        lines = [l for l in lines if l[b] == x1]
    elif x2_count > x1_count:
        lines = [l for l in lines if l[b] == x2]
    else:
        lines = [l for l in lines if l[b] == '1']
    print(lines)
    my_len = len(lines)
    b+=1

the_l = lines[0]
ox = int(the_l, 2)
print(ox)

# Co2
lines2 = get_lines_from_file(file)

my_len=len(lines2)
b = 0
while my_len > 1:

    first_bits = [l[b] for l in lines2]
    first_count = Counter(first_bits)
    x1,x1_count = first_count.most_common(2)[0]
    x2,x2_count = first_count.most_common(2)[1]
    if x1_count < x2_count:
        lines2 = [l for l in lines2 if l[b] == x1]
    elif x2_count < x1_count:
        lines2 = [l for l in lines2 if l[b] == x2]
    else:
        lines2 = [l for l in lines2 if l[b] == '0']
    print(lines2)
    my_len = len(lines2)
    b+=1

print(lines2)


the_l2 = lines2[0]
co = int(the_l2, 2)
print(co)

print(ox*co)



# for b in bits:
#     y = first_count.most_common(2)[1][0]
#     gamma = gamma + x
#     epsilon = epsilon + y

# g = int(gamma, 2)
# e = int(epsilon, 2)
# print(gamma)
# print(epsilon)
# print(g)
# print(e)
# print(g*e)


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



