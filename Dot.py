class Dot:
    def __init__(self, x: int, y: int):
        if not isinstance(x, int) and not isinstance(y, int):
            raise TypeError("Координаты точки должны быть числом")
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Dot):
            raise TypeError("Сравнивать точку можно только с точкой")
        return self.x == other.x and self.y == other.y