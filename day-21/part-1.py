dice_rolls = 0
dice_val = 1
p1_pos, p2_pos = 4, 9
p1_score, p2_score = 0, 0

def roll_dice(ctr, val):
    rolls = []
    for _ in range(3):
        rolls.append(val)
        val += 1
        if val == 101:
            val = 1
    ctr += 3
    return sum(rolls), ctr, val


while True:
    forward, dice_rolls, dice_val = roll_dice(dice_rolls, dice_val)
    p1_pos += forward
    if p1_pos > 10:
        p1_pos = p1_pos % 10
        if p1_pos == 0:
            p1_pos = 10
    p1_score += p1_pos
    if p1_score >= 1000: break

    forward, dice_rolls, dice_val = roll_dice(dice_rolls, dice_val)
    p2_pos += forward
    if p2_pos > 10:
        p2_pos = p2_pos % 10
        if p2_pos == 0:
            p2_pos = 10
    p2_score += p2_pos
    if p2_score >= 1000: break

print(min(p1_score, p2_score) * dice_rolls)