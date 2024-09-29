from Ship import Ship


class Board:
    def __init__(self):
        self.board_cells = [
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF'],
            ['\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF', '\u25EF']
        ]
        self.ships = []
        self.__hid = True
        self.ships_alive = 0

    @property
    def hidden(self):
        return self.__hid

    @hidden.setter
    def hidden(self, is_hidden: bool):
        if not isinstance(is_hidden, bool):
            raise ValueError("Значение видимости кораблей на доске должно быть булевым")
        self.__hid = is_hidden

    def add_ship(self, ship):
        if len(self.ships) == 7:
            raise ValueError("На доске нет места для кораблей, уже резмещено максимальное количество")
        if ship.length == 3 and len([s for s in self.ships if s.length == 3]) == 1:
            raise ValueError("На доске уже есть корабль длинной в 3 клетки, вы не можете поставить еще один")
        if ship.length == 2 and len([s for s in self.ships if s.length == 2]) == 2:
            raise ValueError("На доске уже есть два корабля длинной в 2 клетки, вы не можете поставить больше")
        if ship.length == 1 and len([s for s in self.ships if s.length == 2]) == 4:
            raise ValueError("На доске уже есть четыре корабля длинной в 1 клетку, вы не можете поставить больше")
        if not self.cells_available(ship):
            raise ValueError("Нельзя поставить корабль на указанные клетки.")
        if not 0 <= ship.starting_point.x <= 5 or not 0 <= ship.starting_point.y <= 5:
            raise ValueError("Начальная точка корабля находится за пределами доски")
        for dot in ship.dots:
            self.board_cells[dot.x][dot.y] = '\u25A0'
        self.ships.append(ship)

    def cells_available(self, ship):
        board_cells = []
        ship_dots_cords = []
        for dot in ship.dots:
            i, j = dot.x, dot.y
            ship_dots_cords.append(i)
            ship_dots_cords.append(j)
            for i in [i for i in range(i - 1, i + 2) if 0 <= i <= 5]:
                for j in [j for j in range(j - 1, j + 2) if 0 <= j <= 5]:
                    board_cells.append(self.board_cells[i][j])
        return all([cell == '\u25EF' for cell in board_cells]) and all([0 <= c <= 5 for c in ship_dots_cords])

    def print_board(self):
        for row in self.board_cells:
            # board_cells.append(['\u25EF' if self.__hid and elem == '\u25A0' else elem for elem in row])
            print("|".join(['\u25EF' if self.__hid and elem == '\u25A0' else elem for elem in row]))


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
    board.print_board()
