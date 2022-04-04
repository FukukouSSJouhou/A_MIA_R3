import base64
import os

from PIL import Image
import io
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
    def similarity(self, images):
        """
        入力された画像とターゲットの類似度を計算して最大のものを返すっピ!

        :param images: 検出された画像たち
        :return: 類似度が最も高い画像
        """
        # BFMatcherオブジェクトの生成
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        # 特徴点を検出
        detector = cv2.AKAZE_create()
        # detector = cv2.ORB_create()
        (target_kp, target_des) = detector.detectAndCompute(self.targetimage, None)

        similarity_list = []
        for comparing_img in images:
            try:
                (comparing_kp, comparing_des) = detector.detectAndCompute(comparing_img, None)
                matches = bf.match(target_des, comparing_des)
                dist = [m.distance for m in matches]
                ret_simi = sum(dist) / len(dist)
            except cv2.error:
                # cv2がエラーを吐いた場合の処理
                ret_simi = 100000
            self.Loggingobj.debugout(ret_simi)
            similarity_list.append(ret_simi)
        if not similarity_list:
            return None
        return images[similarity_list.index(min(similarity_list))]
    def __init__(self,jslog):
        self.front_face_list = []
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
    def processkun(self,targetbase64:str,filename:str,perfps:int):
        self.filename=filename
        self.targetimage= cv2.resize(cv2.cvtColor(np.array(Image.open(io.BytesIO(base64.b64decode(targetbase64)))), cv2.COLOR_BGR2GRAY),
                                          (200, 200))
        capture = cv2.VideoCapture(self.filename)
        self.frames=int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.splitframe=perfps
        fps = capture.get(cv2.CAP_PROP_FPS)
        counterfps = 1
        self.facepoint = []
        # LOAD CASCADE
        cascade_path = './FACE/models/haarcascade_frontalface_default.xml'
        cascade = cv2.CascadeClassifier(cascade_path)
        self.hantei = 0
        while counterfps <= self.frames:
            capture.set(cv2.CAP_PROP_POS_FRAMES, counterfps)
            ret, frame = capture.read()
            if (ret == False):
                counterfps += self.splitframe
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.front_face_list = cascade.detectMultiScale(gray)
            self.Loggingobj.debugout("{} {}".format(counterfps, self.front_face_list))
            faces_list_orig = []
            faces_list_cut = []

            for (x, y, w, h) in self.front_face_list:
                faces_list_orig.append(frame[y: y + h, x: x + w].copy())
            for facekun in faces_list_orig:
                faces_list_cut.append(
                    cv2.resize(cv2.cvtColor(cv2.cvtColor(facekun, cv2.COLOR_BGR2GRAY), cv2.COLOR_BGR2RGB), (200, 200)))
            # for facekun2 in faces_list_cut:
            #    plt.imshow(facekun2)
            #    plt.show()
            similarface = self.similarity(faces_list_cut)
            if similarface is not None:
                self.detect_emotion(similarface)
            counterfps += self.splitframe
    def detect_emotion(self, imgobj):
        """
        実際に感情分析をするッピ!

        :param imgobj: 類似度が一番高い画像が入るッピ!
        :return: 何も返しませんよ
        """

        if imgobj is not None:
            img_array = image.img_to_array(cv2.resize(imgobj, (48, 48)))
            pImg = np.delete(img_array, 1, axis=2)
            pImg = np.delete(pImg, 1, axis=2)
            pImg = np.expand_dims(pImg, 0) / 255
            prediction = self.emotions_XCEPTION.predict(pImg)[0]

            emos = []
            self.Loggingobj.debugout("{}".format(prediction))
            for predict_i in range(len(prediction)):
                emos.append(prediction[predict_i])
            self.timeemos.append(emos)
        else:
            emos = [0, 0, 0, 0, 0]
            self.timeemos.append(emos)