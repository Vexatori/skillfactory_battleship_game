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
            raise TypeError("Направление корабля должно задаваться символами h - горизонтальное, или v - вертикальное")
        self.length = length
        self.health = length
        self.starting_point = dot if isinstance(dot, Dot) else Dot(dot[0], dot[1])
        self.direction = direction

    @property
    def dots(self):
        dot = self.starting_point
        return [Dot(dot.x + (0 if self.direction == 'h' else i), dot.y + (0 if self.direction == 'v' else i)) for i in
                range(self.length)]
