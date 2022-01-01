from helper import *

# ===============================
def parse_file(file) -> tuple:
    lines = get_lines_from_file(file)
    blank_line = lines.index('')
    algorithm = ''.join(lines[:blank_line])
    image = lines[blank_line+1:]
    return (algorithm, image)


# ===============================
def get_surrounding_pixels(image, x, y) -> list:

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

    surrounding = get_surrounding_pixels(image, x, y)
    binary = ''.join([pixel_to_bit(p) for p in surrounding])
    decimal = int(binary, 2)
    
    return decimal


# ===============================
def get_output_pixel(image, x, y) -> str:

    decimal = get_decimal(image, x, y)
    output_pixel = algorithm[decimal]
    
    return output_pixel


# ===============================
def print_image(image):

    for row in image:
        print(row)
    print()


# ===============================
def add_border(image, border_thickness):
    
    new_image = []
    for i in range(len(image)):
        new_image.append('.' * border_thickness + image[i] + '.' * border_thickness)
    width = len(new_image[0])
    new_image = ['.' * width] * border_thickness + new_image + ['.' * width] * border_thickness
    return new_image


# ===============================
def count_light(image) -> int:

    pixels = [pixel for row in image for pixel in row]
    return pixels.count('#')


# ===============================
def enhance(image):

    x_range = range(1, len(image[0]) - 1)
    y_range = range(1, len(image) - 1)

    new_image = [''.join([get_output_pixel(image, x, y) for x in x_range]) for y in y_range]
    
    return new_image
    

# ===============================

# Part One
algorithm, image = parse_file('data.txt')
image = add_border(image, 10)
for step in range(2):
    image = enhance(image)
print("Part One answer:", count_light(image))

# Part Two
algorithm, image = parse_file('data.txt')
image = add_border(image, 100)
for step in range(50):
    image = enhance(image)
print("Part Two answer:", count_light(image))
