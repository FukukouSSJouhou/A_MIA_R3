#!/usr/bin/env python3
import cv2
from PIL import Image

from A_MIA_R3_Core.Face_Process import Face_Process
import ctypes
from tkinter import Image, ttk
from PIL import Image, ImageTk

import tkinter as tk
from A_MIA_R3_Core.Graph_Process import Graph_Process
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.FPCallbackFaceSelector import FPCallbackFaceSelected, FPCallbackFaceSelector

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
class mainold_selectwin:
    def __init__(self):
        pass
    def select_target_img_window(self, frame,front_face_list,fpselected:FPCallbackFaceSelected):
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
        self.showwin = tk.Tk()
        self.showwin.title('Select target image')
        self.showwin.geometry('{}x{}+{}+{}'.format(win_width, win_height,
                                                   #                                           int(QtGui.QGuiApplication.primaryScreen().size().width() / 2 - win_width / 2),
                                                   #                                           int(QtGui.QGuiApplication.primaryScreen().size().height() / 2 - win_height / 2)))
                                                   320, 320))
        # 選択用のラジオボタンを配置
        # 画像それぞれのサイズを取得してshowwinのサイズを決める
        self.rdo_var_target = tk.IntVar()
        self.rdo_var_target.set(self.i + 1)
        rdo_txt = []
        load_img_list = []
        load_img_list_origcv = []
        j = 0
        for (x, y, w, h) in front_face_list:
            # for j in range(self.i):
            # print(j)
            # ラジオボタンに表示するテキストをリストに追加
            rdo_txt.append('img-' + str(j + 1))
            # ラジオボタンを配置
            rdo_target_select = ttk.Radiobutton(self.showwin, variable=self.rdo_var_target, value=j + 1,
                                                text=rdo_txt[j])
            rdo_target_select.place(x=10 + 25 + (100 * j), y=120)

            # jpg画像ファイルを読み込む
            # pil_img = Image.open(self.imgDIR_NAME + '/temp' + str(j) + '.jpg')
            img = frame[y: y + h, x: x + w].copy()
            load_img_list_origcv.append(img.copy())
            pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            pil_img_resize = pil_img.resize(size=(100, 100))
            photo_img = ImageTk.PhotoImage(image=pil_img_resize, master=self.showwin)
            load_img_list.append(photo_img)
            j += 1

        # 一番最後に、target画像が無かった場合に選択するラジオボタンを配置
        rdo_target_select = ttk.Radiobutton(self.showwin, variable=self.rdo_var_target, value=self.i + 1,
                                            text='target画像がない')
        rdo_target_select.place(x=5, y=140)

        # キャンバスを作成して配置
        for j in range(self.i):
            canvas = tk.Canvas(self.showwin, width=100, height=100)
            canvas.create_image(50, 50, image=load_img_list[j])
            # canvas['bg'] = "magenta"
            canvas.place(x=10 + (110 * j), y=10)

        self.showwin.resizable(0, 0)
        self.showwin.grab_set()  # モーダル化
        self.showwin.focus_set()  # フォーカスを移 # サブウィンドウをタスクバーに表示しない

        self.showwin.mainloop()
        self.showwin_close(load_img_list_origcv,fpselected)

    def showwin_close(self, load_img_list_origcv,fpselected:FPCallbackFaceSelected):
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
            #self.targetimage = cv2.resize(cv2.cvtColor(load_img_list_origcv[rdo_which - 1].copy(), cv2.COLOR_BGR2GRAY),
             #                             (200, 200))
            fpselected.execute(cv2.resize(cv2.cvtColor(load_img_list_origcv[rdo_which - 1].copy(), cv2.COLOR_BGR2GRAY),
                                         (200, 200)))

        else:
            return

def logout_color(colorcode,txt):
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
def main():
    """
    メインコードだよ

    :return:
    """
    #Logger Objectの作成
    Loggingobj=MIALogger(logout_color,print)
    filenamekun="koizumi_7_30.mp4"
    Loggingobj.successout("<< A_MIA_R3 Core System>>")
    Loggingobj.debugout("Creating callback object")
    callbackobj_func=mainold_selectwin()
    callbackobj=FPCallbackFaceSelector(callbackobj_func.select_target_img_window)
    Loggingobj.debugout("Creating Face_Process Obj")
    fp=Face_Process(filenamekun,29,Loggingobj,callbackobj)
    Loggingobj.normalout("get Video info")
    fp.get_videoinfo()
    Loggingobj.normalout("Processing...")
    timeemoskun=fp.process()
    Loggingobj.normalout("Generating Graph...")
    gp=Graph_Process(filenamekun,Loggingobj)
    imgkun=gp.process(timeemoskun)
    Loggingobj.successout("Success! Generated graph...")
    #img=Image.fromarray(imgkun)
    imgcv=cv2.cvtColor(imgkun,cv2.COLOR_RGB2BGR)
    cv2.imshow("tdn",imgcv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
