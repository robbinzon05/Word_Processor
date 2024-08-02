from PyQt5.QtWidgets import QFileDialog, QMessageBox
import OpenAndSaveFunctions as fileOps


class FileOperations:
    def __init__(self, text_edit):
        self.text_edit = text_edit

    def new_file(self):
        if self.text_edit.toPlainText():
            reply = QMessageBox.question(
                None, 'Message',
                "There is unsaved text. Do you want to save it?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.save_file()
                self.text_edit.clear()
            elif reply == QMessageBox.No:
                self.text_edit.clear()
            else:
                return
        else:
            self.text_edit.clear()

    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(None, "Open File", "",
                                              "Word Files (*.docx)")
        if file:
            fileOps.open_docx(file, self.text_edit)

    def save_file(self):
        file, _ = QFileDialog.getSaveFileName(None, "Save File", "",
                                              "Word Files (*.docx)")
        if file:
            fileOps.save_docx(file, self.text_edit)

