from copy import copy
from collections import Counter, defaultdict

with open("input") as input_file:
    input_line, rules = input_file.read().split("\n\n")
    rules = rules.split("\n")
    rules = [rule.split(" -> ") for rule in rules]
    rules = {r: c for r,c in rules}

    pairs = defaultdict(int)
    chars = defaultdict(int)

    for i in range(len(input_line) - 1):
        pair = input_line[i:i+2]
        pairs[pair] += 1
    
    for char in input_line:
        chars[char] += 1
    
    for _ in range(40):
        new_pairs = copy(pairs)
        for pair, count in pairs.items():
            insert_char = rules[pair]
            chars[insert_char] += 1 * count
            pair_one = pair[0] + insert_char
            pair_two = insert_char + pair[1]
            new_pairs[pair_one] += 1 * count
            new_pairs[pair_two] += 1 * count
            new_pairs[pair] -= 1 * count
        pairs = new_pairs
 
    max_chars = max(*[chars.values()])
    min_chars = min(*[chars.values()])
    print(max_chars - min_chars)