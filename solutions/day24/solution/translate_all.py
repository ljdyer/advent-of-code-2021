import re


# ====================
def translate_alu(source_file: str, target_file: str):

    with open(source_file, encoding='utf-8') as file:
        alu = file.read()

    regexes_and_subs = [
        (r'div (\w) 1\n', r''),                     # Divide by 1
        (r'mul (\w) (0)', r'\1 = 0'),               # Multiply by zero
        (r'add (\w) -(\S+)', r'\1 = \1 - \2'),      # Add a negative number
        (r'inp (\w)', r'\1 = int(input_.pop(0))'),  # inp
        (r'add (\w) (\S+)', r'\1 = \1 + \2'),       # add
        (r'mul (\w) (\S+)', r'\1 = \1 * \2'),       # mul
        (r'div (\w) (\S+)', r'\1 = \1 // \2'),      # div
        (r'mod (\w) (\S+)', r'\1 = \1 % \2'),       # mod
        (r'eql (\w) (\S+)', r'\1 = int(\1==\2)'),   # eql
        (r'(\S) = 0\n\1 = \1 \+ (\S+)', r'\1 = \2'),# set to zero then add
                                                    # something
        (r'(\S) = (\S+)\n\1 = \1 ([\*\+\-%]) (\S+)', r'\1 = \2 \3 \4'),
                                                    # set to value then do
                                                    # another operation
        (r'(\S) = (\S+) ([\*%]) (\S+)\n\1 = \1 \+ (\S+)', r'\1 = \2 \3 \4 + \5'),
                                                    # multiply or divide then
                                                    # add
        (r'(\S) = (\S+) \+ (\S+)\n\1 = \1 \* (\S+)', r'\1 = (\2 + \3) * \4'),
                                                    # add then multiply
        (r'x = int\(x==w\)\nx = int\(x==0\)', r'x = int(x!=w)')
                                                    # literal string match
    ]

    for regex, sub in regexes_and_subs:
        alu = re.sub(regex, sub, alu)

    with open(target_file, "w", encoding='utf-8', ) as file:
        file.write(alu)


translate_alu('tests/test1.txt', 'tests/test1_translated.txt')
translate_alu('tests/test2.txt', 'tests/test2_translated.txt')
translate_alu('tests/test3.txt', 'tests/test3_translated.txt')
translate_alu('data.txt', 'data_translated.txt')
