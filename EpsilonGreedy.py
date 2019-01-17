import numpy as np
from Bandit import Bandit

#epsilon, array of bandits, number of trials
def epsilonGreedy(epsilon, bandits, iterations):
    bestBandit = 0
    totalReward = 0
    for i in range(iterations):
        if(np.random.randn() <= epsilon):
            choice = np.random.choice(len(bandits))
            bandit = bandits[choice]
            reward = bandit.pull()
            totalReward += reward
            bandit.updateMean(reward)
            bestBandit = np.argmax([b.xBar for b in bandits])
        else:
            bandit = bandits[bestBandit]
            reward = bandit.pull()
            bandit.updateMean(reward)
            totalReward += reward
            bestBandit = np.argmax([b.xBar for b in bandits])
    return totalReward

bandits = []
for i in range(4):
    bandits.append(Bandit(i))


print(epsilonGreedy(0.1, bandits, 10000))
print(epsilonGreedy(0.01, bandits, 10000))
print(epsilonGreedy(0.001, bandits, 10000))
