from helper import *
from collections import Counter

# Get data
lines = get_lines_from_file("data.txt")
start_fishes = [int(x) for x in lines[0].split(",")]


# ====================
def countdown(fishes):

    new_fishes = {}

    # Count all fish down by one
    for i in range(8,-1,-1):
        if i+1 in fishes.keys():
            new_fishes[i] = fishes[i+1]
        else:
            new_fishes[i] = 0
    # Add new fish for every fish that has reached 0
    new_fishes[8] = fishes[0]
    # Reset fish that generated a new fish to 6
    new_fishes[6] += fishes[0]

    return new_fishes
    

# ====================
def total_fishes(fishes):
    num_fish = sum(fishes.values())
    return num_fish


# === Part 1 ===
fishes = Counter(start_fishes)
for day in range(80):
    fishes = countdown(fishes)
print(total_fishes(fishes))


# === Part 2 ===
fishes = Counter(start_fishes)
for day in range(256):
    fishes = countdown(fishes)
print(total_fishes(fishes))




