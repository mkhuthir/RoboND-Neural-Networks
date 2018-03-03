#!/usr/bin/python

import tensorflow as tf

# set the constants
x=tf.constant(10)
y=tf.constant(5)

#do the math
z1=tf.add(x,y)
z2=tf.subtract(x,y)
z3=tf.multiply(x,y)
z4=tf.divide(x,y)

#run
with tf.Session() as sess:
    i1=sess.run(x)
    i2=sess.run(y)
    o1=sess.run(z1)
    o2=sess.run(z2)
    o3=sess.run(z3)
    o4=sess.run(z4)
    print("X={} Y={} add={} subtract={} multiply={} divide={}".format(i1,i2,o1,o2,o3,o4))