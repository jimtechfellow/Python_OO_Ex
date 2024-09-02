class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


if __name__ == '__main__':
    p1 = Point(1,2)
    print(type(p1))
    print(isinstance(p1, Point))
    # <class '__main__.Point'>
    # True


    p1.draw()
    # Point (1,2)


    print(p1.x, p1.y)
    # 1 2

