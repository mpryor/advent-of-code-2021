from math import inf as INFINITY
from collections import defaultdict

def normalize_beacons(beacons):
    # Shift lowest x until it's x == 0, translate all Xs the same amount
    # Shift lowest y until it's y == 0, translate all Ys the same amount
    min_x = INFINITY
    min_y = INFINITY
    translate_x = INFINITY
    translate_y = INFINITY
    for beacon in beacons:
        x,y = beacon
        if x < min_x:
            min_x = x
            translate_x = -(x)
        if y < min_y:
            min_y = y
            translate_y = -(y)
        
    for beacon in beacons:
        beacon[0] = beacon[0] + translate_x
        beacon[1] = beacon[1] + translate_y

scanners = []

with open("sample") as input_file:
    scanners_file = input_file.read().split("\n\n")
    for scanner_block in scanners_file:
        scanner_lines = scanner_block.split("\n")
        scanner_name = scanner_lines[0]
        scanner = {"name": scanner_name, "beacons": []}
        for i in range(1, len(scanner_lines)):
            beac_x, beac_y = scanner_lines[i].split(",")
            scanner["beacons"].append([int(beac_x), int(beac_y)])
        scanners.append(scanner)

    for scanner in scanners:
        normalize_beacons(scanner["beacons"])

    total_scanners = []
    for i, i_scanner in enumerate(scanners):
        for j in range(i + 1, len(scanners)):
            j_scanner = scanners[j]

            map = defaultdict(int)
            for i_beacon in i_scanner["beacons"]:
                map[tuple(i_beacon)] += 1

            for j_beacon in j_scanner["beacons"]:
                map[tuple(j_beacon)] += 1

            no_matches = sum([1 for k,v in map.items() if v == 2])
            if no_matches >= 3:
                for i_beacon in i_scanner["beacons"]:
                    total_scanners.append(i_beacon)

    print(len(total_scanners))