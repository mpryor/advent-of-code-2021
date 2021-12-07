from collections import Counter

with open("input") as input_file:
    fish = [int(f) for f in input_file.read().split(",")]
    fish_c = Counter(fish)
    no_of_days = 256
    while no_of_days > 0:
        for i in range(0, 9):
            l = i - 1
            if i == 0:
                new_fish = fish_c[i]
            else:
                fish_c[l] = fish_c[i]
        fish_c[6] += new_fish
        fish_c[8] = new_fish
        no_of_days -= 1
    total = sum([y for x, y in fish_c.items()])
    print(total)
