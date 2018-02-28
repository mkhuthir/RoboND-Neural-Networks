#!/usr/bin/python

# Quiz Solution
# Note: You can't run code in this tab
import numpy as np


def softmax(z):
    """Compute softmax values for each sets of scores in z."""
    return np.exp(z) / np.sum(np.exp(z), axis=0)

logits = [3.0, 1.0, 0.2]
print(softmax(logits))

