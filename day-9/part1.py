import sys
import numpy as np

grid = np.genfromtxt("input", delimiter=1, dtype="int")


def search(grid, y, x, visited):
    if (y, x) in visited or y == len(grid) or y < 0 or x == len(grid[y]) or x < 0 or grid[y][x] == 9:
        return 0
    else:
        visited.append((y, x))
        t = 1
        t += search(grid, y+1, x, visited)
        t += search(grid, y-1, x, visited)
        t += search(grid, y, x+1, visited)
        t += search(grid, y, x-1, visited)
        return t


def in_bounds(y, x, grid):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y])


t = []
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        curr_cell = grid[i][j]
        adj = [(y, x) for y, x in [(i, j+1), (i, j-1),
                                   (i-1, j), (i+1, j)] if in_bounds(y, x, grid)]
        curr_min = min(min([grid[y][x] for y, x in adj]), curr_cell)
        if curr_min == curr_cell:
            t.append(search(grid, i, j, []))

print(np.product(sorted(t, reverse=True)[0:3]))
