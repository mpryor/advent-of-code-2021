from collections import Counter
with open("input") as input_file:
    input_line, rules = input_file.read().split("\n\n")
    rules = rules.split("\n")
    rules = [rule.split(" -> ") for rule in rules]
    rules = {r: c for r,c in rules}

    for _ in range(40):
        new_line = ""
        for i in range(len(input_line) - 1):
            pair = input_line[i:i+2]
            insert_char = rules[pair]
            new_line += pair[0:1] + insert_char
            if i == len(input_line) - 2:
                new_line += pair[1]
        input_line = new_line

    counts = Counter(input_line).values()
    print(max(counts) - min(counts))