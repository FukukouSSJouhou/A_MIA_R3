import av

from A_MIA_R3_Core.faceproc.Facemod import Facemod


class Face_Process:

    def __init__(self,filename:str,split_frames:int):
        self.filename=filename
        self.total_frames=0
        self.split_frames=split_frames
        self.fps=0
    def get_videoinfo(self):
        container=av.open(self.filename)
        self.total_frames = container.streams.video[0].frames
        self.fps=container.streams.video[0].base_rate
    def process(self):
        fm=Facemod(self.filename,self.total_frames,self.fps,self.split_frames)
        fm.process()
