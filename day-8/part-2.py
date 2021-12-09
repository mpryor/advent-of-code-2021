from collections import Counter
import itertools


#         _1__
#      2 |    | 3
#        |_4__|
#      5 |    | 6
#        |_7__|
segment_decode_map = {
    0: [1, 2, 3, 5, 6, 7],
    1: [3, 6],
    2: [1, 3, 4, 5, 7],
    3: [1, 3, 4, 6, 7],
    4: [2, 3, 4, 6],
    5: [1, 2, 4, 6, 7],
    6: [1, 2, 4, 5, 6, 7],
    7: [1, 3, 6],
    8: [1, 2, 3, 4, 5, 6, 7],
    9: [1, 2, 3, 4, 6, 7]
}


def segment_decoder(code, segment_map):
    lit_segments = []
    for char in code:
        lit_segments.append(segment_map[char])
    lit_segments.sort()

    for k, v in segment_decode_map.items():
        if lit_segments == v:
            return k

    return None


def get_perms(possibilities):
    perms = []
    res = itertools.product(*possibilities.values())
    for prod in res:
        dups = max([y for x, y in Counter(prod).items()])
        if dups < 2:
            map = {}
            for i, key in enumerate(possibilities.keys()):
                map[key] = prod[i]
            perms.append(map)
    return perms


def decode(entries):
    decoded_entries = {}

    entries_map = {}
    for entry in entries:
        entry_len = len(entry)
        if entry_len in entries_map:
            entries_map[entry_len].append(entry)
        else:
            entries_map[entry_len] = [entry]

    two_char_entry = entries_map[2][0]
    for char in two_char_entry:
        decoded_entries[char] = [3, 6]

    three_char_entry = entries_map[3][0]
    for char in three_char_entry:
        if char not in decoded_entries:
            decoded_entries[char] = [1]

    four_char_entry = entries_map[4][0]
    for char in four_char_entry:
        if char not in decoded_entries:
            decoded_entries[char] = [2, 4]

    for char in range(ord("a"), ord("g") + 1):
        char = chr(char)
        if char not in decoded_entries:
            decoded_entries[char] = [5, 7]

    working_maps = []
    five_char_entries = entries_map[5]
    for decode_map in get_perms(decoded_entries):
        for code in five_char_entries:
            res = segment_decoder(code, decode_map)
            if res == None:
                break
        if res != None:
            working_maps.append(decode_map)
    return working_maps[0]


with open("input") as input_file:
    total = 0
    for line in input_file:
        entries, segments = line.split("|")
        entries = entries.strip().split(" ")

        segment_map = decode(entries)
        segments = segments.strip().split(" ")

        number = ""
        for segment in segments:
            res = segment_decoder(segment, segment_map)
            number += str(res)

        total += int(number)
    print(total)
