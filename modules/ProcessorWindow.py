import FileOperations as fileOps
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from WordProcessorDesign import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class ProcessorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionNew.triggered.connect(self.newFile)
        self.newFileBut.clicked.connect(self.newFile)

        self.actionOpen.triggered.connect(self.openFile)
        self.openFileBut.clicked.connect(self.openFile)

        self.actionSave.triggered.connect(self.saveFile)
        self.saveBut.clicked.connect(self.saveFile)

    def newFile(self):
        if self.textEdit.toPlainText():
            reply = QMessageBox.question(
                self, 'Message',
                "There is unsaved text. Do you want to save it?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.saveFile()
                self.textEdit.clear()
            elif reply == QMessageBox.No:
                self.textEdit.clear()
            else:
                return
        else:
            self.textEdit.clear()

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                              "Text Files (*.txt);;Word Files (*.docx)")
        if file:
            if file.endswith('.txt'):
                fileOps.open_txt(file, self.textEdit)
            elif file.endswith('.docx'):
                fileOps.open_docx(file, self.textEdit)

    def saveFile(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                              "Text Files (*.txt);;Word Files (*.docx);;PDF "
                                              "Files (*.pdf)")
        if file:
            if file.endswith(".txt"):
                fileOps.save_txt(file, self.textEdit)
            elif file.endswith(".docx"):
                fileOps.save_docx(file, self.textEdit)
            elif file.endswith(".pdf"):
                fileOps.save_pdf(file, self.textEdit)
            else:
                file += ".txt"
                fileOps.save_txt(file, self.textEdit)
