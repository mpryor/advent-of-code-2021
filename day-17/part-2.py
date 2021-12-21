from copy import copy
from itertools import product

with open("input") as input_file:
    lines = input_file.read().split()
    x_range = [int(val) for val in lines[2].replace("x=", "").replace(",", "").split("..")]
    y_range = [int(val) for val in lines[3].replace("y=", "").split("..")]

results = []

possible_xs = range(0, x_range[1] + 10)
possible_ys = range(y_range[0] - 10, abs(y_range[0]) + 10)
velocities = [list(v) for v in product(possible_xs, possible_ys)]

for initial_velocity in velocities:
    probe_pos = [0, 0]
    velocity = copy(initial_velocity)
    while velocity[1] >= 0 or (probe_pos[0] <= x_range[1] and probe_pos[1] >= y_range[0]):
        probe_pos[0] += velocity[0]
        probe_pos[1] += velocity[1]

        if velocity[0] > 0:
            velocity[0] -= 1
        if velocity[0] < 0:
            velocity[0] += 1

        velocity[1] -= 1

        if x_range[0] <= probe_pos[0] <= x_range[1] and y_range[0] <= probe_pos[1] <= y_range[1]:
            results.append(initial_velocity)
            break

print(results)
print(len(results))