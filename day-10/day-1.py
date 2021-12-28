from collections import deque

chunk_chars = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

openers_count = {
    "[": 0,
    "(": 0,
    "{": 0,
    "<": 0
}

char_stack = deque()

total = 0

with open("input") as input_file:
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        for char in line:
            for opener, closer in chunk_chars.items():
                if char == opener:
                    char_stack.append(char)
                elif char == closer:
                    last_opener = char_stack.pop()
                    if last_opener != opener:
                        total += points[char]
                        print(f"Found unexpected {closer}")
print(total)
