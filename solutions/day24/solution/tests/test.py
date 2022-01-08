import math


# ====================
def test1(input_: str):

    input_ = list(input_)
    x = 0
    y = 0
    z = 0
    w = 0
    x = int(input_.pop(0))
    x = x * -1
    return {'x': x, 'y': y, 'z': z, 'w': w}


# ====================
def test2(input_: str):

    input_ = list(input_)
    x = 0
    y = 0
    z = 0
    w = 0
    z = int(input_.pop(0))
    x = int(input_.pop(0))
    z = z * 3
    z = int(z == x)
    return {'x': x, 'y': y, 'z': z, 'w': w}


# ====================
def test3(input_: str):

    input_ = list(input_)
    x = 0
    y = 0
    z = 0
    w = 0
    w = int(input_.pop(0))
    z = z + w
    z = z % 2
    w = math.floor(w / 2)
    y = y + w
    y = y % 2
    w = math.floor(w / 2)
    x = x + w
    x = x % 2
    w = math.floor(w / 2)
    w = w % 2
    return {'x': x, 'y': y, 'z': z, 'w': w}


# Test 1 For example, here is an ALU program which takes an input number,
# negates it, and stores it in x:
print(test1('7'))
print(test1('3'))

# Here is an ALU program which takes two input numbers, then sets z to 1 if
# the second input number is three times larger than the first input number,
# or sets z to 0 otherwise:
print(test2('39'))
print(test2('38'))

# Here is an ALU program which takes a non-negative integer as input, converts
# it into binary, and stores the lowest (1's) bit in z, the second-lowest
# (2's) bit in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's)
# bit in w:
print(test3('8'))
print(test3('7'))
