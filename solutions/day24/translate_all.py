import re

def translate_alu(source_file: str, target_file: str):

    with open(source_file, encoding='utf-8') as file:
        alu = file.read()

    re_inp = r'inp (\w)'
    sub_inp = r'\1 = int(input_.pop(0))'
    re_add = r'add (\w) (\S+)'
    sub_add = r'\1 = \1 + \2'
    re_mul = r'mul (\w) (\S+)'
    sub_mul = r'\1 = \1 * \2'
    re_div = r'div (\w) (\S+)'
    sub_div = r'\1 = math.floor(\1 / \2)'
    re_mod = r'mod (\w) (\S+)'
    sub_mod = r'\1 = \1 % \2'
    re_eql = r'eql (\w) (\S+)'
    sub_eql = r'\1 = int(\1==\2)'

    alu = re.sub(re_inp, sub_inp, alu)
    alu = re.sub(re_add, sub_add, alu)
    alu = re.sub(re_mul, sub_mul, alu)
    alu = re.sub(re_div, sub_div, alu)
    alu = re.sub(re_mod, sub_mod, alu)
    alu = re.sub(re_eql, sub_eql, alu)

    with open(target_file, "w", encoding='utf-8', ) as file:
        file.write(alu)


translate_alu('test1.txt', 'test1_translated.txt')
translate_alu('test2.txt', 'test2_translated.txt')
translate_alu('test3.txt', 'test3_translated.txt')
translate_alu('data.txt', 'data_translated.txt')