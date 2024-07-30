from PyQt5.QtWidgets import QApplication


class EditOperations:
    def __init__(self, text_edit):
        self.text_edit = text_edit
        self.clipboard = QApplication.clipboard()

    def copy(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            self.clipboard.setText(cursor.selectedText())

    def paste(self):
        cursor = self.text_edit.textCursor()
        cursor.insertText(self.clipboard.text())

    def cut(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            self.clipboard.setText(cursor.selectedText())
            cursor.removeSelectedText()
