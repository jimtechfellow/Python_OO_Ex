from class_method_ex import Point


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

if __name__ == '__main__':

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1 == p2)
    # True

    p3 = Point(3, 10)
    print(p1 > p3)
    # False