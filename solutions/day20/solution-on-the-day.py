from helper import *

# ==============================
def test_get_nine():

    print('=== test_get_nine ===')

    get_nine = get_nine_pixels(image, 2,2)
    try:
        assert get_nine == "...#...#."
    except:
        print('Failed!')
        print("Got:", get_nine)
        print("EXpected:", "...#...#.")
        exit()
    print('Passed.')
    print()


def test_get_decimal():

    print('=== test_get_decimal ===')

    decimal = get_decimal(image, 2,2)
    expected = 34
    try:
        assert decimal == expected
    except:
        print('Failed!')
        print("Got:", decimal)
        print("Expected:", expected)
        exit()
    print('Passed.')


def test_get_output_pixel():

    print('=== test_get_output_pixel ===')

    pixel = get_output_pixel(image, 2,2)
    expected = '#'
    try:
        assert pixel == expected
    except:
        print('Failed!')
        print("Got:", pixel)
        print("Expected:", expected)
        exit()
    print('Passed.')
    print()


# =============================================================

# ===============================
def get_nine_pixels(image, x, y) -> list:

    top_row = image[y-1][x-1:x+2]
    middle_row = image[y][x-1:x+2]
    bottom_row = image[y+1][x-1:x+2]
    return ''.join([top_row, middle_row, bottom_row])


# ===============================
def pixel_to_bit(p: str) -> str:

    if p == '#':
        return '1'
    else:
        return '0'


# ===============================
def get_decimal(image, x, y) -> str:

    nine = get_nine_pixels(image, x, y)
    binary = ''.join([pixel_to_bit(p) for p in nine])
    decimal = int(binary, 2)
    
    return decimal


# ===============================
def get_output_pixel(image, x, y) -> str:

    decimal = get_decimal(image, x, y)
    # print(list(enumerate(algorithm))[decimal - 3: decimal + 3])
    # if decimal == 0:
    #     output_pixel = '.'
    # else:
    #     output_pixel = algorithm[decimal]
    output_pixel = algorithm[decimal]
    
    return output_pixel


# ===============================
def print_image(image):

    for row in image:
        print(row)
    print()


# ===============================
def add_blanks(image):
    
    for i in range(len(image)):
        image[i] = '..' + image[i] + '..'
    width = len(image[0])
    image = ['.' * width] * 2 + image + ['.' * width] * 2
    return image

# ===============================
def count_light(image) -> int:

    pixels = [pixel for row in image for pixel in row]
    return pixels.count('#')



# ===============================
def convert_image(image):

    image = add_blanks(image)
    image = add_blanks(image)
    image = add_blanks(image)

    height = len(image)
    width = len(image[0])
    x_range = range(1,width-1)
    y_range = range(1,height-1)

    output_image = []
    for y in y_range:
        this_line = ''
        for x in x_range:
            # print(x,y)
            # print(get_nine_pixels(image,x,y))
            new_pixel = get_output_pixel(image, x, y)
            this_line = this_line + new_pixel
        output_image.append(this_line)
    
    return output_image


# print(algorithm)

# test_get_nine()
# test_get_decimal()
# test_get_output_pixel()

lines = get_lines_from_file("data.txt")
# lines = get_lines_from_file("test.txt")
blank_line = lines.index('')
algorithm = ''.join(lines[:blank_line])
image = lines[blank_line+1:]

# print_image(image)

width = len(image[0])
height = len(image)

border_start = 2
converted = image
for i in range(50):
    converted = convert_image(converted)
    border_start = border_start + 3

# print_image(converted)
print_image(converted)

width = len(converted[0])
height = len(converted)
converted = [row[border_start:width-border_start] for row in converted[border_start:height-border_start]]

# print(len(converted[0]))
# print(len(converted))
# print_image(converted)

print(count_light(converted))