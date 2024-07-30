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
                                              "Text Files (*.txt);;Word Files (*.docx)")
        if file:
            if file.endswith('.txt'):
                fileOps.open_txt(file, self.text_edit)
            elif file.endswith('.docx'):
                fileOps.open_docx(file, self.text_edit)

    def save_file(self):
        file, _ = QFileDialog.getSaveFileName(None, "Save File", "",
                                              "Text Files (*.txt);;Word Files (*.docx);;PDF Files (*.pdf)")
        if file:
            if file.endswith(".txt"):
                fileOps.save_txt(file, self.text_edit)
            elif file.endswith(".docx"):
                fileOps.save_docx(file, self.text_edit)
            elif file.endswith(".pdf"):
                fileOps.save_pdf(file, self.text_edit)
            else:
                file += ".txt"
                fileOps.save_txt(file, self.text_edit)
