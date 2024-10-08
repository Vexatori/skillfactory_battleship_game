from Dot import Dot
from Player import Player


class User(Player):
    def ask(self):
        shot_dot = None
        shot_str = "Необходимо ввести через пробел правильные координаты (два числа через пробел) для хода: "
        while True:
            if (not shot_dot or len(shot_dot) != 2
                    or not shot_dot[0].isnumeric() or not shot_dot[1].isnumeric()):
                shot_dot = str(input(f"{shot_str}")).split()
            else:
                break
        return Dot(int(shot_dot[0]) - 1, int(shot_dot[1]) - 1)
