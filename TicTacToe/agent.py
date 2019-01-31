import numpy as np

class agent:


    def __init__(self, eps=0.1, alpha=0.5):
        self.eps = eps
        self.alpha = alpha
        self.verbose = False
        self.stateHistory = []

    def setV(self, V):
        self.V = V

    def setSymbol(self, sym):
        self.sym = sym

    def resetHistory(self):
        self.stateHistory = []

    def takeAction(self, env):
        r = np.random.rand()
        if r < self.eps:
            move = self.getRandomAction(env.board)
            env.board[move] = self.sym
        else:
            move = self.getBestMove(env)
            env.board[move] = self.sym

    def updateStateHistory(self, state):
        self.stateHistory.append(state)

    def update(self, env):
        reward = env.reward(self.sym)
        target = reward
        for state in reversed(self.stateHistory):
            self.V[state] = self.V[state] + (self.alpha * (target - self.V[state]))
            target = self.V[state]

    def getRandomAction(self, board):
        possibleSpots = []
        for i in range(len(board)):
            if board[i] == 0:
                possibleSpots.append(i)

        choice = np.random.choice(len(possibleSpots))
        return possibleSpots[choice]

    def getBestMove(self, env):
        bestValue = -1
        bestState = None
        move = None
        for i in range(len(env.board)):
            if env.board[i] == 0:
                env.board[i] = self.sym
                state = env.getState()
                env.board[i] = 0
                if self.V[state] > bestValue:
                    bestValue = self.V[state]
                    bestState = state
                    move = i

        return move







