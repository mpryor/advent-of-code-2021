from itertools import *

t = 0

lines = open("input").readlines()

for k in lines:
    a, b = k.split(" | ")
    do = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
          "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    req = set(do)
    for x in permutations("abcdefg"):
        m = dict(zip(x, "abcdefg"))
        r = set("".join(sorted(map(m.get, q))) for q in a.split())
        if r == req:
            b = ["".join(sorted(map(m.get, q))) for q in b.split()]
            b = "".join(str(do.index(q)) for q in b)
            t += int(b)
            break

print(t)
