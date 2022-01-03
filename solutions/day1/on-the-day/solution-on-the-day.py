from helper import *

# Open test data
# lines = get_lines_from_file("test.txt")

# # Open data
lines = get_lines_from_file("data.txt")

# # Write to new file
# write_lines_to_file("new.txt", lines)


# List comprehension 
lines = [int(l) for l in lines]




count = 0
for i in range(len(lines)-2):
    print(sum(lines[i:i+3])), sum(lines[i+1:i+4])
    if sum(lines[i:i+3]) < sum(lines[i+1:i+4]):

        count+=1

print(count)



# # Print last n
# print_last_n(100, lines)


# === REGEX ===

# # Get instances of 'foo', 'bar' from string
# alpha = "foo|bar"
# subs = get_substrings(alpha, my_str)

# Parse string into parts
# reg = r'(.*)-(.*) (.*): (.*)'
# parts = get_groups(reg, my_str)



