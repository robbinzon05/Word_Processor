from PyQt5.QtWidgets import QColorDialog, QFontDialog, QTextEdit, QSpinBox, QInputDialog
from PyQt5.QtGui import QTextCharFormat


class FormatOperations:
    def __init__(self, text_edit: QTextEdit, size_spin_box: QSpinBox):
        self.text_edit = text_edit
        self.size_spin_box = size_spin_box
        self.size_spin_box.valueChanged.connect(self.change_size)

    def select_font(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()
        else:
            current_font = self.text_edit.currentFont()

        font, ok = QFontDialog.getFont(current_font)
        if ok:
            self.change_format({'font': font})

    def select_color(self):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_color = current_format.foreground().color()
        else:
            current_color = self.text_edit.textColor()

        color = QColorDialog.getColor(current_color)
        if color.isValid():
            self.change_format({'color': color})

    def change_size(self, size):
        self.change_format({'size': size})

    def select_size(self):
        size, ok = QInputDialog.getInt(self.text_edit, "Выбрать размер", "Размер текста:", self.size_spin_box.value(),
                                       1, 100)
        if ok:
            self.size_spin_box.setValue(size)

    def change_format(self, attrs):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            format = QTextCharFormat()

            if 'font' in attrs:
                format.setFont(attrs['font'])
            if 'color' in attrs:
                format.setForeground(attrs['color'])
            if 'size' in attrs:
                format.setFontPointSize(attrs['size'])

            cursor.mergeCharFormat(format)
        else:
            format = self.text_edit.currentCharFormat()

            if 'font' in attrs:
                format.setFont(attrs['font'])
            if 'color' in attrs:
                format.setForeground(attrs['color'])
            if 'size' in attrs:
                format.setFontPointSize(attrs['size'])

            self.text_edit.setCurrentCharFormat(format)
