from Dot import Dot


class Ship:
    def __init__(self, length: (int, str), dot: (Dot, tuple), direction: str):
        """
        Конструктор класса Ship
        Параметры
        ---------
        length : int
                длина корабля
        dot : Dot or tuple
                начальная точка корабля (его нос)
        direction : int
                направление корабля: h - горизонтальное, v - вертикальное
        """
        if isinstance(length, str) and not length.lstrip("-").isnumeric():
            raise TypeError("Длина корабля должна быть числом")
        if not isinstance(dot, Dot) and not isinstance(dot, tuple):
            raise TypeError("Начальная точка корабля должна быть точкой (Dot) или кортежем")
        if not isinstance(direction, str) or direction not in ['h', 'v']:
            raise ValueError("Направление корабля должно задаваться символами h - горизонтальное, или v - вертикальное")
        self.__ship_length = int(length)
        self.__ship_health = int(length)
        self.__ship_starting_point = dot if isinstance(dot, Dot) else Dot(dot[0], dot[1])
        self.__ship_direction = direction

    @property
    def length(self):
        return self.__ship_length

    @property
    def health(self):
        return self.__ship_health

    @property
    def starting_point(self):
        return self.__ship_starting_point

    @property
    def direction(self):
        return self.__ship_direction

    @property
    def dots(self):
        dot = self.__ship_starting_point
        sd = self.__ship_direction
        return [Dot(dot.x + (0 if sd == 'h' else i), dot.y + (0 if sd == 'v' else i)) for i in range(self.length)]

    def decrease_health(self):
        self.__ship_health -= 1

    def __str__(self):
        ship_dots = ", ".join([str(d) for d in self.dots])
        return f'Ship: length: {self.__ship_length}, health: {self.__ship_health}, ship_dots: {ship_dots}, direction: {self.__ship_direction}'
