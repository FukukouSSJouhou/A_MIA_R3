import os

import cv2
from tensorflow.python.keras.models import load_model

def path_cutext(pathkun):
    pathkun22, extkun = os.path.splitext(os.path.basename(pathkun))
    return pathkun22

class Facemod:
    def __init__(self,filename,frames,splitkun):
        self.filename=filename
        self.frames=frames
        self.splitframe=splitkun
        model_path = './FACE/models/5face_emotions_100ep.hdf5'
        self.emotions_XCEPTION = load_model(model_path, compile=False)

        self.timeemos=[]
        self.video_path_ONLY=path_cutext(self.filename)
        # 動画画像保存フォルダを作成
        self.imgDIR_NAME = './FACE/temp_img/img_'+self.video_path_ONLY
        if not os.path.exists(self.imgDIR_NAME):
            os.makedirs(self.imgDIR_NAME)

        if not os.path.exists('./FACE/facepointmemo/'):
            os.makedirs('./FACE/facepointmemo/')

        if not os.path.exists('./FACE/emomemo/'):
            os.makedirs('./FACE/emomemo/')
    def process(self):
        capture = cv2.VideoCapture(self.filename)
        fps = capture.get(cv2.CAP_PROP_FPS)
        counterfps=1
        self.facepoint=[]
        # LOAD CASCADE
        cascade_path='./FACE/models/haarcascade_frontalface_default.xml'
        cascade=cv2.CascadeClassifier(cascade_path)
        self.hantei = 0
        while counterfps <= self.frames:
            capture.set(cv2.CAP_PROP_POS_FRAMES, counterfps)
            ret,frame=capture.read()
            if(ret == False):
                counterfps+=self.splitframe
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.front_face_list = cascade.detectMultiScale(gray)
            print("{} {}".format(counterfps, self.front_face_list))
            counterfps+=self.splitframe