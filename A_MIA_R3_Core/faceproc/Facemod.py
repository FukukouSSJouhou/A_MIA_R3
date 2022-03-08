import cv2


class Facemod:
    def __init__(self,filename,frames,splitkun):
        self.filename=filename
        self.frames=frames
        self.splitframe=splitkun
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