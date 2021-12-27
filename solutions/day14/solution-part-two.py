from collections import Counter
import math


# ====================
def get_state(polymer_template: str, rules: dict) -> dict:
    """Generate state dict from polymer template"""

    state = {pair: 0 for pair in rules.keys()}

    for i in range(len(polymer_template)-1):
        pair = polymer_template[i:i+2]
        state[pair] += 1

    return state


# ====================
def next_step(old_state: dict, rules: dict) -> dict:
    """Return the state after one step forward"""

    new_state = {pair: 0 for pair in rules.keys()}

    for old_pair, num in old_state.items():
        new_pair_1 = old_pair[0] + rules[old_pair]
        new_pair_2 = rules[old_pair] + old_pair[1]
        new_state[new_pair_1] += num
        new_state[new_pair_2] += num

    return new_state


# ====================
def get_letter_freqs(state: dict) -> dict:
    """Get letter frequencies from state dict"""

    all_letters = list(set(''.join(state.keys())))
    letter_freqs = {letter: 0 for letter in all_letters}

    for pair, num in state.items():
        letter_freqs[pair[0]] += num
        letter_freqs[pair[1]] += num

    # Correct for overlapping letters
    for letter in letter_freqs.keys():
        letter_freqs[letter] = math.ceil(letter_freqs[letter]/2)

    return letter_freqs
        
        
# ====================
def get_answer(letter_freqs: dict) -> int:
    """What do you get if you take the quantity of the most common element and
    subtract the quantity of the least common element?"""

    freqs = letter_freqs.values()
    return max(freqs) - min(freqs)


# ====================
def solve(data_file: str, num_steps: int) -> int:
    """Solve the problem"""

    # Get data
    with open(data_file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    polymer_template = lines[0]
    rules = {}
    for i in range(2,len(lines)):
        from_, to = lines[i].split(" -> ")
        rules[from_] = to

    # Iterate through steps
    state = get_state(polymer_template, rules)
    for _ in range(num_steps):
        state = next_step(state, rules)

    # Get answer
    letter_freqs = get_letter_freqs(state)
    answer = get_answer(letter_freqs)
    
    return answer


# === MAIN PROGRAM ===

# Run tests
assert solve("test.txt", 10) == 1588
assert solve("test.txt", 40) == 2188189693529
assert solve("data.txt", 10) == 2549

# Solve for 40 steps with actual data
print(solve("data.txt", 40))