from agent import agent
from environment import environment
from human import human

def playGame(p1, p2, env, draw=0):
    currentPlayer = None
    while not env.isOver():
        if currentPlayer == p1:
            currentPlayer = p2
        else:
            currentPlayer = p1

        if draw != 0:
            env.drawBoard()

        currentPlayer.takeAction(env)
        state = env.getState()
        p1.updateStateHistory(state)
        p2.updateStateHistory(state)

    if draw != 0:
        env.drawBoard()

    p1.update(env)
    p2.update(env)


def initializeV(allEnvironments, sym):
    V = {}
    for e in allEnvironments:
        if e.ended:
            if e.winner == sym:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[e.getState()] = v
    return V


def generateAllStates():
    allStates = ["0", "1", "2"]
    for j in range(8):
        tempStates = []
        size = len(allStates)
        for i in range(size):
            tempStates.append(allStates[i] + "0")
            tempStates.append(allStates[i] + "1")
            tempStates.append(allStates[i] + "2")
        allStates = tempStates

    allEnvironments = []

    for i in allStates:
        allEnvironments.append(environment(i))

    return allEnvironments


def main():
    p1 = agent()
    p2 = agent()

    allEnvs = generateAllStates()

    p1V = initializeV(allEnvs, 1)
    p1.setV(p1V)
    p1.setSymbol(1)

    p2V = initializeV(allEnvs, 2)
    p2.setV(p2V)
    p2.setSymbol(2)

    for i in range(1000):
        if i % 200 == 0:
            print(i)
        playGame(p1, p2, environment(), 0)

    hum = human()
    hum.setSymbol(2)
    p1.setVerbose(True)

    while True:
        playGame(p1, hum, environment(), 2)
        print("Game Over\n\n\n")



if __name__ == "__main__":
    main()
