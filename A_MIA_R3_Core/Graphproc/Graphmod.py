import os

import numpy as np
from matplotlib import pyplot as plt


class DrawGraphs:
    def __init__(self,path_ONLY):
        self.path_ONLY=path_ONLY
        if not os.path.exists("./MakeGraph/graphs/"):
            os.makedirs("./MakeGraph/graphs/")

    def DrawEmotion(self,emotiondataarray):
        colors = ["#ff0000", "#ffff00", "#000000", "#0000ff", "#00ff00"]
        ylist = [[], [], [], [], []]
        for i in range(5):
            for j in range(len(emotiondataarray)):
                ylist[i].append(emotiondataarray[j][i])
        x=list(range(len(emotiondataarray)))
        print(x)
        fig=plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        linetype='-'
        title='detected emotions (Face only) ' + self.path_ONLY
        for i in range(5):
            ax.plot(x,ylist[i],linetype,c=colors[i],linewidth=1)

        # 汎用要素
        ax.grid(True)
        ax.set_xlabel('frame [?]')
        ax.set_ylabel('exist rate')
        ax.set_title(title)
        ax.legend(['angry','happy','neutral','sad','surprise'])
        fig.canvas.draw()
        im = np.array(fig.canvas.renderer.buffer_rgba())
        return im