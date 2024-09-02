class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


if __name__ == '__main__':
    p1 = Point(1, 2)
    print(p1.default_color)
    # red

    Point.default_color = "blue"
    print(Point.default_color)
    # blue