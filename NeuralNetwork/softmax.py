#!/usr/bin/python

import numpy as np

def softmax(z):
    """Compute softmax values for each sets of scores in z."""
    return np.exp(z) / np.sum(np.exp(z), axis=0)

logits = [3.0, 1.0, 0.2]
sm = softmax(logits)

print("\nLogits :\t{}\nSoftmax:\t{}\nTotal  :\t{}\n".format(logits,sm, np.sum(sm)))