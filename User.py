from Player import Player


class User(Player):
    def ask(self):
        shot_dot = None
        shot_str = "Необходимо ввести через пробел правильные координаты для хода: "
        while (not shot_dot or len(shot_dot) < 2
               or not isinstance(shot_dot[0], int) or not isinstance(shot_dot[1], int)):
            shot_dot = str(input(f"{shot_str}")).split()
        return shot_dot
