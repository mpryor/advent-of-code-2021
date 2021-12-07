with open("input") as file:
    l = [int(i) for i in file.read().split(",")]

l.sort()
mid = l[len(l) // 2]
out = sum(abs(x - mid) for x in l)
