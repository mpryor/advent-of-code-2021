import sys
import numpy as np


def adj(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]


def in_bounds(y, x, grid):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y])


def search(grid, y, x, visited):
    if (y, x) in visited or not in_bounds(y, x, grid) or grid[y][x] == 9:
        return 0
    else:
        visited.append((y, x))
        return sum([search(grid, y, x, visited) for y, x in adj(y, x)]) + 1


grid = np.genfromtxt("input", delimiter=1, dtype="int")
t = []
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        adj_cells = [(y, x) for y, x in adj(i, j) if in_bounds(y, x, grid)]
        curr_min = min(min([grid[y][x] for y, x in adj_cells]), col)
        if curr_min == col:
            t.append(search(grid, i, j, []))

print(np.product(sorted(t, reverse=True)[0:3]))
