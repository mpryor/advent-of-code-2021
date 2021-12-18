#   0 1 2 3 4
# 0 X - - - X  
# 1 - - - - -    
# 2 - X 
# 3   x
# 4
#
# Fold along x = 2

def draw_points(points):
    max_x = max([x for x,y in points])
    max_y = max([y for x,y in points])
    rows = []
    for i in range(max_y + 1):
        row = []
        for j in range(max_x + 1):
            row.append("-")
        rows.append(row)
    
    for x,y in points:
        rows[y][x] = "X"

    for row in rows:
        row_str = ""
        for col in row:
            row_str += col
        print(row_str)


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

with open("input") as input_file:
    points = []
    for line in input_file:
        if "fold" in line:
            line = line.strip()
            axis, value = line.split(" ")[2].split("=")
            if axis == "x":
                points = fold_x(points, int(value))
            if axis == "y": 
                points = fold_y(points, int(value))
    
        if "fold" not in line and line != "\n":
            x,y = line.strip().split(",")
            points.append((int(x),int(y)))

print(len(points))
draw_points(points)