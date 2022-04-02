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
    def setFilename(self,filename):
        self.filenamekun=filename
        self.Loggingobj.successout("set Filename:{}".format(filename))
        return filename
    def run(self):
        self.Loggingobj.successout("Run!!")
        self.Loggingobj.blueout(self.filenamekun)
        return 0