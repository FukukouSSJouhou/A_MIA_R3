import os

from A_MIA_R3_Core.Graphproc import Graphmod
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
s

class Graph_Process:
    def __path_cutext2(self,pathkun):
        pathkun22, extkun = os.path.splitext(os.path.basename(pathkun))
        return pathkun22
    def __init__(self,filename,Loggingkun:MIALogger):
        self.filename=filename
        self.path_ONLY=self.__path_cutext2(filename)
        self.Loggingkun=Loggingkun
    def process(self,Facearray):
        Instance2_graph = Graphmod.DrawGraphs(self.path_ONLY,self.Loggingkun)
        return Instance2_graph.DrawEmotion(Facearray)

