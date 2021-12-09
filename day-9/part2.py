import sys
import numpy as np

t = 0
grid = np.genfromtxt("sample", delimiter=1, dtype="int")


for i, row in enumerate(grid):
    for j, col in enumerate(row):
        # check if current cell is less than all adjacent cells
        curr_cell = grid[i][j]

        r = grid[i][j + 1] if j + 1 < len(row) else sys.maxsize
        l = grid[i][j - 1] if j - 1 > -1 else sys.maxsize
        u = grid[i-1][j] if i - 1 > -1 else sys.maxsize
        d = grid[i+1][j] if i + 1 < len(grid) else sys.maxsize
        if curr_cell < r and curr_cell < l and curr_cell < u and curr_cell < d:
            # we've found the lowest point, now find the size of the basin
            print(i, j)
            t += curr_cell + 1
