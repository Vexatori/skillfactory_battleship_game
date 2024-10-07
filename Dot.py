class Dot:
    def __init__(self, x: (str, int), y: (str, int)):
        if ((isinstance(x, str) and not x.lstrip("-").isnumeric())
                or (isinstance(y, str) and not y.lstrip("-").isnumeric())):
            raise TypeError("Координаты точки должны быть числом")
        # если ввод точки был ручной, то делаем -1 у точки, т.к человек вводит числа не как компуктер) у него индексы
        # с 1 начинаются
        self.__x_cor = int(x) + (-1 if isinstance(x, str) else 0)
        self.__y_cor = int(y) + (-1 if isinstance(y, str) else 0)

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
