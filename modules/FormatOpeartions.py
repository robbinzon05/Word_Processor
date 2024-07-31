from PyQt5.QtWidgets import QColorDialog, QFontDialog, QTextEdit, QInputDialog
from PyQt5.QtGui import QColor


class FormatOperations:
    def __init__(self, text_edit: QTextEdit):
        self.text_edit = text_edit

    def select_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            cursor = self.text_edit.textCursor()
            format = cursor.charFormat()
            format.setFont(font)
            cursor.mergeCharFormat(format)

    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.text_edit.textCursor()
            format = cursor.charFormat()
            format.setForeground(QColor(color))
            cursor.mergeCharFormat(format)

    def select_size(self):
        size, ok = QInputDialog.getInt(self.text_edit, "Выбор размера текста", "Укажите размер текста:", min=1, max=100)
        if ok:
            cursor = self.text_edit.textCursor()
            format = cursor.charFormat()
            format.setFontPointSize(size)
            cursor.mergeCharFormat(format)
