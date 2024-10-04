from BoardOutException import BoardOutException
from Ship import Ship
from Dot import Dot
from BoardSetupException import BoardSetupException


class Board:
    def __init__(self):
        self.__board_cells = [
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF']
        ]
        self.__ships = []
        self.__hid = True
        self.__ships_alive = 0

    @property
    def ships_on_board(self):
        return self.__ships

    @property
    def hidden(self):
        return self.__hid

    @hidden.setter
    def hidden(self, is_hidden: bool):
        if not isinstance(is_hidden, bool):
            raise TypeError("Значение видимости кораблей на доске должно быть булевым")
        self.__hid = is_hidden

    def out(self, dot: Dot):
        if not isinstance(dot, Dot):
            raise TypeError("Проверять выход за границы поля можно только у точек")
        return not 0 <= dot.x <= 5 or not 0 <= dot.y <= 5

    def add_ship(self, ship):
        if len(self.__ships) == 7:
            raise BoardSetupException("На доске нет места для кораблей, уже резмещено максимальное количество")
        if ship.length == 3 and len([s for s in self.__ships if s.length == 3]) == 1:
            raise BoardSetupException("На доске уже есть корабль длинной в 3 клетки, вы не можете поставить еще один")
        if ship.length == 2 and len([s for s in self.__ships if s.length == 2]) == 2:
            raise BoardSetupException("На доске уже есть два корабля длинной в 2 клетки, вы не можете поставить больше")
        if ship.length == 1 and len([s for s in self.__ships if s.length == 2]) == 4:
            raise BoardSetupException("На доске уже есть четыре корабля длинной в 1 клетку, вы не можете поставить \
                больше")
        if not self.__cells_available(ship):
            raise BoardSetupException("Нельзя поставить корабль на указанные клетки.")
        if self.out(ship.starting_point):
            raise BoardSetupException("Начальная точка корабля находится за пределами доски")
        for dot in ship.dots:
            self.__board_cells[dot.x][dot.y] = '\u25A0'
        self.__ships.append(ship)
        self.__ships_alive += 1

    def __cells_available(self, ship):
        __board_cells = []
        ship_dots_cords = []
        for dot in ship.dots:
            i, j = dot.x, dot.y
            ship_dots_cords.append(i)
            ship_dots_cords.append(j)
            for i in [i for i in range(i - 1, i + 2) if 0 <= i <= 5]:
                for j in [j for j in range(j - 1, j + 2) if 0 <= j <= 5]:
                    __board_cells.append(self.__board_cells[i][j])
        return all([cell == '\u25EF' for cell in __board_cells]) and all([0 <= c <= 5 for c in ship_dots_cords])

    def print_board(self):
        for row in self.__board_cells:
            print("|".join(['\u25EF' if self.__hid and elem == '\u25A0' else elem for elem in row]))

    def shot(self, dot: (Dot, tuple)):
        if not isinstance(dot, Dot) or not isinstance(dot, tuple):
            raise TypeError("Выстрел должен быть задан точкой или кортежем")
        shot_dot = dot if isinstance(dot, Dot) else Dot(dot[0], dot[1])
        if self.out(shot_dot):
            raise BoardOutException(shot_dot)
        if self.__board_cells[shot_dot.x][shot_dot.y] in ['X', 'T']:
            raise BoardSetupException("Нельзя выстрелить в уже подбитую точку")
        if len([s for s in self.__ships if shot_dot in s.dots]) > 1:
            self.__board_cells[shot_dot.x][shot_dot.y] = 'X'
            [s for s in self.__ships if shot_dot in s.dots][0].decrease_health()
            return True
        else:
            self.__board_cells[shot_dot.x][shot_dot.y] = 'T'
            return False


if __name__ == '__main__':
    # test_board = Board()
    # for r in test_board.board_condition:
    #     print("|".join(r))
    # print(list(range(-1, 2)))
    board = Board()
    board.hidden = False
    ship_1 = Ship(3, (0, 0), 'v')
    ship_2 = Ship(2, (4, 0), 'h')
    ship_3 = Ship(2, (0, 2), 'h')
    ship_4 = Ship(1, (0, 5), 'v')
    board.add_ship(ship_1)
    board.add_ship(ship_2)
    board.add_ship(ship_3)
    board.add_ship(ship_4)
    # board.print_board()
    some_dot = Dot(1, 0)
    ship_on_dot = [s for s in board.ships_on_board if some_dot in s.dots]
    print(*ship_on_dot[0].dots)
    # for s in board.ships_on_board:
    #     print(*s.dots)
