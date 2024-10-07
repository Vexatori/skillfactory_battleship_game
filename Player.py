from Board import Board
from BoardOutException import BoardOutException
from BoardSetupException import BoardSetupException


class Player:
    def __init__(self, board, foes_board):
        if not isinstance(board, Board) or not isinstance(foes_board, Board):
            raise TypeError("Доски игроков должны быть экземплярами Board")
        self.__players_board = board
        self.__foes_board = foes_board

    def ask(self):
        pass

    def move(self, shot_dot):
        nice_shot = None
        while True:
            try:
                nice_shot = self.__foes_board.shot(shot_dot)
            except (BoardOutException, BoardSetupException) as e:
                print(f"Неверный ход: {e.message}")
                return nice_shot
            else:
                break
        return nice_shot
        # nice_shot = True
        # shot_dot = None
        # while True:
        #     while (not shot_dot or len(shot_dot) < 2
        #            or not isinstance(shot_dot[0], int) or not isinstance(shot_dot[1], int) or nice_shot):
        #         if not shot_dot or len(shot_dot) < 2 or not isinstance(shot_dot[0], int):
        #             shot_str = "Необходимо ввести правильные координаты для хода: "
        #         else:
        #             shot_str = "Введите через пробел координаты хода: "
        #         shot_dot = str(input(f"{shot_str}")).split()
        #     try:
        #         nice_shot = self.__foes_board.shot(shot_dot)
        #         if not nice_shot:
        #             break
        #     except (BoardOutException, BoardSetupException) as e:
        #         print(f"Неверный ход: {e.message}")
