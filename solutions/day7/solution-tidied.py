# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


lines = get_lines_from_file("data.txt")

start_positions = [int(x) for x in lines[0].split(",")]
max_pos = max(start_positions)

# Generate dictionary of amounts of fuel burned for each distance
# Reduces running time of program compared to 'on the day' solution
amts_burned = {}
amts_burned[0] = 0
for i in range(1,2000):
    amts_burned[i] = amts_burned[i-1] + i
    

# === Part 1 ===
fuel_amts = []
for align_pos in range(max_pos):
    fuel_amt = sum([abs(start_pos - align_pos)
                    for start_pos in start_positions])
    fuel_amts.append(fuel_amt)

print(min(fuel_amts))


# === Part 2 ===
fuel_amts = []
for align_pos in range(max_pos):
    fuel_amt = sum([amts_burned[abs(start_pos - align_pos)]
                    for start_pos in start_positions])
    fuel_amts.append(fuel_amt)
    
print(min(fuel_amts))
