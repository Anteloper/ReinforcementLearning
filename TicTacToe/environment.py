
class environment:
    def __init__(self, boardString="000000000"):
        self.board = []
        for i in boardString:
            self.board.append(int(i))
        self.x = 1
        self.o = 2
        self.winner = None
        self.ended = False
        self.isOver()

    def isEmpty(self, i):
        return self.board[i] == 0

    def reward(self, sym):
        if not self.ended:
            return 0
        return 1 if self.winner == sym else 0

    def getState(self):
        state = ""
        for i in self.board:
            state += str(i)
        return state

    def isOver(self):
        if "0" not in self.getState():
            self.ended = True

        self.checkAllWinningPaths(1)
        self.checkAllWinningPaths(2)
        return self.ended

    def playMove(self, index, symbol):
        self.board[index] = symbol

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
        aestheticBoard = []
        for i in self.board:
            if i == 0:
                aestheticBoard.append("_")
            elif i == 1:
                aestheticBoard.append("X")
            else:
                aestheticBoard.append("O")

        for i in range(0, 7, 3):
            print(str(aestheticBoard[i]) + " " + str(aestheticBoard[i+1]) + " " + str(aestheticBoard[i+2]))
        print("\n")
