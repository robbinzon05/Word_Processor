from PyQt5.QtWidgets import QFileDialog, QTextEdit
from PyQt5.QtGui import QTextImageFormat


class InsertOperations:
    def __init__(self, text_edit: QTextEdit):
        self.text_edit = text_edit

    def insert_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.text_edit, "Choose image", "",
                                                   "Image Files (*.png *.jpg)",
                                                   options=options)
        if file_path:
            cursor = self.text_edit.textCursor()
            image_format = QTextImageFormat()
            image_format.setName(file_path)
            cursor.insertImage(image_format)
