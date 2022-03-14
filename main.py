#!/usr/bin/env python3
import os
import sys

from PySide2 import QtWidgets, QtQml


def main():
    #環境変数をセット
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    #Qtのアプリケーションオブジェクトを生成
    app = QtWidgets.QApplication(sys.argv)
    engine=QtQml.QQmlApplicationEngine()
    engine.load("A_MIA_R3.qml")
    


if __name__ == '__main__':
    main()
