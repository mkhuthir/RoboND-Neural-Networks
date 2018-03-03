#!/usr/bin/python

import tensorflow as tf

# Define constants
x = tf.constant(10)
y = tf.constant(2)

#Do casting
z = tf.subtract(tf.divide(x,y),tf.cast(tf.constant(1), tf.float64))

# Run
with tf.Session() as sess:
    output = sess.run(z)
    print(output)
