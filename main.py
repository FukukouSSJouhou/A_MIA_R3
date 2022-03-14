#!/usr/bin/env python3
import os
import sys

from PySide2 import QtWidgets


def main():
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QtWidgets.QApplication(sys.argv)
    

if __name__ == '__main__':
    main()
