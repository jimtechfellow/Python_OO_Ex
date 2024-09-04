from class_method_ex import Point


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # gt= greater than means " >"
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


if __name__ == '__main__':

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1 == p2)
    # True

    p3 = Point(3, 10)
    print(p1 > p3)
    print(p1 < p3)
    # False
    # True

    p4 = p1+p3
    print(p4.x, p4.y)
    # 4 12
