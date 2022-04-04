import os

from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger


import numpy as np

import cv2

from keras_preprocessing import image
from tensorflow.python.keras.models import load_model
from matplotlib import pyplot as plt

from A_MIA_R3_Core.faceproc.Facemod import path_cutext


class A_MIR_R3_node_tensor2(object):

    def logout_color(self,colorcode, txt):
        """
        色付きログ出力を行うコードだよ

        :param colorcode: カラーコード
        :param txt: 出力内容
        :return:
        """
        r = int(colorcode[1:3], 16)
        g = int(colorcode[3:5], 16)
        b = int(colorcode[5:7], 16)
        self.jslog("\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, txt))
    def __init__(self,jslog):
        self.jslog = jslog
        self.logout_color("#FF00FF", "Python Class for Tensorflow init..")
        self.Loggingobj = MIALogger(self.logout_color, self.jslog)
        model_path = './FACE/models/5face_emotions_100ep.hdf5'
        self.Loggingobj.normalout("Loading model...")
        self.emotions_XCEPTION = load_model(model_path, compile=False)

        self.timeemos = []
        self.targetimage = None

        if not os.path.exists('./FACE/facepointmemo/'):
            os.makedirs('./FACE/facepointmemo/')

        if not os.path.exists('./FACE/emomemo/'):
            os.makedirs('./FACE/emomemo/')