from helper import *

# Open test data
lines = get_lines_from_file("test.txt")

# # Open data
# lines = get_lines_from_file("data.txt")

# # Write to new file
# write_lines_to_file("new.txt", lines)


# List comprehension 
lines = [l for l in lines]

x = 0
y = 0
aim = 0

reg = r'(\w*) (\d*)'
dir_amt = [get_groups(reg, x) for x in lines]

for dir, amt in dir_amt:
    if dir == 'forward':
        x += int(amt)
        y += int(amt) * aim
    if dir == 'down':
        aim += int(amt)
        # y += int(amt)
    if dir == 'up':
        aim -= int(amt)
        # y -= int(amt)

print(x, y)
print(x*y)


# Print first n
# print_first_n(100, dir_amt)

# # Print last n
# print_last_n(100, lines)







# === REGEX ===

# # Get instances of 'foo', 'bar' from string
# alpha = "foo|bar"
# subs = get_substrings(alpha, my_str)

# Parse string into parts
# reg = r'(.*)-(.*) (.*): (.*)'
# parts = get_groups(reg, my_str)



