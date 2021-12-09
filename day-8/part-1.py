num_segments = [6, 2,  5, 5, 4,  5, 6, 3,  7,  6]
#               0  1*  2  3  4*  5  6  7*  8*  9

# dab = 7 -> d is top, a-b are right segments
# ab = 1
# eafb = 4

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

with open("input") as input_file:
    displays = []
    total = 0
    for line in input_file:
        entries, output = line.split("|")
        entries = entries.strip().split(" ")
        output = output.strip().split(" ")
        for out in output:
            if len(out) in [2, 3, 4, 7]:
                total += 1
    print(total)
