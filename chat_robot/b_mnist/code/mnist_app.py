"""
提供对外的接口访问
"""
import base64
import io

import numpy as np
from PIL import Image
from flask import Flask, request

import chat_robot.b_mnist.code as co
from chat_robot.b_mnist.code.mnist_recognize import Recognize

app = Flask(__name__)

rec = Recognize(co.model_dir)


@app.route("/", methods=["post"])
def recognize():
    data = request.get_json()
    base64str = data["img"]
    decode = base64.b64decode(base64str)
    image = io.BytesIO(decode)
    image_open = Image.open(image)
    img_array = np.array(image_open)
    gray = convert2gray(img_array)
    test_img = gray.flatten() / 255
    pred = rec.recognize([test_img])
    return str(pred)


def convert2gray(img):
    """
    图片转为灰度图，如果是3通道图则计算，单通道图则直接返回
    :param img:
    :return:
    """
    if len(img.shape) > 2:
        r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img


if __name__ == '__main__':
    app.run()
