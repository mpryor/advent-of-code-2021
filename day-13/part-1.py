#   0 1 2 3 4
# 0 X - - - X  
# 1 - - - - -    
# 2 - X 
# 3   x
# 4
#
# Fold along x = 2

with open("input") as input_file:
    points = []
    for line in input_file:
        if "fold" not in line and line != "\n":
            x,y = line.strip().split(",")
            points.append((int(x),int(y)))

def fold_y(points, y_fold):
    for i, (x,y) in enumerate(points):
        if y > y_fold:
            y = y - y_fold
            y = y_fold - y
        points[i] = x,y
    return list(set(points))

def fold_x(points, x_fold):
    for i, (x,y) in enumerate(points):
        if x > x_fold:
            x = x - x_fold
            x = x_fold - x
        points[i] = x,y
    return list(set(points))

points = fold_x(points, 655)
print(len(points))