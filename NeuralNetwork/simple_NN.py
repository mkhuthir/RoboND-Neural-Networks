#!/usr/bin/python

import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# inputs,weights, and bias
inputs  = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

# Calculate the output
output = sigmoid(np.dot(weights, inputs) + bias)

print('\nSimple Neural network:\n\nOutput=Sigmoid(w1.x1 + w2.x2 + b)')
print('\nx-inputs\t:{}\nw-weights\t:{}\nb-bias  \t:{}\n\nOutput  \t:{}\n'.format(inputs,weights,bias,output))
