import os
import random
import time

__author__ = 'rkhozinov'

#!/usr/bin/python

# list of patterns

patterns = [[1, 1, -1, -1],
            [-1, -1, 1, -1],
            [-1, -1, -1, -1]]

# number of units
n = 4

alpha = 1

weights = []
output = []


def initWeights(n):
    global weights
    weights = [[0 for _ in range(n)] for _ in range(n)]
    print (weights)


# initialises units to activation
def initNetwork(p):
    global output
    output = p
    print p

# pick unit at random and update k times
def updateNetwork(k):
    global output, weights
    for l in range(k):
        unit = random.randint(0, n - 1)
        # print ("updating unit", unit)
        act = 0
        for i in range(n):
            act += output[i] * weights[unit][i]
            output[unit] = 1 if act > 0 else -1
            # time.sleep(0.2)
        # print (('-' * 20).ljust(80))
        print ('%s:%d' % (output, unit + 1))


def learn(p):
    global alpha, n, weights
    for i in range(n):
        for j in range(n):
            if i != j:
                weights[i][j] += alpha * int(p[i]) * int(p[j])


print ('Initialising all weights to zero.')
print ('Weights initialised:')
initWeights(n)
learn(patterns[0])
learn(patterns[1])
print ('Initial patterns:')
print(patterns)
print('Now choosing a pattern at random...')
print('Adjusting weights via Hebbian learning...')
print('Adjusting weights for chosen pattern:')
print (weights)
print ('Initialising the network to a random state...')
print('Network initialised:')
# manual init
initNetwork([1, -1, 1, -1])
# random init
#initNetwork([r for r in range(5)])
print('Updating the network')
updateNetwork(10)
print(os.linesep + 'Final pattern:')
print (output)
print (os.linesep * 3)
