from collections import deque

chunk_chars = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

openers_count = {
    "[": 0,
    "(": 0,
    "{": 0,
    "<": 0
}

char_stack = deque()
scores = []

with open("input") as input_file:
    lines = input_file.readlines()

    for line in lines:
        missing_closers = deque()
        is_corrupt = False
        line = line.strip()

        for char in line:
            if not is_corrupt:
                for opener, closer in chunk_chars.items():
                    if char == opener:
                        char_stack.append(char)
                        missing_closers.append(closer)
                    elif char == closer:
                        missing_closers.pop()
                        last_opener = char_stack.pop()
                        if last_opener != opener:
                            is_corrupt = True

        total = 0
        if not is_corrupt:
            while len(missing_closers) > 0:
                last_val = missing_closers.pop()
                total *= 5
                total += points[last_val]
        if total != 0:
            scores.append(total)

scores.sort()
print(scores[len(scores) // 2])
