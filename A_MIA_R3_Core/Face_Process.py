import av

from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.Facemod import Facemod


class Face_Process:
    def __init__(self, filename: str, split_frames: int, loggerobj: MIALogger):
        """
        コンストラクタだよ～

        :param filename: ビデオファイル名
        :param split_frames: 一回当たりのフレーム数
        :param loggerobj: Logger object
        """
        self.filename = filename
        self.Loggingobj = loggerobj
        self.total_frames = 0
        self.split_frames = split_frames

    def get_videoinfo(self):
        """
        ビデオ情報取得
        """
        self.Loggingobj.debugout("Opening video file")
        container = av.open(self.filename)
        self.Loggingobj.debugout("getting frames")
        self.total_frames = container.streams.video[0].frames

    def process(self):
        """
        実際に感情分析の処理を呼び出す。

        :return: 一定フレーム当たりの感情データ
        """
        fm = Facemod(self.filename, self.total_frames, self.split_frames, self.Loggingobj)
        self.Loggingobj.normalout("Starting target selector...")
        fm.target_img_select()
        # fm.showtargetimage()
        fm.process()
        return fm.get_timeemos()
