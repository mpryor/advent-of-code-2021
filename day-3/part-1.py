#!/bin/python3

with open("input") as input_file:
    bit_strings = input_file.readlines()

num_bits = len(bit_strings)

bit_counts = None
for bit_string in bit_strings:
    bit_string = bit_string.replace("\n", "")
    if bit_counts == None:
        bit_counts = [0] * len(bit_string)

    for i, bit in enumerate(bit_string):
        bit_counts[i] += int(bit)

gamma_rate_bits = []
epsilon_rate_bits = []

for i in bit_counts:
    if i > (num_bits / 2):
        gamma_rate_bits.append(1)
        epsilon_rate_bits.append(0)
    else:
        gamma_rate_bits.append(0)
        epsilon_rate_bits.append(1)


def binary_array_to_int(bin_array):
    total = 0
    for i, bit in enumerate(bin_array[len(bin_array)-1::-1]):
        total += (pow(2, i) * bit)

    return total


gamma_rate = binary_array_to_int(gamma_rate_bits)
epsilon_rate = binary_array_to_int(epsilon_rate_bits)
power = gamma_rate * epsilon_rate

print(f"{gamma_rate_bits}: {gamma_rate}")
print(f"{epsilon_rate_bits}: {epsilon_rate}")
print(f"power total: {power}")
