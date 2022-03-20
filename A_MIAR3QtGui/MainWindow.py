from PySide2 import QtCore


class MainWindowConnect(QtCore.QObject):
    def __init__(self,parent=None):
        super(MainWindowConnect,self).__init__(parent)
