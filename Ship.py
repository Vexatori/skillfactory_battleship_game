import Dot


class Ship:
    def __init__(self, length: int, dot: Dot, direction: int):
        """
        Конструктор класса Ship
        Параметры
        ---------
        length : int
                длина корабля
        dot : Dot or tuple
                начальная точка корабля (его нос)
        direction : int
                направление корабля: 1 - горизонтальное, 0 - вертикальное
        """
        if not isinstance(length, int):
            raise TypeError("Длина корабля должна быть числом")
        if not isinstance(dot, Dot) and not isinstance(dot, tuple):
            raise TypeError("Начальная точка корабля должна быть Dot")
        if not isinstance(direction, int):
            raise TypeError("Направление корабля должно задаваться числом")
        self.length = length
        self.health = length
        self.starting_point = dot
        self.direction = direction

    def dots(self):
        dot = self.starting_point
        return [Dot(dot.x + (0 if self.direction == 0 else i), dot.y + (0 if self.direction == 1 else i)) for i in
                range(self.length)]
