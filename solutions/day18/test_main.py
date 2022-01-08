from main import *


# ====================
LISTS_AND_EXPLODES = [
    ([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]),
    ([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]),
    ([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
    ([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
    ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
    ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]])
]

LISTS = [lis for lis, _ in LISTS_AND_EXPLODES] + \
    [[[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
        [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]]

STEPS = [
    [[[[0,7],4],[7,[[8,4],9]]],[1,1]],
    [[[[0,7],4],[15,[0,13]]],[1,1]],
    [[[[0,7],4],[[7,8],[0,13]]],[1,1]],
    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]],
    [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
]

LISTS_AND_SPLITS = [
    ([[[[0,7],4],[15,[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,13]]],[1,1]]),
    ([[[[0,7],4],[[7,8],[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
]

BEFORE_AND_AFTER = [
    ([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], [[[[0,7],4],[[7,8],[6,0]]],[8,1]]),
    ([[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]], [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]])  
]

FILES_AND_RESULTS = [
    ('test_data/test1.txt', [[[[1,1],[2,2]],[3,3]],[4,4]]),
    ('test_data/test2.txt', [[[[3,0],[5,3]],[4,4]],[5,5]]),
    ('test_data/test3.txt', [[[[5,0],[7,4]],[5,5]],[6,6]]),
    ('test_data/test4.txt', [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
]

SUMS_AND_REDUCTIONS = [
    ([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]], [7,[[[3,7],[4,3]],[[6,3],[8,8]]]], [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]),
    ([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]], [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]], [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]),
    ([[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]], [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]], [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]),
    ([[[[4,3],4],4],[7,[[8,4],9]]],[1,1],[[[[0,7],4],[[7,8],[6,0]]],[8,1]])
]

MAGNITUDES = [
    ([[1,2],[[3,4],5]], 143),
    ([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384),
    ([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
    ([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
    ([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
    ([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488)
]


# ====================
def test_list_map_convert():

    print('=== test_list_map_convert ===')
    for l in LISTS:
        assert map_to_list(list_to_map(l)) == l
    print('Passed.')
    print()


# ====================
def test_explode():

    print('=== test_explode ===')
    for l, explosion in LISTS_AND_EXPLODES:
        _, exploded = reduction_step(l)
        try:
            assert (exploded == explosion)
        except:
            print('Failed!')
            print(l)
            print(explosion)
            print(exploded)
            exit()
    print('Passed.')
    print()


# ====================
def test_split():

    print('=== test_split ===')
    for l, split_ in LISTS_AND_SPLITS:
        _, splitted = reduction_step(l)
        try:
            assert (splitted == split_)
        except:
            print('Failed!')
            print(l)
            print(split_)
            print(splitted)
            exit()
    print('Passed.')
    print()


# ====================
def test_split_or_explode():

    print('=== test_split_or_explode ===')
    for i in range(1,len(STEPS)):
        _, done = reduction_step(STEPS[i-1])
        try:
            assert done == STEPS[i]
        except:
            print('Failed!')
            print(i)
            print(STEPS[i])
            print(STEPS[i-1])
            print(done)
            quit()
    print('Passed.')
    print()


# ====================
def test_reduce():

    print('=== test_reduce ===')
    for before, after in BEFORE_AND_AFTER:
        reduced = reduce(before)
        try:
            assert reduced == after
        except:
            print('Failed')
            print("Before:", before)
            print("After:", after)
            print("Expected:", reduced)
            exit()
    print('Passed.')
    print()


# ====================
def test_whole_file():

    print('=== test_whole_file ===')
    for filename, reference in FILES_AND_RESULTS:
        a_and_r = added_and_reduced(filename)
        try:
            assert a_and_r == reference
        except:
            print('Failed!')
            print(filename)
            print(reference)
            print(a_and_r)
            print
            exit()
    print('Passed.')
    print()


# ====================
def test_add_and_reduce():

    print('=== test_add_and_reduce ===')
    for x, y, answer in SUMS_AND_REDUCTIONS:
        added = add(x,y)
        ans = reduce(added)
        try:
            assert ans == answer
        except:
            print('Failed')
            print("After addition:", added)
            print("After reduction:", ans)
            print("Expected:", answer)
            exit()
    print('Passed.')
    print()


# ====================
def test_magnitude():
    print('=== test_magnitude ===')
    for snum, mag_expected in MAGNITUDES:
        mag_actual = magnitude(snum)
        try:
            assert mag_actual == mag_expected
        except:
            print('!!! Failed for snailfish number', snum)
            print("Actual:", mag_actual)
            print("Expected:", mag_expected)
            exit()
    print('Passed.')
    print()


# ====================
def test_magnitude_from_file():
    
    print('=== test_magnitude_from_file ===')
    mag_actual = magnitude_from_file('test_data/test_magnitude.txt')
    mag_expected = 4140
    try:
        assert mag_actual == mag_expected
        print("Passed.")
    except:
        print("!!! Failed !!!")
        print("Actual:", mag_actual)
        print("Expected:", mag_expected)


# ============================
test_list_map_convert()
test_explode()
test_split()
test_split_or_explode()
test_add_and_reduce()
test_whole_file()
test_magnitude()
test_magnitude_from_file()