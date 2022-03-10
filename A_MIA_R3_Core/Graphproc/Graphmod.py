import os


class DrawGraphs:
    def __init__(self,path_ONLY):
        self.path_ONLY=path_ONLY
        if not os.path.exists("./MakeGraph/graphs/"):
            os.makedirs("./MakeGraph/graphs/")