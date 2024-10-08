from BoardOutException import BoardOutException
from BoardSetupException import BoardSetupException
from Dot import Dot
from Player import Player
from random import randint


class AI(Player):
    def ask(self):
        i = randint(0, 5)
        j = randint(0, 5)
        return Dot(i, j)
