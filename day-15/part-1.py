import sys
import numpy as np
from copy import copy

grid = np.genfromtxt("input", delimiter=1, dtype="int")
print(grid)


def minCost(cost, m, n):
    tc = [[0 for x in range(len(cost))] for x in range(len(grid[0]))]
    tc[0][0] = 0

    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]

    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]

    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j]

    return tc[m][n]

min_cost = minCost(grid, len(grid) - 1, len(grid[0]) - 1)
print(min_cost)