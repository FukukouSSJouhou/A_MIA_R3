from A_MIA_R3_Core.Loggingkun.MIALogger_base import MIALogger_base


class MIALogger(MIALogger_base):

    def __timestampbaseout(self,colorcode,strtxt):
        self.origcolorout(colorcode,strtxt)
    def __timestampbaseoutnocr(self,strtxt):
        self.orignocrkunout(strtxt)
    def __init__(self,baseoutkun,nocrkun,enabledebug:bool = True):
        self.origcolorout=baseoutkun
        self.orignocrkunout=nocrkun
        super().__init__(self.__timestampbaseout,self.__timestampbaseoutnocr,enabledebug)