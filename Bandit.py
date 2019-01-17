from __future__ import division
import numpy as np


class Bandit:
    def __init__(self, m):
        self.trueMean = m
        self.xBar = 0
        self.count = 0

    def pull(self):
        self.count += 1
        return (np.random.randn()) + self.trueMean

    def updateMean(self, observed):
        self.xBar = ((self.count-1.0)/self.count) * self.xBar + (1.0/self.count * observed)

    def display(self):
        print("True Mean: " + str(self.trueMean))
        print("xBar: " + str(self.xBar))
        print("Count: " + str(self.count))
