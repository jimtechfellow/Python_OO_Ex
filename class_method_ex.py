class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")

    @classmethod
    def zero(cls):
        return cls(0, 0)

if __name__ == '__main__':
    point = Point.zero()
    print(point.x, point.y)
    # 0 0