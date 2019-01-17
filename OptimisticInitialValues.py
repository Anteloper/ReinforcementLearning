import numpy as np
from Bandit import Bandit

#Array of bandits, number of trials
def optimisticInitialValues(bandits, iterations):
    bestBandit = 0
    totalReward = 0
    for bandit in bandits:
        bandit.xBar = 10
    for i in range(iterations):
        bandit = bandits[bestBandit]
        reward = bandit.pull()
        bandit.updateMean(reward)
        totalReward += reward
        bestBandit = np.argmax([b.xBar for b in bandits])

    return totalReward


bandits = []
for i in range(4):
    bandits.append(Bandit(i))


print(optimisticInitialValues(bandits, 10000))
