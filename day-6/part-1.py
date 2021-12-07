with open("input") as input_file:
    fish = input_file.read().split(",")
    fish = [int(f) for f in fish]

    no_of_days = 56
    while no_of_days > 0:
        new_fish = []
        for i in range(0, len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1
        fish += new_fish

        no_of_days -= 1
    print(len(fish))
