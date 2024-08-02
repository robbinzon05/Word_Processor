from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QColorDialog, QFontDialog, \
    QInputDialog, QMessageBox
from styles_database import DatabaseManager


class NewStyleDialog(QDialog):
    def __init__(self, parent=None):
        super(NewStyleDialog, self).__init__(parent)
        self.setWindowTitle("Make new style")

        self.layout = QVBoxLayout()
        self.nameLabel = QLabel("Style name:")
        self.layout.addWidget(self.nameLabel)
        self.nameEdit = QLineEdit()
        self.layout.addWidget(self.nameEdit)

        self.fontButton = QPushButton("Choose font")
        self.layout.addWidget(self.fontButton)
        self.fontButton.clicked.connect(self.choose_font)

        self.colorButton = QPushButton("Choose color")
        self.layout.addWidget(self.colorButton)
        self.colorButton.clicked.connect(self.choose_color)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.font = None
        self.color = None

    def choose_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font = font

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

    def get_style(self):
        return {
            'name': self.nameEdit.text(),
            'font': self.font,
            'color': self.color
        }


class StyleSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super(StyleSelectionDialog, self).__init__(parent)
        self.setWindowTitle("Choice of style")
        self.db = DatabaseManager()

        self.layout = QVBoxLayout()
        self.label = QLabel("Choose style:")
        self.layout.addWidget(self.label)

        self.comboBox = QComboBox()
        self.layout.addWidget(self.comboBox)

        self.deleteButton = QPushButton("Delete style", self)
        self.layout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self.show_delete_style_dialog)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def populate_styles(self, styles):
        self.comboBox.clear()
        for style in styles:
            self.comboBox.addItem(style['name'])

    def get_selected_style(self):
        return self.comboBox.currentIndex()

    def show_delete_style_dialog(self):
        styles = self.db.get_styles()
        if styles:
            items = [s[1] for s in styles]
            a = QInputDialog(self)
            item, ok = a.getItem(self, "Delete style", "Choose style:", items, 0,
                                 False)
            if ok and item:
                self.delete_style(item, a)
        else:
            QMessageBox.warning(self.text_edit.parentWidget(), "Error!", "Make at least one style.")

    def delete_style(self, style_name, a):
        styles = self.db.get_styles()
        style_to_delete = None
        for style in styles:
            if style[1] == style_name:
                style_to_delete = style
                break
        if style_to_delete:
            self.db.remove_style(style_to_delete[0])
            QMessageBox.information(self, "Success!", f"Style '{style_name}'is deleted.")
        else:
            QMessageBox.warning(self, "Error!", f"Style '{style_name}' not found.")
