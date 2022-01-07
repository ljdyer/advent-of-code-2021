import re
from collections import Counter


ORIENTATION_DESCRIPTORS = [
    ('x', 'y', 'z'),
    ('x', 'z', '-y'),
    ('x', '-y', '-z'),
    ('x', '-z', 'y'),
    ('-x', 'y', '-z'),
    ('-x', 'z', 'y'),
    ('-x', '-y', 'z'),
    ('-x', '-z', '-y'),
    ('y', 'z', 'x'),
    ('y', 'x', '-z'),
    ('y', '-z', '-x'),
    ('y', '-x', 'z'),
    ('-y', 'z', '-x'),
    ('-y', '-x', '-z'),
    ('-y', '-z', 'x'),
    ('-y', 'x', 'z'),
    ('z', 'x', 'y'),
    ('z', '-x', '-y'),
    ('z', 'y', '-x'),
    ('z', '-y', 'x'),
    ('-z', '-x', 'y'),
    ('-z', '-y', '-x'),
    ('-z', 'y', 'x'),
    ('-z', 'x', '-y')
]


# ====================
def orientation_state(sign_and_letter: str) -> tuple:

    if sign_and_letter[0] == '-':
        return (-1, sign_and_letter[1])
    else:
        return (1, sign_and_letter[0])


ORIENTATIONS = [list(map(orientation_state, x))
                for x in ORIENTATION_DESCRIPTORS]


# ====================
class Scanner:

    # ====================
    def __init__(self, beacons_relative):

        self.orientation = 0
        self.beacons_relative = beacons_relative
        self.beacons_orientated = beacons_relative

    # # ====================
    # def __str__(self):

    #     beacon_coords = []
    #     for b in self.beacons_absolute:
    #         beacon_coords.append(str(b))
    #     return '\n'.join(beacon_coords)

    # ====================
    def set_orientation(self, orientation: int):

        self.orientation = orientation
        self.refresh_beacon_coords()

    # ====================
    def get_shifted(self, coords: tuple):

        x_shift, y_shift, z_shift = coords
        return set([(x + x_shift, y + y_shift, z + z_shift) for x, y, z
                    in self.beacons_orientated])
        
    # ====================
    def refresh_beacon_coords(self):
        orientation = ORIENTATIONS[self.orientation]
        orientated = [orientate(beacon, orientation)
                      for beacon in self.beacons_relative]
        self.beacons_orientated = set(sorted(orientated))


# ====================
def orientate(beacon: tuple, orientation: tuple):

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
        set(sorted([beacon_string_to_tuple(beacon)
            for beacon in re.findall(regex, scanner)]))
        for scanner in scanner_data
    ]

    return beacons


# === TESTS ===

# ====================
def test_orientations():
    print("=== test_orientations ===")
    observations = get_beacon_data("data/scanner0_test.txt")
    scanner0 = Scanner(observations[0])
    observation_orientations = {}
    for orientation_index in range(len(ORIENTATIONS)):
        scanner0.set_orientation(orientation_index)
        observation = scanner0.beacons_orientated
        print(observation)
        if observation in observations:
            observation_orientations[observations.index(observation)] = \
                orientation_index
    print(observation_orientations)
    try:
        assert sorted(observation_orientations.keys()) == list(range(5))
        print("Passed.")
    except AssertionError:
        print("!!! Failed !!!")
        quit()


# ====================
def overlapping_beacons(beacons1: set, beacons2: set):

    beacons = beacons1.intersection(beacons2)
    return list(beacons)



# ====================
def sign_only_int(input_: int) -> int:

    if input_ > 0:
        return 1
    elif input_ < 0:
        return -1
    elif input_ == 0:
        return 0


# ====================
def sign_only(coords: tuple):

    return tuple([sign_only_int(x) for x in coords])


# ====================
def same_signs(beacons1: set, beacons2: set):

    beacon1_signs = Counter([sign_only(beacon) for beacon in beacons1])
    beacon2_signs = Counter([sign_only(beacon) for beacon in beacons2])
    return sum((beacon1_signs & beacon2_signs).values())





# === MAIN PART OF PROGRAM ===

test_orientations()

scanner_observations = get_beacon_data("data/test.txt")
scanners = []

for beacon_data in scanner_observations:
    scanners.append(Scanner(beacon_data))

scanner0_beacons = scanners[0].get_shifted((0, 0, 0))
for orientation in range(len(ORIENTATIONS)):
    print(orientation)
    scanners[1].set_orientation(orientation)
    scanner1_beacons = scanners[1].get_shifted((0,0,0))
    print(same_signs(scanner0_beacons, scanner1_beacons))
    

    # for x in range(-2000,2000):
    #     for y in range(-2000,2000):
    #         for z in range(-2000,2000):
    #             num_overlapping = len(overlapping_beacons(scanner0_beacons, scanner1_beacons))
    #             if num_overlapping > 0:
    #                 print(num_overlapping)
