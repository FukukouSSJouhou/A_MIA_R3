import os

import cv2
import tk as tk
from tensorflow.python.keras.models import load_model

def path_cutext(pathkun):
    pathkun22, extkun = os.path.splitext(os.path.basename(pathkun))
    return pathkun22

class Facemod:
    def __init__(self,filename,frames,splitkun):
        self.filename=filename
        self.frames=frames
        self.splitframe=splitkun
        model_path = './FACE/models/5face_emotions_100ep.hdf5'
        self.emotions_XCEPTION = load_model(model_path, compile=False)

        self.timeemos=[]
        self.targetimage=[]
        self.video_path_ONLY=path_cutext(self.filename)
        # 動画画像保存フォルダを作成
        self.imgDIR_NAME = './FACE/temp_img/img_'+self.video_path_ONLY
        if not os.path.exists(self.imgDIR_NAME):
            os.makedirs(self.imgDIR_NAME)

        if not os.path.exists('./FACE/facepointmemo/'):
            os.makedirs('./FACE/facepointmemo/')

        if not os.path.exists('./FACE/emomemo/'):
            os.makedirs('./FACE/emomemo/')
    def target_img_select(self):

        self.imgDIR_NAME = './FACE/temp_img/img_' + self.video_path_ONLY
        if not os.path.exists(self.imgDIR_NAME):
            os.makedirs(self.imgDIR_NAME)
        #self.loggingobj.debugout(self.filename)
        capture = cv2.VideoCapture(self.filename)
        fps = capture.get(cv2.CAP_PROP_FPS)
        counterfps=1
        self.facepoint=[]
        # LOAD CASCADE
        cascade_path='./FACE/models/haarcascade_frontalface_default.xml'
        cascade=cv2.CascadeClassifier(cascade_path)
        self.hantei = 0
        while counterfps <= self.frames:
            capture.set(cv2.CAP_PROP_POS_FRAMES, counterfps)
            ret,frame=capture.read()
            if(ret == False):
                counterfps+=self.splitframe
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.front_face_list = cascade.detectMultiScale(gray)
            print("{} {}".format(counterfps, self.front_face_list))
            if len(self.front_face_list) == 0:
                counterfps+=self.splitframe
                continue
            else:
                for(x,y,w,h) in self.front_face_list:

            counterfps+=self.splitframe
    def process(self):
        capture = cv2.VideoCapture(self.filename)
        fps = capture.get(cv2.CAP_PROP_FPS)
        counterfps=1
        self.facepoint=[]
        # LOAD CASCADE
        cascade_path='./FACE/models/haarcascade_frontalface_default.xml'
        cascade=cv2.CascadeClassifier(cascade_path)
        self.hantei = 0
        while counterfps <= self.frames:
            capture.set(cv2.CAP_PROP_POS_FRAMES, counterfps)
            ret,frame=capture.read()
            if(ret == False):
                counterfps+=self.splitframe
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.front_face_list = cascade.detectMultiScale(gray)
            print("{} {}".format(counterfps, self.front_face_list))
            counterfps+=self.splitframe

    def select_target_img_window(self):
        win_width = 10 + (120 * self.i)
        win_height = 180

        self.showwin = tk.Tk()
        self.showwin.title('Select target image')
        self.showwin.geometry('{}x{}+{}+{}'.format(win_width, win_height,
                                                   int(QtGui.QGuiApplication.primaryScreen().size().width() / 2 - win_width / 2),
                                                   int(QtGui.QGuiApplication.primaryScreen().size().height() / 2 - win_height / 2)))

        # 選択用のラジオボタンを配置
        # 画像それぞれのサイズを取得してshowwinのサイズを決める
        self.rdo_var_target = tk.IntVar()
        self.rdo_var_target.set(self.i + 1)
        rdo_txt = []
        load_img_list = []

        for j in range(self.i):
            # print(j)
            # ラジオボタンに表示するテキストをリストに追加
            rdo_txt.append('img-' + str(j + 1))
            # ラジオボタンを配置
            rdo_target_select = ttk.Radiobutton(self.showwin, variable=self.rdo_var_target, value=j + 1,
                                                text=rdo_txt[j])
            rdo_target_select.place(x=10 + 25 + (100 * j), y=120)

            # jpg画像ファイルを読み込む
            pil_img = Image.open(self.imgDIR_NAME + '/temp' + str(j) + '.jpg')
            pil_img_resize = pil_img.resize(size=(100, 100))
            photo_img = ImageTk.PhotoImage(image=pil_img_resize, master=self.showwin)
            load_img_list.append(photo_img)

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
        self.showwin_close()

    def showwin_close(self):
        ##### showwinを消した時の処理 #####
        rdo_which = self.rdo_var_target.get()
        print(rdo_which)
        # 'target画像がない'を選択していない場合、処理
        if rdo_which - 1 != self.i:
            old = self.imgDIR_NAME + '/temp' + str(rdo_which - 1) + '.jpg'
            new = self.imgDIR_NAME + '/target.jpg'
            shutil.copy(old, new)
        else:
            return