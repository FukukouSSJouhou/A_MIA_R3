#!/usr/bin/env python3
import cv2
from PIL import Image

from A_MIA_R3_Core.Face_Process import Face_Process
import ctypes

from A_MIA_R3_Core.Graph_Process import Graph_Process

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

def main():
    filenamekun="koizumi_7_30.mp4"
    fp=Face_Process(filenamekun,29)
    fp.get_videoinfo()
    timeemoskun=fp.process()
    gp=Graph_Process(filenamekun)
    imgkun=gp.process(timeemoskun)
    #img=Image.fromarray(imgkun)
    imgcv=cv2.cvtColor(imgkun,cv2.COLOR_RGB2BGR)
    cv2.imshow("tdn",imgcv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Hello")


if __name__ == '__main__':
    main()
