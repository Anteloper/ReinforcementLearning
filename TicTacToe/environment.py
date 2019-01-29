
class environment():
    def __init__(self):
        self.board = [0 for i in range(9)]
        self.x = 1
        self.o = 2
        self.winner = None
        self.ended = False

    def isEmpty(self, i):
        return self.board[i] == 0

    def reward(self, sym):
        if not self.ended:
            return 0
        return 1 if self.winner == sym else 0

    def getState(self):
        state = ""
        for i in self.board:
            state += str(self.board[i])
        return state

    def isOver(self):
        if not "0" in self.getState():
            return True

        self.checkAllWinningPaths(1)
        self.checkAllWinningPaths(0)
        return self.ended

    def checkAllWinningPaths(self, sym):
        #Check row winners
        for i in range(0, 7, 3):
            if(self.board[i] == sym and self.board[i+1] == sym and self.board[i+2]==sym):
                self.winner = sym
                self.ended = True
                return
        #Check column winners
        for i in range(3):
            if(self.board[i]==sym and self.board[i+3] == sym and self.board[i+6]==sym):
                self.winner = sym
                self.ended = True
                return

        #Check diagonals
        if (self.board[2] == sym and self.board[4] == sym and self.board[6] == sym):
            self.winner = sym
            self.ended = True
            return

        if(self.board[0] == sym and self.board[4] == sym and self.board[8] == sym):
            self.winner = sym
            self.ended = True
            return

    def drawBoard(self):
        for i in range(0, 7, 3):
            print(str(self.board[i]) + " " + str(self.board[i+1]) + " " + str(self.board[i+1]))

def main():
    e = environment()
    e.checkAllWinningPaths(1)
    e.drawBoard()

main()






