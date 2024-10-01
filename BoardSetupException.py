class BoardSetupException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"BoardSetupException, {self.message}"
        else:
            return "BoardSetupException, Ошибка взаимодействия с полем"