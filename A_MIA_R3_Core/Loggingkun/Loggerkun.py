from A_MIA_R3_Core.Loggingkun.MIALogger_base import MIALogger_base


class MIALogger(MIALogger_base):
    def __init__(self,baseoutkun,nocrkun,enabledebug:bool = True):
        super().__init__(baseoutkun,nocrkun,enabledebug)