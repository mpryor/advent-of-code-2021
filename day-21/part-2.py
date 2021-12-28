dice_rolls = 0
dice_val = 1
p1_pos, p2_pos = 4, 9
p1_score, p2_score = 0, 0

def p2_roll(val, p1_pos, p2_pos, p1_score, p2_score):
    pass

def p1_roll(val, p1_pos, p2_pos, p1_score, p2_score):
    p1_pos += val
    if p1_pos > 10:
        p1_pos = p1_pos % 10
    if p1_pos == 0:
        p1_pos = 1

    p1_score += p1_pos

    if val == 3:
        p2_roll(1)

p1_roll(1)
p1_roll(2)
p1_roll(3)

print(min(p1_score, p2_score) * dice_rolls)