import heapq
import numpy as np
from copy import copy
from itertools import product
from math import inf as INFINITY
from collections import defaultdict

def in_bounds(grid, node):
    y, x = node
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

def get_adj(grid, current_node):
    y,x = current_node
    adj_nodes = [(y-1, x), (y+1, x), (y, x+1), (y, x-1)]
    return [adj_node for adj_node in adj_nodes if in_bounds(grid, adj_node)]

def djikstra(grid):
    min_costs = defaultdict(lambda: INFINITY)
    destination = (len(grid) - 1, len(grid[len(grid) - 1]) - 1)

    pq = []
    heapq.heappush(pq, (0, (0, 0)))
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == destination:
            return current_distance

        if current_distance > min_costs[current_node]:
            continue

        for adj_node in get_adj(grid, current_node):
            distance = current_distance + grid[adj_node[0]][adj_node[1]]
            if distance < min_costs[adj_node]:
                min_costs[adj_node] = distance
                heapq.heappush(pq, (distance, adj_node))

grid = np.genfromtxt("sample", delimiter=1, dtype="int")
new_grid = np.zeros(shape=(len(grid) * 5, len(grid[0]) * 5), dtype=int)

for y, row in enumerate(grid):
    for x, col in enumerate(grid[y]):
        for i, j in product(range(5), range(5)):
            new_y = y + i * len(grid)
            new_x = x + j * len(grid[y])
            new_grid[new_y][new_x] = grid[y][x] + i + j
            if new_grid[new_y][new_x] > 9:
                new_grid[new_y][new_x] = new_grid[new_y][new_x] - 9 

min_cost = djikstra(new_grid)
print(min_cost)