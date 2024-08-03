import webbrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QInputDialog, QMessageBox
from PyQt5.QtGui import QTextImageFormat, QTextCursor


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

    def update_open_link(self):
        cursor = self.text_edit.textCursor()
        if self.is_link_selected(cursor):
            self.open_link()

    def show_link_dialog(self, url):
        reply = QMessageBox.question(self.text_edit.parentWidget(), 'Following a link',
                                     f'Do you want to follow the link?: {url}?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            webbrowser.open(QUrl(url).toString())

    def open_link(self):
        cursor = self.text_edit.textCursor()
        if self.is_link_selected(cursor):
            link_format = cursor.charFormat()
            url = link_format.anchorHref()
            if url:
                self.show_link_dialog(url)

    def is_link_selected(self, cursor):
        cursor.select(QTextCursor.WordUnderCursor)
        link_format = cursor.charFormat()
        return link_format.isAnchor()

    def insert_link(self):
        link_text, ok1 = QInputDialog.getText(self.text_edit.parentWidget(), 'Link text',
                                              'Enter text for link:')
        if ok1 and link_text:
            url, ok2 = QInputDialog.getText(self.text_edit.parentWidget(), 'Link URL',
                                            'Enter URL for link (example: http://example.com):')
            if ok2 and url:
                cursor = self.text_edit.textCursor()

                cursor.insertHtml(f'<a href="{url}">{link_text}</a> ')

                self.text_edit.setTextCursor(cursor)
