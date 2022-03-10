#!/usr/bin/env python3
import cv2
from PIL import Image

from A_MIA_R3_Core.Face_Process import Face_Process
import ctypes

from A_MIA_R3_Core.Graph_Process import Graph_Process
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
def logout_color(colorcode,txt):
    """
    色付きログ出力を行うコードだよ

    :param colorcode: カラーコード
    :param txt: 出力内容
    :return:
    """
    r = int(colorcode[1:3], 16)
    g = int(colorcode[3:5], 16)
    b = int(colorcode[5:7], 16)
    print("\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, txt))
def main():
    """
    メインコードだよ

    :return:
    """
    #Logger Objectの作成
    Loggingobj=MIALogger(logout_color,print)
    filenamekun="koizumi_7_30.mp4"
    Loggingobj.successout("<< A_MIA_R3 Core System>>")
    Loggingobj.debugout("Creating Face_Process Obj")
    fp=Face_Process(filenamekun,29,Loggingobj)
    Loggingobj.normalout("get Video info")
    fp.get_videoinfo()
    Loggingobj.normalout("Processing...")
    timeemoskun=fp.process()
    Loggingobj.normalout("Generating Graph...")
    gp=Graph_Process(filenamekun,Loggingobj)
    imgkun=gp.process(timeemoskun)
    Loggingobj.successout("Success! Generated graph...")
    #img=Image.fromarray(imgkun)
    imgcv=cv2.cvtColor(imgkun,cv2.COLOR_RGB2BGR)
    cv2.imshow("tdn",imgcv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
