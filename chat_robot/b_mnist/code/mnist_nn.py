"""
mnist 网络模型
"""
import tensorflow as tf


class MnistNN(object):

    def __init__(self, model_dir):
        self.model_dir = model_dir
        self.input_dim = 784
        self.output_dim = 10
        self.keep_prob = 0.9
        with tf.name_scope("input_data"):
            self.x = tf.placeholder(tf.float32, [None, self.input_dim])
            self.y = tf.placeholder(tf.float32, [None, self.output_dim])
            self.keep_prob = tf.placeholder(tf.float32)

    def model(self):
        # 第一层神经网络
        weight1 = tf.Variable(tf.truncated_normal([self.input_dim, 500], stddev=0.1))
        bias1 = tf.Variable(tf.constant(0.1, shape=[500]))
        layer1 = tf.nn.dropout(tf.nn.relu(tf.matmul(self.x, weight1) + bias1), keep_prob=self.keep_prob)

        # 第二层神经网络
        weight2 = tf.Variable(tf.truncated_normal([500, 10], stddev=0.1))
        bias2 = tf.Variable(tf.constant(0.1, shape=[10]))
        y_predict = tf.identity(tf.matmul(layer1, weight2) + bias2)
        return y_predict
