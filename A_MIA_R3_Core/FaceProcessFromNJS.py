from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.FaceModFromNJS import FaceModFromNJS


class FaceProcessFromNJS:
    def __init__(self, loggingobj: MIALogger, filename: str, perframe: int):
        self.Loggingobj = loggingobj
        self.filename = filename
        self.perframe = perframe

        self.FPkun=FaceModFromNJS(self.Loggingobj,self.filename,self.perframe)

    def openFile(self):
        self.FPkun.openFileObj()
    def getNextSomeFrameB64(self):
        return self.FPkun.getNextB64Lists()
    def getTargetImage(self,indexkun):
        return self.FPkun.getTargetImage(indexkun)
    def getTargetImageBase64(self,indexkun):
        return self.FPkun.getTargetImageBase64(indexkun)
    def closeObj(self):
        self.FPkun.closeObj()