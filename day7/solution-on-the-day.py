# Part 1: 00:07:40
# Part 2: 00:12:58

# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


lines = get_lines_from_file("data.txt")

poss = [int(x) for x in lines[0].split(",")]

def amt_burned(start_pos, end_pos):
    distance = abs(start_pos-end_pos)
    this_step = 1
    total = 0
    for i in range(distance):
        total += this_step
        this_step += 1
    return total

max_x = max(poss)
fuel_amts = []
for i in range(max_x):
    fuel_amt = sum([amt_burned(x,i) for x in poss])
    fuel_amts.append((fuel_amt,i))
    # print(fuel_amt, i)
    
fuel_amts = sorted(fuel_amts)
print(fuel_amts[:1])
# print(best)
