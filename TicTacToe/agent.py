from __future__ import print_function
import numpy as np

class agent:
    def __init__(self, eps=0.1, alpha=0.5):
        self.eps = eps
        self.alpha = alpha
        self.verbose = False
        self.stateHistory = []

    def setV(self, V):
        self.V = V

    def setVerbose(self, verbose):
        self.verbose = verbose

    def setSymbol(self, sym):
        self.sym = sym

    def resetHistory(self):
        self.stateHistory = []

    def takeAction(self, env):
        r = np.random.rand()
        if r < self.eps:
            if(self.verbose):
                print("Taking random action")
            move = self.getRandomAction(env.board)
            env.playMove(move, self.sym)
        else:
            if(self.verbose):
                print("Taking best action")
            move = self.getBestMove(env)
            env.playMove(move, self.sym)

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
        valueMap = {}
        for i in range(len(env.board)):
            if env.isEmpty(i):
                env.playMove(i, self.sym)
                state = env.getState()
                valueMap[i] = self.V[state]
                env.playMove(i, 0)
                if self.V[state] > bestValue:
                    bestValue = self.V[state]
                    bestState = state
                    move = i
        if(self.verbose):
            self.valueMapDisplay(env, valueMap)
        return move


    def valueMapDisplay(self, env, valueMap):
        for i in range(0, 7, 3):
            print("\n---------------------------")
            for j in range(3):
                if env.isEmpty(i+j):
                    # print the value
                    print(str(round(valueMap[i+j], 2)) + "  |", end="  ")
                else:
                    if env.board[i+j] == env.x:
                        print("x  |", end="  ")
                    elif env.board[i+j] == env.o:
                        print("o  |", end="  ")
                    else:
                        print("   |", end="  ")
        print("\n\n")
