import datetime
import inspect

from A_MIA_R3_Core.Loggingkun.MIALogger_base import MIALogger_base


class MIALogger(MIALogger_base):

    def __timestampbaseout(self,colorcode,strtxt):
        self.origcolorout(colorcode,"[{}]\t{}".format(datetime.datetime.now(),strtxt))
    def __timestampbaseoutnocr(self,strtxt):
        self.orignocrkunout("[{}]\t{}".format(datetime.datetime.now(),strtxt))
    def __init__(self,baseoutkun,nocrkun,enabledebug:bool = True):
        self.origcolorout=baseoutkun
        self.orignocrkunout=nocrkun
        super().__init__(self.__timestampbaseout,self.__timestampbaseoutnocr,enabledebug)

    def debugout(self,strkun):
        """
        デバッグ出力(紫色) シンボル名付き

        :param strkun: 出力させたい文字列
        :return:
        """
        if self.enabledebug == True:
            super().debugout("\b[{} -> {} ]\t{}".format(inspect.stack()[1].filename,inspect.stack()[1].function,strkun))
    def debugout_none(self,strkun):
        """
        デバッグ出力(紫色)

        :param strkun: 出力させたい文字列
        :return:
        """
        super().debugout(strkun)