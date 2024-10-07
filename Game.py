from Board import Board
from AI import AI
from BoardSetupException import BoardSetupException
from Dot import Dot
from Ship import Ship
from User import User
from random import choice, randint


class Game:
    def __init__(self):
        self.players_board = None
        self.ai_board = None
        self.player = None
        self.ai = None

    @staticmethod
    def random_board():
        new_board = Board()
        ships = [3, 2, 2, 1, 1, 1, 1]
        try_count = 0
        while len(new_board.ships_on_board) != 7:
            for ship in ships:
                while try_count < 100:
                    try_count += 1
                    direction = choice(['v', 'h'])
                    ship_dot = Dot(randint(0, 6), randint(0, 6))
                    new_ship = Ship(ship, ship_dot, direction)
                    try:
                        new_board.add_ship(new_ship)
                    except BoardSetupException:
                        continue
                    else:
                        break
                if try_count >= 100:
                    break
            if len(new_board.ships_on_board) != 7 and try_count >= 100:
                try_count = 0
                new_board = Board()
        return new_board

    @staticmethod
    def greet():
        print("""\
        Привет!
        Тебя приветствует реализация игры "Морской бой" от Суюнова Александра.
        Прежде чем начать играть, ознакомься, пожалуйста, с правилами игры:
        1. Чтобы заполнить доску, необходимо расставить 7 кораблей: один с 3 жизнями, два с 2 и четыре с 1.
        Также вы можете заполнить доску рандомно, если вас "ломает" самому ее заполнять)))
        2. Вначале игры вас попросят расставить их, указав: длину, начальную точку (нос корабля) и его направление 
        (куда нужно отрисовать его: горизонтально или вертикально).
        Значения указываются через пробел. Длина и начальная точка (номер строки и столбца) должны быть числами.
        А направление должно быть одним из значений: "v" или "h", вертикальное и горизонтальное, соответственно.
        Пример: 3 1 2 v - поставить верткально корабль длинной в 3 клетки на первую строку во второй столбец.
        Не бойтесь ошибиться, игра предупредит вас, если что-то пойдет не так.
        3. Координаты хода также должны быть числами, указанными через пробел.
        4. Если вы удачно подбили корабль противника, то вам будет предложено походить еще раз.
        5. Игра продолжается до тех пор, пока у кого-нибудь не останется ни одного корабля.\n
        Удачной игры!\n\n
        """)

    def __loop(self):
        while self.players_board.ships_alive_on_board != 0 or self.ai_board.ships_alive_on_board != 0:
            players_move = None
            players_shot = None
            while players_shot is None or players_shot:
                players_move = self.player.ask()
                players_shot = self.player.move(players_move)
            ai_move = None
            ai_shot = None
            while ai_shot is None or ai_shot:
                ai_move = self.ai.ask()
                ai_shot = self.ai.move(ai_move)
        return "Победа Игрока!" if self.ai_board.ships_alive_on_board == 0 else "Победа ИИ! Стыдно, мешок с костями..."

    def start(self):
        Game.greet()
        self.ai_board = Game.random_board()
        players_board_variant = None
        while players_board_variant not in [1, 2]:
            players_board_variant = input("Игрок, введите 1 или 2 для ручного или автоматического создания доски: ")
            players_board_variant = None if not players_board_variant.isnumeric() else int(players_board_variant)
        self.players_board = Board() if players_board_variant == 1 else Game.random_board()
        self.players_board.hidden = False
        if players_board_variant == 1:
            while len(self.players_board.ships_on_board) != 7:
                try:
                    new_ship = None
                    while new_ship is None or len(str(new_ship).split()) < 4:
                        new_ship = str(input("Введите значения через пробел для создания нового корабля, как было "
                                             "сказано в инструкции ранее: ")).split()
                        if len(str(new_ship).split()) < 4:
                            print("Нужно 4 значения, чтобы создать корабль, проверьте данные и повторите ввод")
                    new_ship = Ship(new_ship[0], (new_ship[1], new_ship[2]), new_ship[3])
                    self.players_board.add_ship(new_ship)
                except (BoardSetupException, ValueError, TypeError) as e:
                    print(f"Ошибка создания корабля: {e}")
                else:
                    self.players_board.print_board()
        self.ai = AI(self.ai_board, self.players_board)
        self.player = User(self.players_board, self.ai_board)
        print(self.__loop())


if __name__ == '__main__':
    # board = Game.random_board()
    # board.hidden = False
    # board.print_board()
    new_game = Game()
    new_game.start()

# ■|◯|■|◯|■|◯
# ■|◯|◯|◯|◯|◯
# ■|◯|■|◯|◯|◯
# ◯|◯|■|◯|◯|■
# ■|■|◯|◯|◯|◯
# ◯|◯|◯|■|◯|◯
