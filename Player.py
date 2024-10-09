from Board import Board
from BoardOutException import BoardOutException
from BoardSetupException import BoardSetupException


class Player:
    def __init__(self, board, foes_board):
        if not isinstance(board, Board) and not isinstance(foes_board, Board):
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
            except (BoardOutException, BoardSetupException, TypeError):
                return nice_shot
            else:
                break
        return nice_shot
