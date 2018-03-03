#!/usr/bin/python

import numpy as np

# 3 inputs
x = np.array([[0.2],
              [0.5],
              [0.6]])

# 2 layers weights
W = np.array([[-0.5,  0.2,  0.1],
              [ 0.7, -0.8,  0.2]])

# 2 layers bias
b = np.array([[0.1],
              [0.2]])

# 2 outputs outputs
y = np.dot(W,x)+b

print "Output or Logits = {}".format(y.T)
