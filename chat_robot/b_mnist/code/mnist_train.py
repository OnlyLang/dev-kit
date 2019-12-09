"""
利用 mnist nn 进行训练
"""
import os

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import chat_robot.b_mnist.code as co
from chat_robot.b_mnist.code.mnist_nn import MnistNN


class TrainMnist(MnistNN):

    def __init__(self, model_dir, data_dir, batch_size=100, learning_rate=0.001, max_step=100):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.max_step = max_step
        self.mnist = input_data.read_data_sets(self.data_dir, one_hot=True)

        super(TrainMnist, self).__init__(model_dir)

    def get_batch(self, train=True):
        if train:
            xs, ys = self.mnist.train.next_batch(self.batch_size)
        else:
            xs, ys = self.mnist.test.images, self.mnist.test.labels
        return xs, ys

    def train(self):
        # 预测
        y_predict = self.model()
        # 损失函数
        diff = tf.nn.softmax_cross_entropy_with_logits(labels=self.y, logits=y_predict)
        cross_entropy = tf.reduce_mean(diff)

        # 训练方式，最小化损失函数
        train = tf.train.AdamOptimizer(self.learning_rate).minimize(cross_entropy)

        # 开始计算正确率
        correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(self.y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        saver = tf.train.Saver(save_relative_paths=True)

        with tf.Session() as session:
            init = tf.global_variables_initializer()
            session.run(init)

            if os.path.exists(self.model_dir):
                saver.restore(session, self.model_dir)

            for i in range(self.max_step):
                x, y = self.get_batch()
                _, cost = session.run([train, cross_entropy], feed_dict={self.x: x, self.y: y, self.keep_prob: 0.9})
                if i % 10 == 0:
                    x, y = self.get_batch(False)
                    acc = session.run([accuracy], feed_dict={self.x: x, self.y: y, self.keep_prob: 1.0})
                    print("第%s次训练，正确率为：%s" % (i, acc))

            saver.save(session, self.model_dir)


if __name__ == '__main__':
    mnist_train = TrainMnist(model_dir=co.model_dir, data_dir=co.data_dir,max_step=5000)
    mnist_train.train()
