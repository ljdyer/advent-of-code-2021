import nltk
import re

# ====================
def get_lines_from_file(file: str) -> list:
    """Get the lines from a text file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


# ====================
def write_lines_to_file(file: str, lines: list): 
    """Save list of lines to a text file"""

    with open(file, "w", encoding='utf-8', ) as file:
        file.write("\n".join(lines))


# ====================
def print_first_n(n: int, lines: list):
    if n < len(lines):
        for_range = n
    else:
        for_range = len(lines)
    for i in range(for_range):
        print(lines[i])


# ====================
def print_last_n(n: int, lines: list):
    if n < len(lines):
        for_range = n
    else:
        for_range = len(lines)
    for i in range(len(lines)-for_range, len(lines)):
        print(lines[i])


# ====================
def get_groups(regex, text) -> tuple:

    return re.findall(regex, text)[0]


# ====================
def get_substrings(alphabet, text) -> list:
    """Alphabet is string of substrings separated by |"""

    return(nltk.regexp_tokenize(text, alphabet))
