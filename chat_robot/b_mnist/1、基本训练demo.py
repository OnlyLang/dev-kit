from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

# 定义数据存放目录
data_dir = "./MNIST_DATA"
# 定义日志存放目录
log_dir = "./MNIST_LOG"
# 训练的最大步数
max_steps = 1000
# dropout 率
dropout = 0.9
# 学习率
learning_rate = 0.001
# 读取数据，并开启one_hot 编码
mnist = input_data.read_data_sets(data_dir, one_hot=True)

# 创建一个tensorflow的默认会话
session = tf.InteractiveSession()

# 创建输入数据的占位符
with tf.name_scope("input_data"):
    x = tf.placeholder(tf.float32, [None, 784], name="x-input")
    y_ = tf.placeholder(tf.float32, [None, 10], name="y-input")

# 保存图形信息
with tf.name_scope("input_reshape"):
    # 将一维的图像信息转换为一个正确的图像信息
    image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
    # summary 是将数据汇总给tensorbord
    tf.summary.image("input_image", image_shaped_input, 10)


# 接下来是神经网络部分。
# 采用简单神经网络

# 初始化神经网络的参数信息
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 在tensorbord中记录参数的变化
def variable_summaries(var):
    with tf.name_scope("summaries"):
        # 计算参数的均值，并使用tf.summary.scalar 记录
        mean = tf.reduce_mean(var)
        tf.summary.scalar("mean", mean)

        # 计算参数的标准差
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar("stddev", stddev)
        tf.summary.scalar("max", tf.reduce_max(var))
        tf.summary.scalar("min", tf.reduce_min(var))

        # 用直方图记录参数的分布
        tf.summary.histogram("histogram", var)


# 构建神经网络
def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
    with tf.name_scope(layer_name):
        # 初始化权重信息
        with tf.name_scope("weights"):
            weights = weight_variable([input_dim, output_dim])
            variable_summaries(weights)
        with tf.name_scope("bias"):
            bias = bias_variable([output_dim])
            variable_summaries(bias)

        # 执行 wx+b 的线性计算，并且用直方图记录下来
        with tf.name_scope("linear_compute"):
            predicted = tf.matmul(input_tensor, weights) + bias
            tf.summary.histogram("linear", predicted)
        activations = act(predicted, name="activation")
        tf.summary.histogram("activations", activations)
    return activations


hidden1 = nn_layer(x, 784, 500, "layer1")

with tf.name_scope("dropout"):
    keep_prob = tf.placeholder(tf.float32)
    tf.summary.scalar("dropout_keep_probability", keep_prob)
    dropped = tf.nn.dropout(hidden1, keep_prob)

y = nn_layer(dropped, 500, 10, "layer2", act=tf.identity)

with tf.name_scope("loss"):
    # 计算交叉熵损失
    diff = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y)
    with tf.name_scope("total"):
        # 计算所有样本的交叉熵损失的均值
        cross_entropy = tf.reduce_mean(diff)
    tf.summary.scalar("loss", cross_entropy)

with tf.name_scope("train"):
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

# 计算准确率
with tf.name_scope("accuracy"):
    with tf.name_scope("acc_predict"):
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

merged = tf.summary.merge_all()

train_writer = tf.summary.FileWriter(log_dir + "/train", session.graph)
test_writer = tf.summary.FileWriter(log_dir + "/test")

# 运行初始化所有变量
tf.global_variables_initializer().run()


# 数据获取
def feed_dict(train):
    if train:
        xs, ys = mnist.train.next_batch(100)
        k = dropout
    else:
        xs, ys = mnist.test.images, mnist.test.labels
        k = 1.0
    return {x: xs, y_: ys, keep_prob: k}


for i in range(max_steps):
    if i % 10 == 0:
        summary, acc = session.run([merged, accuracy], feed_dict=feed_dict(False))
        test_writer.add_summary(summary, i)
        print("accuracy at step %s: %s" % (i, acc))
    else:
        summary, _ = session.run([merged, train_step], feed_dict=feed_dict(True))
        train_writer.add_summary(summary, i)

train_writer.close()
test_writer.close()
