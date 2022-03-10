import os

from A_MIA_R3_Core.Graphproc import Graphmod


class Graph_Process:
    def __path_cutext2(self,pathkun):
        pathkun22, extkun = os.path.splitext(os.path.basename(pathkun))
        return pathkun22
    def __init__(self,filename):
        self.filename=filename
        self.path_ONLY=self.__path_cutext2(filename)
    def process(self,Facearray):
        Instance2_graph = Graphmod.DrawGraphs(self.path_ONLY)
        return Instance2_graph.DrawEmotion(Facearray)

