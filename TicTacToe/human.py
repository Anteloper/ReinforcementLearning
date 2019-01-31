
class human:
    def __init__(self):
        pass

    def setSymbol(self, sym):
        self.sym = sym

    def takeAction(self, env):
        while True:
            move = int(raw_input("Enter index of your next move, 0-8: "))
            if env.isEmpty(move):
                env.board[move] = self.sym
                return
            else:
                print("Move already taken")

    def update(self, env):
        pass

    def updateStateHistory(self, s):
        pass