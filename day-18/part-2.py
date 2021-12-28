import math
import json

def explode(l):
    list_str = str(l)
    nested_count = 0
    exploding_list_str = ""
    exploding_list_range = []
    prev_int_range = []
    reset = False

    for i, char in enumerate(list_str):
        if ord(char) in range(ord("0"), ord("9") + 1) and len(exploding_list_str) == 0:
            if reset:
                prev_int_range = []
                reset = False
            prev_int_range.append(i)
        else:
            reset = True

        if char == "[":
            if nested_count >= 5 and len(exploding_list_str) > 0:
                exploding_list_range = []
                exploding_list_str = ""
            nested_count += 1

        if nested_count >= 5 and list_str[i + 1] != "[":
            exploding_list_str += char
            exploding_list_range.append(i)

        if char == "]":
            if len(exploding_list_str) > 0:
                prev_int = ""
                for index in prev_int_range:
                    prev_int += list_str[index]

                exploding_list = json.loads(exploding_list_str)
                
                if len(prev_int) > 0:
                    prev_int = int(prev_int)
                    prev_int += exploding_list[0]
                else:
                    prev_int = None

                next_int_str = ""
                next_int_range = []
                j = i
                while j < len(list_str):
                    if ord(list_str[j]) in range(ord("0"), ord("9") + 1):
                        next_int_range.append(j)
                        next_int_str += list_str[j]
                    elif len(next_int_str) > 0:
                        break
                    j += 1

                if len(next_int_str) > 0:
                    next_int = int(next_int_str)
                    next_int += exploding_list[1]
                else:
                    next_int = None

                start = ""
                if prev_int == None:
                    start = list_str[0:exploding_list_range[0]]
                else: 
                    start = list_str[0:prev_int_range[0]] + str(prev_int) + list_str[prev_int_range[-1] + 1:exploding_list_range[0]]

                end = ""
                if next_int == None:
                    end = list_str[exploding_list_range[-1] + 1:]
                else:
                    end = list_str[exploding_list_range[-1] + 1:next_int_range[0]] + str(next_int) + list_str[next_int_range[-1] + 1:]

                return start + "0" + end
            nested_count -= 1
    return False


def split(l):
    list_str = str(l)
    split_str = ""
    split_indexes = []
    for i, char in enumerate(list_str):
        if char not in ["[", "]", ",", " "]:
            split_str += char
            split_indexes.append(i)
        else:
            if len(split_str) > 0 and int(split_str) >= 10:
                split_int = int(split_str)
                new_split = [math.floor(split_int / 2), math.ceil(split_int / 2)]
                return list_str[0:split_indexes[0]] + str(new_split) + list_str[split_indexes[1] + 1:]
            split_str = ""
            split_indexes = []
    return False


def reduce(l):
    change = True
    l = str(l)
    while change:
        if change := explode(l):
            l = change
        else:
            if change := split(l):
                l = change
    return json.loads(l)


def get_magnitude(row):
    l = row[0]
    r = row[1]
    l_mag = 0
    r_mag = 0
    if type(l) == type([]):
        l_mag = get_magnitude(l) * 3
    else:
        l_mag = l * 3
    
    if type(r) == type([]):
        r_mag = get_magnitude(r) * 2
    else:
        r_mag = r * 2

    return l_mag + r_mag


with open("sample") as input_file:
    rows = [json.loads(row.strip()) for row in input_file.readlines()]
    sums = []
    for i, irow in enumerate(rows):
        for j, jrow in enumerate(rows):
            if i != j:
                sums.append([irow, jrow])
    
    max_mag = 0
    for sum in sums:
        reduced = reduce(sum)
        mag = get_magnitude(reduced)
        if mag > max_mag:
            max_mag = mag

    print(max_mag)