#!/usr/bin/env python3
import os
import sys

from PySide2 import QtWidgets, QtQml

from A_MIAR3QtGui.MainWindow import MainWindowConnect


def main():
    #環境変数をセット
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    #Qtのアプリケーションオブジェクトを生成
    app = QtWidgets.QApplication(sys.argv)
    #ウィンドウ部分のコードを紐づけするオブジェクトの生成
    mainwinconnect=MainWindowConnect()
    #QMLのEngineを作成
    engine=QtQml.QQmlApplicationEngine()
    #操作用のrootコンテキストを取得
    ctx=engine.rootContext()
    #紐づけオブジェクトの紐づけ(mainwinconnectという名前で参照可能)
    ctx.setContextProperty("mainwinconnect",mainwinconnect)
    #qmlをロード
    engine.load("A_MIA_R3.qml")
    #正常にロードできていなければ落とす
    if not engine.rootObjects():
        sys.exit(-1)
    #アプリケーションの開始
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
