from Dot import Dot
from Player import Player


class User(Player):
    def ask(self):
        shot_dot = None
        shot_str = "Необходимо ввести через пробел правильные координаты для хода: "
        while True:
            shot_dot = str(input(f"{shot_str}")).split()
            if (not shot_dot or len(shot_dot) < 2
                    or not shot_dot[0].isnumeric() or not shot_dot[1].isnumeric()):
                print("Должно быть две координаты, и они должны быть числами, пожалуйста, проверьте данные.")
                shot_dot = str(input("Повторите ввод")).split()
            else:
                break
        return Dot(int(shot_dot[0]) - 1, int(shot_dot[1]) - 1)
