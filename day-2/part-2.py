#!/bin/python3
with open("sub-route") as sub_routes_file:
    aim = pos = depth = 0

    for line in sub_routes_file:
        command, amount = line.split(" ")
        amount = int(amount)

        if command == "forward":
            pos += amount
            depth += amount * aim
        elif command == "down":
            aim += amount
        elif command == "up":
            aim -= amount

    print(f"Position: {pos}")
    print(f"Depth: {depth}")
    print(pos * depth)
