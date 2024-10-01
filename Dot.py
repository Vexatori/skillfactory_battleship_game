class Dot:
    def __init__(self, x: int, y: int):
        if not isinstance(x, int) and not isinstance(y, int):
            raise TypeError("Координаты точки должны быть числом")
        self.__x_cor = x
        self.__y_cor = y

    @property
    def x(self):
        return self.__x_cor

    @property
    def y(self):
        return self.__y_cor

    def __eq__(self, other):
        if not isinstance(other, Dot):
            raise TypeError("Сравнивать точку можно только с точкой")
        return self.__x_cor == other.x and self.__y_cor == other.y

    def __str__(self):
        return f"Dot: ({self.__x_cor}, {self.__y_cor})"
