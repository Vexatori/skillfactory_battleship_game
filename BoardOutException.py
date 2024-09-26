class BoardOutException(Exception):
    def __init__(self, dot=None):
        if dot:
            self.message = f"Клетка ({dot.x}, {dot.y}) находится за пределами игрового поля"
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"BoardOutException, {self.message}"
        else:
            return "BoardOutException, Ошибка хода"
