class WebSocImgSelectCallback:
    def __init__(self,callback):
        """
        コンストラクタッピ！

        :param callback:callback methodッピ!

        """
        self.callback=callback
    def execute(self,index:int):
        """
        callbackを実行するッピ!

        :param index: index!
        :return: 何も返さないッピ!

        """
        self.callback(index)