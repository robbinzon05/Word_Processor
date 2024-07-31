from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from WordProcessorDesign import Ui_MainWindow
from FileOperations import FileOperations
from EditOperations import EditOperations
from FormatOpeartions import FormatOperations


class ProcessorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ProcessorWindow, self).__init__(parent)
        self.setupUi(self)

        self.file_ops = FileOperations(self.textEdit)
        self.edit_ops = EditOperations(self.textEdit)
        self.format_ops = FormatOperations(self.textEdit, self.spinBox)

        # FILE OPERATIONS
        self.actionNew.triggered.connect(self.file_ops.new_file)
        self.actionOpen.triggered.connect(self.file_ops.open_file)
        self.actionSave.triggered.connect(self.file_ops.save_file)

        QShortcut(QKeySequence("Ctrl+N"), self, self.file_ops.new_file)
        QShortcut(QKeySequence("Ctrl+O"), self, self.file_ops.open_file)
        QShortcut(QKeySequence("Ctrl+S"), self, self.file_ops.save_file)

        # EDIT OPERATIONS
        self.actionCopy.triggered.connect(self.edit_ops.copy)
        self.actionPaste.triggered.connect(self.edit_ops.paste)
        self.actionCut.triggered.connect(self.edit_ops.cut)

        QShortcut(QKeySequence("Ctrl+C"), self, self.edit_ops.copy)
        QShortcut(QKeySequence("Ctrl+V"), self, self.edit_ops.paste)
        QShortcut(QKeySequence("Ctrl+X"), self, self.edit_ops.cut)

        # FORMAT OPERATIONS
        self.actionFont_2.triggered.connect(self.format_ops.select_font)
        self.actionSize_2.triggered.connect(self.format_ops.select_size)
        self.actionColor_2.triggered.connect(self.format_ops.select_color)

        # TOOLBAR BUTTONS
        self.newFileBut.clicked.connect(self.file_ops.new_file)
        self.openFileBut.clicked.connect(self.file_ops.open_file)
        self.saveBut.clicked.connect(self.file_ops.save_file)
        self.fontBut.clicked.connect(self.format_ops.select_font)
        self.textSizeBut.clicked.connect(self.format_ops.select_size)
        self.colorBut.clicked.connect(self.format_ops.select_color)
        self.redoBut.clicked.connect(self.textEdit.redo)
        self.undoBut.clicked.connect(self.textEdit.undo)








