import numpy as np
from collections import Counter, deque
from itertools import product

grid = np.genfromtxt("input", dtype="int", delimiter=1)


def in_bounds(grid, y, x):
    return -1 < y < len(grid) and -1 < x < len(grid[y])


def get_adj(grid, y, x):
    ys = [y-1, y, y+1]
    xs = [x-1, x, x+1]
    adj_cells = product(ys, xs)
    return [(adj_y, adj_x) for adj_y, adj_x in adj_cells if in_bounds(grid, adj_y, adj_x) if (adj_y, adj_x) != (y, x)]


q = deque()

flashes = 0

has_synced = False

step = 0
while not has_synced:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            q.append((y, x))

    while len(q) > 0:
        y, x = q.popleft()
        grid[y][x] += 1
        if grid[y][x] == 10:
            q += get_adj(grid, y, x)

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if grid[y][x] >= 10:
                grid[y][x] = 0
                flashes += 1

    if grid.max() == 0:
        has_synced = True

    step += 1

print(step)
