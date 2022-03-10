class MIALogger():
    def __init__(self,baseoutkun,nocrkun,enabledebug:bool = True):
        self.logginkun=baseoutkun
        self.nocrlogging=nocrkun
        self.enabledebug=enabledebug
    def normalout(self,strkun):
        self.nocrlogging(strkun)
    def colorout(self,color,strkun):
        self.logginkun(color,strkun)
    def errout(self,strkun):
        self.logginkun("#FF0000",strkun)
    def successout(self,strkun):
        self.logginkun("#00FF00",strkun)
    def warnout(self,strkun):
        self.logginkun("#FFFF00",strkun)
    def debugout(self,strkun):
        if self.enabledebug == True:
            self.logginkun("#FF00FF",strkun)
    def blueout(self,strkun):
        self.logginkun("#0000FF",strkun)
