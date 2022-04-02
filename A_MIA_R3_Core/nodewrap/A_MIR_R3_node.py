import base64

import cv2

from A_MIA_R3_Core.Face_Process import Face_Process
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.FPCallbackFaceSelector import FPCallbackFaceSelected, FPCallbackFaceSelector


class A_MIR_R3_node2(object):
    def GenerateImageListsAndSend(self,frame,front_face_list,fpselected:FPCallbackFaceSelected):

        """
        検出された画像からターゲットを選出するためにダイアログを表示するッピ!

        :param frame: 現在のフレームッピ!
        :return: 何も返さないッピ!
        """
        self.i = 0
        for (x, y, w, h) in front_face_list:
            self.i += 1

        self.frame = frame.copy()

        load_img_list_base64 = []
        self.load_img_list_origcv = []
        j = 0
        load_img_list_base64.append("")
        for (x, y, w, h) in front_face_list:

            img = frame[y: y + h, x: x + w].copy()
            self.load_img_list_origcv.append(img.copy())
            imgkundest=cv2.resize(img,dsize=(100,100))
            ret,dstdata=cv2.imencode(".jpg",imgkundest)
            load_img_list_base64.append(base64.b64encode(dstdata))
            j += 1
        senddt={"data":load_img_list_base64}
        self.fpselected=fpselected
        self.imagelistsendcallback(senddt)
        while True:
            if self.selectimgended == True:
                break
            else:
                pass

    def recieve_selectimg(self,imageindex):
        if imageindex == 0:
            self.selectimgended=True
            return
        else:
            self.fpselected.execute(self.load_img_list_origcv[imageindex-1])
    def logout_color(self,colorcode, txt):
        """
        色付きログ出力を行うコードだよ

        :param colorcode: カラーコード
        :param txt: 出力内容
        :return:
        """
        r = int(colorcode[1:3], 16)
        g = int(colorcode[3:5], 16)
        b = int(colorcode[5:7], 16)
        self.jslog("\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, txt))
    def __init__(self,jslog):
        self.jslog=jslog
        self.logout_color("#FF00FF","Python Class init..")
        # Create logger Object
        self.Loggingobj = MIALogger(self.logout_color, self.jslog)
        self.filenamekun=""
        self.imagelistsendcallback=None
        self.selectimgended=False
        self.fpselected=None
        self.load_img_list_origcv = []
    def setFilename(self,filename):
        self.filenamekun=filename
        self.Loggingobj.successout("set Filename:{}".format(filename))
        return filename
    def run(self):
        self.Loggingobj.successout("Run!!")
        self.Loggingobj.blueout(self.filenamekun)
        self.Loggingobj.successout("<< A_MIA_R3 Core System>>")
        self.Loggingobj.debugout("Creating callback object")
        callbackobj=FPCallbackFaceSelector(self.GenerateImageListsAndSend)
        self.Loggingobj.debugout("Creating Face_Process Obj")
        fp = Face_Process(self.filenamekun, 29, self.Loggingobj, callbackobj)
        self.Loggingobj.normalout("get Video info")
        fp.get_videoinfo()
        self.Loggingobj.normalout("Processing...")
        timeemoskun = fp.process()
        return 0
    def Setimagelistsendcallback(self,cb):
        self.Loggingobj.blueout("Set Callback")
        self.imagelistsendcallback=cb
        return "aaaaaa"