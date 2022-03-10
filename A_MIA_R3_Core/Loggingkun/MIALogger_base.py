import inspect
class MIALogger_base:
    """
    カラー出力ができるLogger
    """
    def __init__(self,baseoutkun,nocrkun,enabledebug:bool = True):
        """
        コンストラクタです。

        :param baseoutkun: 色付き出力関数
        :param nocrkun: 色なし出力関数
        :param enabledebug: デバッグログを表示するか否か
        """
        self.logginkun=baseoutkun
        self.nocrlogging=nocrkun
        self.enabledebug=enabledebug
    def normalout(self,strkun):
        """
        装飾なしの出力

        :param strkun: 出力させたい文字列
        :return:
        """
        self.nocrlogging(strkun)
    def colorout(self,color,strkun):
        """
        カラーコードで色を指定した出力

        :param color: カラーコード
        :param strkun: 出力させたい文字列
        :return:
        """
        self.logginkun(color,strkun)
    def errout(self,strkun):
        """
        エラー出力(赤色)

        :param strkun: 出力させたい文字列
        :return:
        """
        self.logginkun("#FF0000",strkun)
    def successout(self,strkun):
        """
        成功時出力(緑色)

        :param strkun: 出力させたい文字列
        :return:
        """
        self.logginkun("#00FF00",strkun)
    def warnout(self,strkun):
        """
        警告出力(黄色)

        :param strkun: 出力させたい文字列
        :return:
        """
        self.logginkun("#FFFF00",strkun)
    def debugout_none(self,strkun):
        """
        デバッグ出力(紫色)

        :param strkun: 出力させたい文字列
        :return:
        """
        if self.enabledebug == True:
            self.logginkun("#FF00FF",strkun)
    def debugout(self,strkun):
        """
        デバッグ出力(紫色) シンボル名付き

        :param strkun: 出力させたい文字列
        :return:
        """
        if self.enabledebug == True:
            self.logginkun("#FF00FF","[{} -> {} ]\n{}".format(inspect.stack()[1].filename,inspect.stack()[1].function,strkun))
    def blueout(self,strkun):
        """
        青色の出力

        :param strkun: 出力させたい文字列
        :return:
        """
        self.logginkun("#0000FF",strkun)
