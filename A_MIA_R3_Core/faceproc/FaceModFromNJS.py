import av
import cv2

from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger


class FaceModFromNJS:
    def __init__(self,Loggingobj:MIALogger,filename:str,pertime:int):
        self.Loggingobj=Loggingobj
        self.filename=filename
        self.container=None
        self.pertime=pertime

        self.total_frames = 0
        self.current_fps = 1
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
                
