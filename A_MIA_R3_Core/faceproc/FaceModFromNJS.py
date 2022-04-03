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

