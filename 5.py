import tensorflow as tf

x = tf.ones([10, 4, 4, 5])
w = tf.ones([2, 2, 2, 5])
y = tf.nn.conv2d_transpose(x, w, output_shape=[10, 12, 12, 2], strides=[1, 3, 3, 1], padding='SAME')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(y))