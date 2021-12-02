#!/bin/python3

with open("sub-route") as sub_routes_file:
    curr_pos = 0
    curr_depth = 0

    for line in sub_routes_file:
        instruction = line.split(" ")
        command = instruction[0]
        amount = int(instruction[1])
        if command == "forward":
            curr_pos += amount
        elif command == "down":
            curr_depth += amount
        elif command == "up":
            curr_depth -= amount

    print(f"Position: {curr_pos}")
    print(f"Depth: {curr_depth}")
    print(curr_pos * curr_depth)
