import re

ORIENTATIONS = [
    ['+x', '+y', '+z'], ['+x', '+z', '+y'], ['+y', '+x', '+z'],
    ['+y', '+z', '+x'], ['+z', '+x', '+y'], ['+z', '+y', '+x'],
    ['+x', '+y', '-z'], ['+x', '+z', '-y'], ['+y', '+x', '-z'],
    ['+y', '+z', '-x'], ['+z', '+x', '-y'], ['+z', '+y', '-x'],
    ['+x', '-y', '-z'], ['+x', '-z', '-y'], ['+y', '-x', '-z'],
    ['+y', '-z', '-x'], ['+z', '-x', '-y'], ['+z', '-y', '-x'],
    ['-x', '-y', '-z'], ['-x', '-z', '-y'], ['-y', '-x', '-z'],
    ['-y', '-z', '-x'], ['-z', '-x', '-y'], ['-z', '-y', '-x']
]

ORIENTATION_TUPLES = [[(int(coord[0] + '1'), coord[1])
                       for coord in orientation]
                      for orientation in ORIENTATIONS]


# ====================
class Scanner:

    # ====================
    def __init__(self, beacons):

        self.orientation = 0
        self.beacons = beacons
        self.beacons_observed = beacons

    # ====================
    def __str__(self):

        observed = []
        for b in self.beacons_observed:
            observed.append(str(b))
        return '\n'.join(observed)

    # ====================
    def set_orientation(self, orientation_index: int):

        self.orientation = orientation_index

        orientation = ORIENTATION_TUPLES[orientation_index]

        def observe_with_orientation(beacon: tuple):
            return observe(beacon, orientation)
        observed = [observe_with_orientation(beacon)
                    for beacon in self.beacons]
        self.beacons_observed = sorted(observed)


# ====================
def observe(beacon: tuple, orientation: tuple):
    beacon_coords = {
        'x': beacon[0], 'y': beacon[1], 'z': beacon[2]
    }
    observed_coords = tuple(
        [coord[0] * beacon_coords[coord[1]] for coord in orientation]
    )
    return observed_coords


# ====================
def get_text_from_file(file: str) -> list:
    """Get text from a file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read()
    return lines


# ====================
def get_groups(regex, text) -> tuple:

    return re.findall(regex, text)


# ====================
def beacon_string_to_tuple(beacon_string: str) -> tuple:

    string_split = beacon_string.split(',')
    beacon_ints = [int(coord) for coord in string_split]
    return tuple(beacon_ints)


# ====================
def get_beacon_data(file: str) -> list:
    """Get beacon data from a file"""

    data = get_text_from_file(file)
    regex = r'--- scanner \d+ ---'
    scanner_data = [scanner for scanner in re.split(regex, data)
                    if not scanner == ""]
    regex = r'.*,.*,.*'
    beacons = [
        sorted([beacon_string_to_tuple(beacon)
                for beacon in re.findall(regex, scanner)])
        for scanner in scanner_data
    ]

    return beacons


data = get_beacon_data("data/scanner0_test.txt")
print(data[4])
scanner0 = Scanner(data[0])
# print(scanner0.beacons_observed)
for orientation_index in range(len(ORIENTATIONS)):
    scanner0.set_orientation(orientation_index)
    print(scanner0.beacons_observed)
    print(orientation_index)
    if sorted(scanner0.beacons_observed) in data:
        print('===')
        print(scanner0.beacons_observed)
        print(data.index(scanner0.beacons_observed))
        print(orientation_index)
        print('===')

