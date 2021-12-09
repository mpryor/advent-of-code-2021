s = 0
for x, y in [x.split('|') for x in open('input')]:  # split signal and output
    l = {len(s): set(s) for s in x.split()}    # get number of segments

    n = ''
    for o in map(set, y.split()):              # loop over output digits
        olen = len(o)
        four_len = o & l[4]
        two_len = o & l[2]
        if olen == 2:
            n += '1'
        elif olen == 3:
            n += '7'
        elif olen == 4:
            n += '4'
        elif olen == 7:
            n += '8'
        elif olen == 5 and four_len == 2:
            n += '2'
        elif olen == 5 and four_len == 3 and two_len == 1:
            n += '5'
        elif olen == 5 and four_len == 3 and two_len == 2:
            n += '3'
        elif olen == 6 and four_len == 4:
            n += '9'
        elif olen == 6 and four_len == 3 and two_len == 1:
            n += '6'
        elif olen == 6 and four_len == 3 and two_len == 2:
            n += '0'
    s += int(n)
