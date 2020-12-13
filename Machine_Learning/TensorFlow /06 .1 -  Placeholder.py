import tensorflow as tf 

NUM_PARALLEL_EXEC_UNITS = 4
config = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=NUM_PARALLEL_EXEC_UNITS, inter_op_parallelism_threads=2,
                       allow_soft_placement=True, device_count={'CPU': NUM_PARALLEL_EXEC_UNITS})

with tf.compat.v1.Session(config=config) as sess:
	a = 100
	b = 200
	x = tf.compat.v1.placeholder(tf.int32) 
	y = tf.compat.v1.placeholder(tf.int32)

	c = tf.add(x,y)
	
	result = sess.run(c, feed_dict={x: a, y: b})
	print(result)
	sess.close()



