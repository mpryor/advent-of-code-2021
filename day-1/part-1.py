#!/bin/python3
import sys

with open("depths", "r") as depths_file:
    prev = sys.maxsize

    num_increments = 0

    for line in depths_file:
        curr = int(line)
        if curr > prev:
            num_increments += 1
        prev = curr

    print(num_increments)
