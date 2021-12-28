import re
from collections import defaultdict

def intersect(new_x, new_X, new_y, new_Y, new_z, new_Z, old_x, old_X, old_y, old_Y, old_z, old_Z):
    x = max(new_x, old_x); X = min(new_X, old_X)
    y = max(new_y, old_y); Y = min(new_Y, old_Y)
    z = max(new_z, old_z); Z = min(new_Z, old_Z)
    if x <= X and y <= Y and z <= Z:
        return x, X, y, Y, z, Z

with open("input") as input_file:
    cubes = defaultdict(int)

    for state, new_cube in map(str.split, input_file):
        new_cube = *map(int, re.findall("-?\d+", new_cube)),

        for old_cube, amt in cubes.copy().items():
            if intersection := intersect(*new_cube, *old_cube):
                cubes[intersection] -= amt

        if state == "on":
            cubes[new_cube] += 1

    total_sum = sum([(X-x+1)*(Y-y+1)*(Z-z+1)*amt for (x,X,y,Y,z,Z),amt in cubes.items()])
    print(total_sum)