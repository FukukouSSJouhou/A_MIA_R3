import base64

import av
import cv2

from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger


class FaceModFromNJS:
    def ImageCutter(self, frame, front_face_list):
        """
        検出された画像をカットしてBase64に変換して返すッピ!
        :param frame: frameッピ!
        :param front_face_list: 検出された画像の座標リストッピ!
        :return: Base64
        """

        i = 0
        for (x, y, w, h) in front_face_list:
            i += 1

        frame2s = frame.copy()

        load_img_list_base64 = []
        self.load_img_list_origcv = []
        j = 0
        load_img_list_base64.append("")
        for (x, y, w, h) in front_face_list:
            img = frame2s[y: y + h, x: x + w].copy()
            self.load_img_list_origcv.append(img.copy())
            imgkundest=cv2.resize(img,dsize=(100,100))
            ret,dstdata=cv2.imencode(".jpg",imgkundest)
            load_img_list_base64.append("data:image/jpeg;base64,{}".format(base64.b64encode(dstdata).decode("ascii")))
            j += 1
        #senddt={"data":load_img_list_base64}
        return load_img_list_base64
    def __init__(self,Loggingobj:MIALogger,filename:str,pertime:int):
        self.Loggingobj=Loggingobj
        self.filename=filename
        self.container=None
        self.pertime=pertime

        self.total_frames = 0
        self.current_fps = 1
    def getTargetImage(self,indexkun):
        return self.load_img_list_origcv[indexkun-1].copy()
    def getTargetImageBase64(self,indexkun):
        ret,dstdata=cv2.imencode(".jpg",self.getTargetImage(indexkun))
        return base64.b64encode(dstdata).decode("ascii")
    def closeObj(self):
        self.capture.release()
        self.current_fps=self.total_frames+88
    def openFileObj(self):
        container = av.open(self.filename)
        self.total_frames= container.streams.video[0].frames
        self.capture = cv2.VideoCapture(self.filename)
        fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.facepoint = []
        cascade_path = './FACE/models/haarcascade_frontalface_default.xml'
        self.cascade = cv2.CascadeClassifier(cascade_path)
    def getNextB64Lists(self):
        if self.current_fps > self.total_frames:
            return ["END"]
        else:
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.current_fps)
            ret, frame = self.capture.read()

            if (ret == False):
                self.current_fps += self.pertime
                return [""]
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            front_face_list = self.cascade.detectMultiScale(gray)
            self.Loggingobj.debugout("{} {}".format(self.current_fps, front_face_list))
            if len(front_face_list) == 0:
                self.current_fps += self.pertime
                return [""]
            else:
                # self.select_target_img_window(frame)
                # self.callbackobj.execute(frame, self.front_face_list, self.fpfsselectedkun)

                self.Loggingobj.debugout("Before image cutter")

                self.current_fps += self.pertime
                return self.ImageCutter(frame,front_face_list)
