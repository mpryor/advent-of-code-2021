import sys
from collections import Counter

with open("input") as input_file:
    positions = [int(x) for x in input_file.read().split(",")]

pos_counter = Counter(positions)
min_fuel = int(sys.maxsize)
for target_pos in range(0, max(pos_counter)):
    total_fuel = 0
    for curr_pos, count in pos_counter.items():
        fuel_cost = abs(curr_pos - target_pos)
        total_fuel += count * fuel_cost * (fuel_cost + 1) // 2
    min_fuel = min(total_fuel, min_fuel)

print(min_fuel)
