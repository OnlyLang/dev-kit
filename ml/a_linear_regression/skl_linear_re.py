"""
使用sklearn 实现线性回归
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn import linear_model
from sklearn.externals import joblib
import numpy as np

font = FontProperties(fname=r"C:/Windows/Fonts/FZYTK.TTF", size=10)


def run_plt(size=None, title="测试图", x_label="x坐标", y_label="y坐标"):
    plt.figure(figsize=size)
    plt.title(title, fontproperties=font)
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt


plt = run_plt()
X_ = [[6], [8], [10], [14], [18]]
y_ = [[7], [9], [13], [17.5], [18]]


def show(X, y):
    plt.plot(X, y, 'k.')
    plt.show()


def train():
    # 调用 sklearn 的线性模型
    model = linear_model.LinearRegression()
    print("====================================")
    model.fit(X_, y_)  # 线性模型的数据填充，即训练过程

    joblib.dump(model, "linear_model.m")
    model.predict()


model = joblib.load("../model/linear_model.m")
predict = model.predict([[10]])
print(predict)
