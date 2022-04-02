from tkinter import ttk

import av
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.FPCallbackFaceSelector import FPCallbackFaceSelector, FPCallbackFaceSelected
from A_MIA_R3_Core.faceproc.Facemod import Facemod


class Face_Process:
    def __init__(self, filename: str, split_frames: int, loggerobj: MIALogger,callbackkun:FPCallbackFaceSelector):
        """
        コンストラクタだよ～

        :param filename: ビデオファイル名
        :param split_frames: 一回当たりのフレーム数
        :param loggerobj: Logger object
        :param callbackkun: Callback Object
        """
        self.filename = filename
        self.Loggingobj = loggerobj
        self.total_frames = 0
        self.split_frames = split_frames
        self.callbackkun=callbackkun


    async def get_videoinfo(self):
        """
        ビデオ情報取得
        """
        self.Loggingobj.debugout("Opening video file")
        container = av.open(self.filename)
        self.Loggingobj.debugout("getting frames")
        self.total_frames = container.streams.video[0].frames

    async def process(self):
        """
        実際に感情分析の処理を呼び出す。

        :return: 一定フレーム当たりの感情データ
        """
        fm = Facemod(self.filename, self.total_frames, self.split_frames, self.Loggingobj,self.callbackkun)
        self.Loggingobj.normalout("Starting target selector...")
        await fm.target_img_select()
        # fm.showtargetimage()
        self.Loggingobj.normalout("Start detecting emotions...")
        await fm.process()
        self.Loggingobj.successout("Success! Generated emos data!")
        return fm.get_timeemos()
