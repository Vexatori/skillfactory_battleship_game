from Dot import Dot


class Ship:
    def __init__(self, length: int, dot: (Dot, tuple), direction: str):
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
        if not isinstance(length, int):
            raise TypeError("Длина корабля должна быть числом")
        if not isinstance(dot, Dot) and not isinstance(dot, tuple):
            raise TypeError("Начальная точка корабля должна быть точкой (Dot) или кортежем")
        if not isinstance(direction, str) or direction not in ['h', 'v']:
            raise ValueError("Направление корабля должно задаваться символами h - горизонтальное, или v - вертикальное")
        self.__ship_length = length
        self.__ship_health = length
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
        return [Dot(dot.x + (0 if self.__ship_direction == 'h' else i), dot.y + (0 if self.__ship_direction == 'v' else i)) for i in
                range(self.length)]

    def decrease_health(self):
        self.__ship_health -= 1
