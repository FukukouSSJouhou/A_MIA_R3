#!/usr/bin/env python3
import base64
import json
import os
import sys
import time

import cv2
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from flask import Flask, request, render_template

from A_MIA_R3_Core.Face_Process import Face_Process
from A_MIA_R3_Core.Graph_Process import Graph_Process
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.FPCallbackFaceSelector import FPCallbackFaceSelector, FPCallbackFaceSelected

app = Flask(__name__)
app.config.from_object(__name__)
class mainold_selectwin:
    def __init__(self,ss):
        self.ws=ss
    def select_target_img_window(self, frame, front_face_list, fpselected: FPCallbackFaceSelected):
        """
        検出された画像からターゲットを選出するためにダイアログを表示するッピ!

        :param frame: 現在のフレームッピ!
        :return: 何も返さないッピ!
        """
        self.i = 0
        for (x, y, w, h) in front_face_list:
            self.i += 1

        win_width = 10 + (120 * self.i)
        win_height = 180
        self.frame = frame.copy()

        load_img_list_base64 = []
        load_img_list_origcv = []
        j = 0
        load_img_list_base64.append("")
        for (x, y, w, h) in front_face_list:
            img = frame[y: y + h, x: x + w].copy()
            self.load_img_list_origcv.append(img.copy())
            imgkundest=cv2.resize(img,dsize=(100,100))
            ret,dstdata=cv2.imencode(".jpg",imgkundest)
            load_img_list_base64.append("data:image/jpeg;base64,{}".format(base64.b64encode(dstdata).decode("ascii")))
            j += 1
        senddt={"data":load_img_list_base64}
        self.ws.send(json.dumps(senddt))
        while True:
            time.sleep(1)
            message = self.ws.receive()
            if message is not None:
                fpselected.execute(
                    cv2.resize(cv2.cvtColor(load_img_list_origcv[message - 1].copy(), cv2.COLOR_BGR2GRAY),
                               (200, 200)))
                break

    def showwin_close(self, load_img_list_origcv, fpselected: FPCallbackFaceSelected):
        """
        選択ダイアログを閉じると呼び出されるっピ!

        :param load_img_list_origcv: オリジナルサイズの候補画像ッピ!
        :return: 何も返さないッピ!
        """
        ##### showwinを消した時の処理 #####
        rdo_which = self.rdo_var_target.get()
        print(rdo_which)
        # 'target画像がない'を選択していない場合、処理
        if rdo_which - 1 != self.i:
            # old = self.imgDIR_NAME + '/temp' + str(rdo_which - 1) + '.jpg'
            # new = self.imgDIR_NAME + '/target.jpg'
            # shutil.copy(old, new)
            # gray and cut
            # self.targetimage = cv2.resize(cv2.cvtColor(load_img_list_origcv[rdo_which - 1].copy(), cv2.COLOR_BGR2GRAY),
            #                             (200, 200))
            fpselected.execute(cv2.resize(cv2.cvtColor(load_img_list_origcv[rdo_which - 1].copy(), cv2.COLOR_BGR2GRAY),
                                          (200, 200)))

        else:
            return


def logout_color(colorcode, txt):
    """
    色付きログ出力を行うコードだよ

    :param colorcode: カラーコード
    :param txt: 出力内容
    :return:
    """
    r = int(colorcode[1:3], 16)
    g = int(colorcode[3:5], 16)
    b = int(colorcode[5:7], 16)
    print("\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, txt))

@app.route('/run')
def run():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']

        # Logger Objectの作成
        Loggingobj = MIALogger(logout_color, print)
        filenamekun = "koizumi_7_30.mp4"
        Loggingobj.successout("<< A_MIA_R3 Core System>>")
        Loggingobj.debugout("Creating callback object")
        callbackobj_func = mainold_selectwin()
        callbackobj = FPCallbackFaceSelector(callbackobj_func.select_target_img_window)
        Loggingobj.debugout("Creating Face_Process Obj")
        fp = Face_Process(filenamekun, 29, Loggingobj, callbackobj)
        Loggingobj.normalout("get Video info")
        fp.get_videoinfo()
        Loggingobj.normalout("Processing...")
        timeemoskun = fp.process()
        Loggingobj.normalout("Generating Graph...")
        gp = Graph_Process(filenamekun, Loggingobj)
        imgkun = gp.process(timeemoskun)
        Loggingobj.successout("Success! Generated graph...")
        # img=Image.fromarray(imgkun)
        imgcv = cv2.cvtColor(imgkun, cv2.COLOR_RGB2BGR)
        cv2.imshow("tdn", imgcv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return
def main():
    """
    メインコードだよ

    :return:
    """
    app.debug = True

    host = 'localhost'
    port = 1919

    host_port = (host, port)
    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()
if __name__ == '__main__':
    main()
