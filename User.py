from Dot import Dot
from Player import Player


class User(Player):
    def __move_decorator(func):
        def wrapper(*args, **kwargs):
            nice_shot = func(*args, **kwargs)
            if nice_shot is None:
                print("Неверный ход, вы попали в уже подбитую клетку или задали неверные координаты. "
                      "Попробуйте еще раз.")
            return nice_shot
        return wrapper

    # Декоратор для того, чтобы предупреждать пользователя о неверном ходе. Для ИИ такого ненужно.
    @__move_decorator
    def move(self, shot_dot):
        return super().move(shot_dot)

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
