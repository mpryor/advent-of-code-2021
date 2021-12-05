#!/bin/python3


def init_grid(grid_length, grid_width):
    grid = []
    for i in range(0, grid_length):
        row = []
        for j in range(0, grid_width):
            row.append(0)
        grid.append(row)
    return grid


def build_grid_from_strings(bit_strings):
    grid = None
    for i, bit_string in enumerate(bit_strings):
        if grid == None:
            grid = init_grid(len(bit_strings), len(bit_string))

        for j, bit in enumerate(bit_string):
            grid[i][j] = bit
    return grid


def calc_co2_scrubber_rating(initial_grid):
    grid = list(initial_grid)

    for j in range(0, len(grid[0])):
        if len(grid) == 1:
            return grid[0]

        sum = 0
        for i in range(0, len(grid)):
            row = grid[i]
            target_bit = row[j]
            sum += int(target_bit)

        if sum >= (len(grid) / 2):
            lcb = 0
        else:
            lcb = 1

        indexes_to_pop = []
        for i in range(0, len(grid)):
            row = grid[i]
            if int(row[j]) != lcb:
                indexes_to_pop.append(i)

        for index in indexes_to_pop[::-1]:
            grid.pop(index)

    return grid[0]


def calc_oxygen_generator_rating(initial_grid):
    grid = list(initial_grid)

    for j in range(0, len(grid[0])):
        sum = 0
        for i in range(0, len(grid)):
            row = grid[i]
            target_bit = row[j]
            sum += int(target_bit)

        if sum >= (len(grid) / 2):
            mcb = 1
        else:
            mcb = 0

        indexes_to_pop = []
        for i in range(0, len(grid)):
            row = grid[i]
            if int(row[j]) != mcb:
                indexes_to_pop.append(i)

        for index in indexes_to_pop[::-1]:
            grid.pop(index)

    return grid[0]


def binary_array_to_int(bin_array):
    total = 0
    for i, bit in enumerate(bin_array[len(bin_array)-1::-1]):
        total += (pow(2, i) * int(bit))

    return total


def main():
    with open("input") as input_file:
        bit_strings = input_file.read().split("\n")

    grid = build_grid_from_strings(bit_strings)
    oxygen_rating = calc_oxygen_generator_rating(grid)
    oxygen_rating_decoded = binary_array_to_int(oxygen_rating)

    co2_scrubber_rating = calc_co2_scrubber_rating(grid)
    co2_scrubber_decoded = binary_array_to_int(co2_scrubber_rating)

    print(oxygen_rating_decoded)
    print(co2_scrubber_decoded)
    print(oxygen_rating_decoded * co2_scrubber_decoded)


if __name__ == "__main__":
    main()
