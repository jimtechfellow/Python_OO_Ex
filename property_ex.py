class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be greater than or equal to 0")
        self.__price = value


if __name__ == '__main__':
    p = Product(-29)
    print(p.price)

    # ValueError: Price must be greater than or equal to 0
