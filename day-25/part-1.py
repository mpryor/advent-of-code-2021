from copy import deepcopy
import numpy as np

grid = [[chr for chr in l.strip()] for l in open("input").readlines()]

def draw_grid(grid):
    for row in grid:
        row_str = ""
        for c in row:
            row_str += c
        # print(row_str)

draw_grid(grid)

has_moved = True
steps = 0
while has_moved:
    # print("\n")

    steps += 1
    has_moved = False
    new_grid = deepcopy(grid)
    for y, row in enumerate(grid):
        x_wrap = False
        for x in range(len(row)):
            c = grid[y][x]
            if c == ">":
                if x == 0:
                    x_wrap = True
                next_pos = x + 1 if x + 1 < len(row) else 0
                if grid[y][next_pos] == "." and not (x_wrap and x == len(row) - 1):
                    has_moved = True
                    new_grid[y][next_pos] = ">"
                    new_grid[y][x] = "."
                    grid[y][x] = "."
                else:
                    grid[y][x] = c
    grid = new_grid
    new_grid = deepcopy(grid)

    for x in range(len(grid[0])):
        y_wrap = False
        for y in range(len(grid)):
            c = grid[y][x]
            if c == "v":
                if y == 0:
                    y_wrap = True
                next_pos = y + 1 if y + 1 < len(grid) else 0
                if grid[next_pos][x] == "." and not (y_wrap and y == len(grid) - 1):
                    has_moved = True
                    new_grid[next_pos][x] = "v"
                    new_grid[y][x] = "."
                    grid[y][x] = "."
                else:
                    grid[y][x] = c
    grid = new_grid
    draw_grid(grid)

print(steps)