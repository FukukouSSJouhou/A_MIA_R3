import json

from A_MIA_R3_Core.FaceProcessFromNJS import FaceProcessFromNJS
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger


class A_MIR_R3_node2(object):

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
        self.FPobj=None
        self.target_imgkun=None
    def setFilename(self,filename):
        self.filenamekun=filename
        self.Loggingobj.successout("set Filename:{}".format(filename))
        return filename
    def run(self):
        self.Loggingobj.successout("Run!!")
        self.Loggingobj.blueout(self.filenamekun)
        self.Loggingobj.successout("<< A_MIA_R3 Core System>>")
    def create_syoriobj(self):
        self.Loggingobj.normalout("Creating Proc Obj....")

        self.FPobj=FaceProcessFromNJS(self.Loggingobj,self.filenamekun,29)
        self.FPobj.openFile()
    def getNextImageBase64(self):
        self.Loggingobj.blueout("test called")
        lsobjkun=self.FPobj.getNextSomeFrameB64()
        senddt = {"data": lsobjkun}
        return json.dumps(senddt)
    def setselectimg(self,indexkun):
        self.target_imgkun =self.FPobj.getTargetImage(indexkun)
        self.Loggingobj.successout("selected image!!")
    def getselectedimg(self,indexkun):
        self.Loggingobj.normalout("get base64 targetimg")
        return self.FPobj.getTargetImageBase64(indexkun)
    def closeObj(self):
        self.FPobj.closeObj()