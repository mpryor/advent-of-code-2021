with open("input") as file:
    d = list(file.read().split(","))

f = list(map(d.count, '012345678'))

for _ in range(256):
    f = f[1:] + f[:1]
    f[6] += f[-1]

print(sum(f))
