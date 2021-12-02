#!/bin/python3

with open("sub-route") as sub_routes_file:
    aim = 0
    horizontal_position = 0
    curr_depth = 0

    for line in sub_routes_file:
        instruction = line.split(" ")
        command = instruction[0]
        amount = int(instruction[1])
        if command == "forward":
            horizontal_position += amount
            curr_depth += amount * aim
        elif command == "down":
            aim += amount
        elif command == "up":
            aim -= amount

    print(f"Position: {horizontal_position}")
    print(f"Depth: {curr_depth}")
    print(horizontal_position * curr_depth)
