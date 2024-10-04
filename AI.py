from Dot import Dot
from Player import Player
from random import randint


class AI(Player):
    def ask(self):
        i = randint(0, 6)
        j = randint(0, 6)
        return Dot(i, j)
