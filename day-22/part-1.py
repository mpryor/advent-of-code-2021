import numpy as np
from itertools import product
from numpy.core.fromnumeric import shape

def in_bounds(rng):
    return -50 <= rng[0] <= 50 and -50 <= rng[1] <= 50

with open("input") as input_file:
    instructions = []
    for line in input_file:
        on_off, ranges = line.strip().split(" ")
        x,y,z = [[int(i[0]), int(i[1])] for i in [l.split("=")[1].split("..") for l in ranges.split(",")]]
        instructions.append((on_off, x, y, z))

    grid = np.zeros(shape=(200000, 200000, 200000), dtype=int)
    for inst, x_rng, y_rng, z_rng in instructions:
        new_val = 0
        if inst == "on":
            new_val = 1

        if in_bounds(x_rng) and in_bounds(y_rng) and in_bounds(z_rng):
            for set_point in product(range(x_rng[0], x_rng[1] + 1), range(y_rng[0], y_rng[1] + 1), range(z_rng[0], z_rng[1] + 1)):
                x,y,z = set_point
                offset = 100000
                grid[x + offset][y + offset][z + offset] = new_val

        print(np.sum(grid))