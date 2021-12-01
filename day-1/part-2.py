#!/bin/python3

# This program calculates the sum of a 3-piece sliding window and compares it to the previous sliding window

# 1,2,3,4,5
# i   j

import sys

with open("depths", "r") as depths_file:
    prev = sys.maxsize

    num_increments = 0
    prev_sum = sys.maxsize
    curr_sum = 0
    j = 0
    depths_file_lines = list(depths_file)

    for i in range(0, len(depths_file_lines) - 2):
        while j < i + 3:
            curr_sum += int(depths_file_lines[j])
            j += 1

        if curr_sum > prev_sum:
            num_increments += 1

        prev_sum = curr_sum
        curr_sum -= int(depths_file_lines[i])

    print(num_increments)
