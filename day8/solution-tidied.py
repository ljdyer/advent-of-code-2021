from helper import *

def reverse_dict(d):
        return {v:k for k,v in d.items() if not isinstance(v,list)}

obs_maps = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
char_maps = reverse_dict(obs_maps)

# Get data
lines = get_lines_from_file("data.txt")


# ====================
def sort_string(s):
    return ''.join(sorted(s))


# ====================
def observations(line):
    line = line.replace('| ', '')
    obs = [sort_string(o) for o in line.split(" ")]
    return obs


lines = [observations(l) for l in lines]


# ====================
def get_obs_with_len(my_len, line):
    """Return obs that have len l in line"""

    obs = list(set(([obs for obs in line if len(obs) == my_len])))
    if len(obs) == 1:
        return obs[0]
    else:
        return obs


# ====================
def get_mapping(line):

    real_to_obs = {}

    def unknown(x):
        if x not in obs_to_real.keys():
            return True
        else:
            return False

    def update_mapping(m):
        for key, val in m.items():
            if isinstance(m[key], list):
                m[key] = [x for x in val if x not in m.values()]
                if len(m[key]) == 1:
                    m[key] = m[key][0]
        return m

    # Get observed versions of numbers with unique number of segments
    one = get_obs_with_len(2,line)
    seven = get_obs_with_len(3,line)
    four = get_obs_with_len(4,line)
    eight = get_obs_with_len(7,line)
    five_segs = get_obs_with_len(5,line)

    # a is in 7 but not in 1
    real_to_obs['a'] = [x for x in seven if x not in one][0]
    # c and f are in 7 and 1
    cf = list(set([x for x in seven if x in one]))
    real_to_obs['c'] = cf
    real_to_obs['f'] = cf
    # b and d are in 4 but not in 7 or 1
    bd = list(set([x for x in four if not x in cf]))
    real_to_obs['b'] = bd
    real_to_obs['d'] = bd
    # e and g are in 8 but not in 4 or 7
    eg = list(set([x for x in eight if not (x in four or x in seven)]))
    real_to_obs['e'] = eg
    real_to_obs['g'] = eg
    # d and g are in all numbers with 5 segments
    dg = [x for x in five_segs[0] if x in five_segs[1] and x in five_segs[2] and x != real_to_obs['a']]
    real_to_obs['d'] = [x for x in real_to_obs['d'] if x in dg][0]
    real_to_obs['g'] = [x for x in real_to_obs['g'] if x in dg][0]

    real_to_obs = update_mapping(real_to_obs)
    obs_to_real = reverse_dict(real_to_obs)

    for l in line:
        remaining_unknowns = [x for x in l if unknown(x)]
        if len(l) == 6 and len(remaining_unknowns) == 1:
            real_to_obs['f'] = remaining_unknowns[0]

    real_to_obs = update_mapping(real_to_obs)
    obs_to_real = reverse_dict(real_to_obs)

    def decode(l):
        return ''.join(obs_to_real[x] for x in l)
    def get_number(l):
        return char_maps[''.join(sorted(l))]

    decoded = [get_number(decode(l)) for l in line][-4:]

    return ''.join([str(d) for d in decoded])


answers = [int(get_mapping(line)) for line in lines]
answer = sum(answers)
print(answer)