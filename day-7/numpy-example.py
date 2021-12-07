import numpy as np
import math

arr = np.fromfile("input", dtype=int, sep=",")
median = np.median(arr)
cost = sum(abs(arr - median))
print(f"part 1: {cost}")


def tri(n):
    return n * (n + 1) // 2


mean = np.mean(arr)
cost = sum(tri(abs(arr - math.floor(mean))))
print(f"part 2: {cost}")
