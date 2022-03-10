import os


class Graph_Process:
    def __path_cutext2(pathkun):
        pathkun22, extkun = os.path.splitext(os.path.basename(pathkun))
        return pathkun22
    def __init__(self,filename):
        self.filename=filename
        self.path_Only=self.__path_cutext2(filename)
    def process(self,Facearray):
        pass
