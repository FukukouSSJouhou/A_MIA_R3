import cv2


class Facemod:
    def __init__(self,filename,frames,splitkun):
        self.filename=filename
        self.frames=frames
        self.splitframe=splitkun
    def process(self):
        capture = cv2.VideoCapture(self.video_path)
        fps = capture.get(cv2.CAP_PROP_FPS)
        counterfps=0
        self.facepoint=[]
        # LOAD CASCADE
        cascade_path='./FACE/models/haarcascade_frontalface_default.xml'
        cascade=cv2.CascadeClassifier(cascade_path)