import numpy as np
from numpy.lib.function_base import flip

grid = np.array([
    ["x", "-", "-", "-"],
    ["-", "x", "-", "-"],
    ["-", "-", "x", "-"],
    ["-", "-", "-", "x"]
])


def flip_x(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i]) // 2):
            x_len = len(grid[i])
            distance_from_end = x_len - j
            new_j = distance_from_end - 1
            tmp = grid[i][new_j]
            grid[i][new_j] = grid[i][j]
            grid[i][j] = tmp


def flip_y(grid):
    for i in range(len(grid) // 2):
        for j in range(len(grid[i])):
            y_len = len(grid)
            distance_from_end = y_len - i
            new_i = distance_from_end - 1
            tmp = grid[new_i][j]
            grid[new_i][j] = grid[i][j]
            grid[i][j] = tmp


print(grid)
flip_y(grid)
print(grid)
