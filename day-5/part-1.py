class Point:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class Line:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        my_str = ""
        my_str += f"Point 1: {self.p1.x},{self.p1.y}" + "\n"
        my_str += f"Point 2: {self.p2.x},{self.p2.y}"
        return my_str

    def is_not_diagonal(self):
        return (self.p1.x == self.p2.x) or (self.p1.y == self.p2.y)

    def get_path(self):
        x_diff = self.p2.x - self.p1.x
        y_diff = self.p2.y - self.p1.y

        if x_diff == 0:
            x_vector = 0
            y_vector = 1 if y_diff > 0 else -1
        elif y_diff == 0:
            x_vector = 1 if x_diff > 0 else -1
            y_vector = 0

        curr_point = self.p1
        points = [Point(curr_point.x, curr_point.y)]
        while curr_point != self.p2:
            curr_point.x += x_vector
            curr_point.y += y_vector
            points.append(Point(curr_point.x, curr_point.y))
        return points


def main():
    with open("input") as input_file:
        lines = []
        for str_line in input_file:
            str_line = str_line.replace(" ", "").replace("\n", "").split("->")
            points = []
            for point in str_line:
                x, y = point.split(",")
                points.append(Point(x, y))
            p1, p2 = points
            lines.append(Line(p1, p2))

    all_points = []

    for line in lines:
        if line.is_not_diagonal():
            points = line.get_path()
            all_points += points

    grid = [[0 for i in range(1000)] for j in range(1000)]

    for point in all_points:
        grid[point.y][point.x] += 1

    danger = 0
    for row in grid:
        for column in row:
            if column >= 2:
                danger += 1
    print(danger)


if __name__ == "__main__":
    main()
