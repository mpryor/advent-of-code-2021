y_range = [-159, -121]
max_y = 0

for y_velocity in range(1,1000):
    y = 0
    max_y_this_range = 0
    while y >= y_range[0] or y_velocity >= 0:
        if y > max_y_this_range:
            max_y_this_range = y
        hit = y_range[0] <= y <= y_range[1] 
        if hit:
            if max_y_this_range > max_y:
                max_y = max_y_this_range
        y += y_velocity
        y_velocity -= 1

print(max_y)