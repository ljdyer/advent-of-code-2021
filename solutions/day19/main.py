from helper import *

lines = get_lines_from_file("data.txt")

lines = [l for l in lines]

POS_NEG = [('+', '+', '+'), ('+', '+', '-'), ('+', '-', '-'), ('-', '-', '-')]
X_Y = [('x', 'y', 'z'), ('x', 'z', 'y'), ('y', 'x', 'z'), ('y', 'z', 'x'), ('z', 'x', 'y'), ('z', 'y', 'x')]

ORIENTATIONS = [['+x', '+y', '+z'], ['+x', '+z', '+y'], ['+y', '+x', '+z'], ['+y', '+z', '+x'],
['+z', '+x', '+y'], ['+z', '+y', '+x'], ['+x', '+y', '-z'], ['+x', '+z', '-y'],
['+y', '+x', '-z'], ['+y', '+z', '-x'], ['+z', '+x', '-y'], ['+z', '+y', '-x'],
['+x', '-y', '-z'], ['+x', '-z', '-y'], ['+y', '-x', '-z'], ['+y', '-z', '-x'],
['+z', '-x', '-y'], ['+z', '-y', '-x'], ['-x', '-y', '-z'], ['-x', '-z', '-y'],
['-y', '-x', '-z'], ['-y', '-z', '-x'], ['-z', '-x', '-y'], ['-z', '-y', '-x']]

ORIENTATIONS_DICT = {count: orientation for count, orientation in enumerate(ORIENTATIONS)}


# ====================
class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons
        self.orientations = {}

    def beacon_list(self):
        