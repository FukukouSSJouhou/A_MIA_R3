class Facemod:
    def __init__(self,filename,frames,fps,splitkun):
        self.filename=filename
        self.frames=frames
        self.fps=fps
        self.splitframe=splitkun
    def process(self):
        capture = cv2.VideoCapture(self.video_path)