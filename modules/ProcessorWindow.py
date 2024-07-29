from WordProcessorDesign import Ui_MainWindow
from PyQt5 import QtWidgets


class ProcessorWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()