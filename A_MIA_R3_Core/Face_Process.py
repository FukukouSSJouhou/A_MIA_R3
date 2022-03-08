import av
class Face_Process:

    def __init__(self,filename:str):
        self.filename=filename
        self.total_frames=0
        self.fps=0
    def get_videoinfo(self):
        container=av.open(self.filename)
        self.total_frames = container.streams.video[0].frames
        self.fps=container.streams.video[0].base_rate
        print(self.total_frames)
        print(self.fps)

