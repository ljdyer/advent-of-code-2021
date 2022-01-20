# TODO: Tidy up and create readme.md!

import random
import re
from collections import Counter
from orientations import ORIENTATIONS


# ====================
def get_text_from_file(file: str) -> list:
    """Get text from a file"""

    with open(file, encoding='utf-8') as file:
        lines = file.read()
    return lines


# ====================
def get_groups(regex: str, text: str) -> tuple:
    """Get regex groups from a string"""

    return re.findall(regex, text)


# ====================
def get_scanner_info_from_file(file: str) -> list:
    """Get list of beacons observed from each scanner from data file"""

    data = get_text_from_file(file)
    regex = r'--- scanner \d+ ---'
    scanner_data = [scanner for scanner in re.split(regex, data)
                    if not scanner == ""]

    regex = r'(.*),(.*),(.*)'
    scanners = [[tuple(int(x) for x in get_groups(regex, line)[0])
                for line in scanner.splitlines() if get_groups(regex, line)]
                for scanner in scanner_data]

    return scanners


# ====================
def orientate(beacon: tuple, orientation_index: int) -> tuple:

    order, signs = ORIENTATIONS[orientation_index]

    return (
        beacon[order[0]] * signs[0],
        beacon[order[1]] * signs[1],
        beacon[order[2]] * signs[2],
    )


# ====================
def orientate_all(beacons: list, orientation_index: int) -> list:

    return [orientate(beacon, orientation_index) for beacon in beacons]


# ====================
def add(beacon1: tuple, beacon2: tuple):

    return (beacon1[0] + beacon2[0],
            beacon1[1] + beacon2[1],
            beacon1[2] + beacon2[2])


# ====================
def add_all(beacons: list, distance: tuple):

    return [add(beacon, distance) for beacon in beacons]


# ====================
def transform(beacon: list, orientation_and_distance: tuple):

    orientation, distance = orientation_and_distance
    oriented = orientate(beacon, orientation)
    mapped = add(oriented, distance)
    return mapped


# ====================
def transform_all(beacons: list, orientation_and_distance: tuple):

    orientation, distance = orientation_and_distance
    oriented = orientate_all(beacons, orientation)
    mapped = add_all(oriented, distance)
    return mapped


# ====================
def manhattan(point1: tuple, point2: tuple):

    x, y, z = point1
    X, Y, Z = point2

    return(abs(x - X) + abs(y - Y) + abs(z - Z))


# ====================
def get_mappings(scanner_one: list, scanner_two: list) -> dict:

    distances = {'x': 0, 'y': 0, 'z': 0}
    orientation_indices = list(range(len(ORIENTATIONS)))

    # x distances between the same beacon viewed from different scanners are
    # the same if the scanners are oriented correctly
    for orientation_index in orientation_indices.copy():
        order, signs = ORIENTATIONS[orientation_index]
        scanner_two_x = [beacon[order[0]] * signs[0] for beacon in scanner_two]
        x_distances = []
        for beacon in scanner_one:
            x_distances.extend(beacon[0] - x for x in scanner_two_x)
        dist, freq = Counter(x_distances).most_common()[0]
        if freq < 12:
            orientation_indices.remove(orientation_index)
        else:
            distances['x'] = dist

    if not orientation_indices:
        return None

    # If the 2 scanners see at least 12 of the same beacons, there will be 4
    # orientations in the list.
    # Doing the same calculation on y distances narrows it down to 1
    # orientation.
    for orientation_index in orientation_indices.copy():
        order, signs = ORIENTATIONS[orientation_index]
        scanner_two_y = [beacon[order[1]] * signs[1] for beacon in scanner_two]
        y_distances = []
        for beacon in scanner_one:
            y_distances.extend(beacon[1] - y for y in scanner_two_y)
        dist, freq = Counter(y_distances).most_common()[0]
        if freq < 12:
            orientation_indices.remove(orientation_index)
        else:
            distances['y'] = dist

    if not orientation_indices:
        return None
    elif len(orientation_indices) > 1:
        raise RuntimeError()

    # Orientation is now determined, so just get the y distance
    s2_orientation = orientation_indices[0]

    order, signs = ORIENTATIONS[s2_orientation]
    scanner_two_z = [beacon[order[2]] * signs[2] for beacon in scanner_two]
    z_distances = []
    for beacon in scanner_one:
        z_distances.extend(beacon[2] - z for z in scanner_two_z)
    dist, freq = Counter(z_distances).most_common()[0]
    if freq >= 12:
        distances['z'] = dist

    distances = (distances['x'], distances['y'], distances['z'])

    return (s2_orientation, distances)


# ====================
if __name__ == "__main__":

    scanners = get_scanner_info_from_file('data/data.txt')

    mappings = {}

    print('Getting mappings...')
    for s1_index in range(len(scanners)):
        for s2_index in range(len(scanners)):
            if s1_index != s2_index:
                mapping = get_mappings(scanners[s1_index], scanners[s2_index])
                if mapping:
                    mappings[(s1_index, s2_index)] = (mapping)

    # === Part One ===

    print('Observing beacons...')
    # Start with scanner 0 beacons and orientation 0
    current_orientation = 0
    scanner_numbers = range(len(scanners))
    scanners_considered = [0]
    beacons_so_far = set(scanners[0].copy())
    orientations_covered = []

    # While there are scanners that have not been considered
    while True:

        # Add beacons for any scanners that can be mapped to the current
        # orientation
        map_to_current = [x for x in scanner_numbers
                          if (current_orientation, x) in mappings
                          and x not in scanners_considered]
        for scanner in map_to_current:
            new_beacons = transform_all(
                scanners[scanner], mappings[(current_orientation, scanner)]
            )
            beacons_so_far.update(new_beacons)
            scanners_considered.append(scanner)
        orientations_covered.append(current_orientation)

        # If all scanners have been considered, we are finished
        if sorted(scanners_considered) == sorted(scanner_numbers):
            break

        try:
            # If possible, switch to the orientation we haven't tried yet that
            # we can map to the highest number of other orientations
            next_orientation_candidates = [x for x in range(len(ORIENTATIONS))
                                           if
                                           (x, current_orientation) in mappings
                                           and x not in orientations_covered]
            routes_out = [(len([mapping for mapping in mappings.keys()
                                if mapping[1] == candidate
                                and mapping[0] not in orientations_covered]),
                           candidate)
                          for candidate in next_orientation_candidates]
            next_orientation = max(routes_out)[1]
        except ValueError:
            # Otherwise, just choose one at random and we'll get there
            # eventually!
            next_orientation_candidates = [x for x in scanner_numbers
                                           if (x, current_orientation)
                                           in mappings]
            next_orientation = random.choice(next_orientation_candidates)

        beacons_so_far = set(transform_all(
            beacons_so_far, mappings[(next_orientation, current_orientation)]
        ))
        current_orientation = next_orientation

    print("Part One answer:", len(beacons_so_far))

    # === Part Two ===

    print('Observing scanners...')
    # Start with scanner 0 and orientation 0
    current_orientation = 0
    scanner_numbers = range(len(scanners))
    scanners_considered = [0]
    scanners_so_far = set([(0, 0, 0)])
    orientations_covered = []

    # While there are scanners that have not been considered
    while True:

        map_to_current = [x for x in scanner_numbers
                          if (current_orientation, x) in mappings
                          and x not in scanners_considered]
        for scanner in map_to_current:
            new_beacon = transform(
                (0, 0, 0), mappings[(current_orientation, scanner)]
            )
            scanners_so_far.add(new_beacon)
            scanners_considered.append(scanner)
        orientations_covered.append(current_orientation)

        # If all scanners have been considered, we are finished
        if sorted(scanners_considered) == sorted(scanner_numbers):
            break

        try:
            # If possible, switch to the orientation we haven't tried yet that
            # we can map to the highest number of other orientations
            next_orientation_candidates = [x for x in range(len(ORIENTATIONS))
                                           if
                                           (x, current_orientation) in mappings
                                           and x not in orientations_covered]
            routes_out = [(len([mapping for mapping in mappings.keys()
                                if mapping[1] == candidate
                                and mapping[0] not in orientations_covered]),
                           candidate)
                          for candidate in next_orientation_candidates]
            next_orientation = max(routes_out)[1]
        except ValueError:
            # Otherwise, just choose one at random and we'll get there
            # eventually!
            next_orientation_candidates = [x for x in scanner_numbers
                                           if (x, current_orientation)
                                           in mappings]
            next_orientation = random.choice(next_orientation_candidates)

        scanners_so_far = set(transform_all(
            scanners_so_far, mappings[(next_orientation, current_orientation)]
        ))
        current_orientation = next_orientation

    manhattans = []

    for s1 in scanners_so_far:
        for s2 in scanners_so_far:
            manhattans.append(manhattan(s1, s2))

    print("Part Two answer:", max(manhattans))
