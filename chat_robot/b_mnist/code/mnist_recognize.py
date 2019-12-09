"""
mnist 识别方法
"""
from chat_robot.b_mnist.code.mnist_nn import MnistNN
import tensorflow as tf
import numpy as np


class Recognize(MnistNN):
    def __init__(self, model_dir):
        super(Recognize, self).__init__(model_dir)
        self.session = tf.Session()
        self.y_predict = self.model()
        saver = tf.train.Saver()
        with self.session.as_default() as sess:
            saver.restore(sess, self.model_dir)

    def recognize(self, input_data):
        run = self.session.run(self.y_predict, feed_dict={self.x: input_data, self.keep_prob: 1.0})
        return np.argmax(run, 1)
