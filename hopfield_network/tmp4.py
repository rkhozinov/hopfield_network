__author__ = 'rkhozinov'

from neurolab.net import newhop

inputs = [[-1, -1, -1], [1, -1, 1]]

net = newhop(inputs)
output = net.sim([[-1, 1, -1], [1, -1, 1]])

print inputs
print output.tolist()