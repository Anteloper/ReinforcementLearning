
class human:
    def __init__(self):
        pass

    def setSymbol(self, sym):
        self.sym = sym

    def takeAction(self, env):
        while True:
            move = raw_input("Enter index of your next move, 0-8")
            if(env.isEmpty(move)== 0):
                env.board[move] = self.sym
            print("Move already taken")

    def update(self, env):
        pass

    def update_state_history(self, s):
        pass