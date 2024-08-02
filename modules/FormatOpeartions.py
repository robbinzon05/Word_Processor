from PyQt5.QtWidgets import QColorDialog, QFontDialog, QTextEdit, QSpinBox, QInputDialog, QDialog, QVBoxLayout, QLabel, \
    QComboBox, QMessageBox
from PyQt5.QtGui import QTextCharFormat, QFont, QTextBlockFormat, QColor
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from StylesOperations import NewStyleDialog, StyleSelectionDialog
from styles_database import DatabaseManager


class LineSpacingDialog(QDialog):
    def __init__(self, parent=None):
        super(LineSpacingDialog, self).__init__(parent)
        self.setWindowTitle("Select interval")

        self.layout = QVBoxLayout()

        self.label = QLabel("Select line spacing:")
        self.layout.addWidget(self.label)

        self.comboBox = QComboBox()
        self.comboBox.addItems(["1", "1,5", "2"])
        self.layout.addWidget(self.comboBox)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def get_selected_spacing(self):
        return self.comboBox.currentText()


class FormatOperations:
    def __init__(self, parent, text_edit: QTextEdit, size_spin_box: QSpinBox):
        self.parent = parent
        self.text_edit = text_edit
        self.db = DatabaseManager()
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
        size, ok = QInputDialog.getInt(self.text_edit, "Select size", "Size of text:", self.size_spin_box.value(),
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

    def toggle_format(self, attribute):
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if attribute == QFont.Bold:
                current_format.setFontWeight(QFont.Bold if current_format.fontWeight() != QFont.Bold else QFont.Normal)
            elif attribute == QFont.StyleItalic:
                current_format.setFontItalic(not current_format.fontItalic())
            elif attribute == "Underline":
                current_format.setFontUnderline(not current_format.fontUnderline())
            cursor.setCharFormat(current_format)
        else:
            current_format = self.text_edit.currentCharFormat()
            if attribute == QFont.Bold:
                current_format.setFontWeight(QFont.Bold if current_format.fontWeight() != QFont.Bold else QFont.Normal)
            elif attribute == QFont.StyleItalic:
                current_format.setFontItalic(not current_format.fontItalic())
            elif attribute == "Underline":
                current_format.setFontUnderline(not current_format.fontUnderline())
            self.text_edit.setCurrentCharFormat(current_format)

    def toggle_bold(self):
        self.toggle_format(QFont.Bold)

    def toggle_italic(self):
        self.toggle_format(QFont.StyleItalic)

    def toggle_underline(self):
        self.toggle_format("Underline")

    def increase_indent(self):
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()

        block_format = cursor.blockFormat()
        block_format.setIndent(block_format.indent() + 1)
        cursor.setBlockFormat(block_format)

        cursor.endEditBlock()

    def decrease_indent(self):
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()

        block_format = cursor.blockFormat()
        block_format.setIndent(max(block_format.indent() - 1, 0))
        cursor.setBlockFormat(block_format)

        cursor.endEditBlock()

    def show_line_spacing_dialog(self):
        dialog = LineSpacingDialog()
        if dialog.exec_():
            selected_spacing = dialog.get_selected_spacing()
            self.set_line_spacing(selected_spacing)

    def set_line_spacing(self, spacing):
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()

        block_format = cursor.blockFormat()
        if spacing == "1":
            block_format.setLineHeight(100, QTextBlockFormat.ProportionalHeight)
        elif spacing == "1,5":
            block_format.setLineHeight(150, QTextBlockFormat.ProportionalHeight)
        elif spacing == "2":
            block_format.setLineHeight(200, QTextBlockFormat.ProportionalHeight)

        cursor.setBlockFormat(block_format)
        cursor.endEditBlock()

    def align_left(self):
        self.set_alignment(Qt.AlignLeft)

    def align_center(self):
        self.set_alignment(Qt.AlignCenter)

    def align_right(self):
        self.set_alignment(Qt.AlignRight)

    def justify(self):
        self.set_alignment(Qt.AlignJustify)

    def set_alignment(self, alignment):
        cursor = self.text_edit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(alignment)
        cursor.setBlockFormat(block_format)
        self.text_edit.setTextCursor(cursor)

    def show_new_style_dialog(self):
        dialog = NewStyleDialog()
        if dialog.exec_():
            style = dialog.get_style()
            if style['name'] and (style['font'] or style['color']):
                font_face = style['font'].family() if style['font'] else None
                font_size = style['font'].pointSize() if style['font'] else None
                font_weight = style['font'].weight() if style['font'] else None
                font_italic = style['font'].italic() if style['font'] else None
                color = style['color'].name() if style['color'] else None
                self.db.add_style(style['name'], font_face, font_size, font_weight, font_italic, color)
            else:
                QMessageBox.warning(self.parent, "Error!",
                                    "Please, write name and choose at least one style element.")

    def show_styles_dialog(self):
        styles = self.db.get_styles()
        if styles:
            dialog = StyleSelectionDialog(self.text_edit.parentWidget())
            style_list = [{'id': s[0], 'name': s[1], 'font_face': s[2], 'font_size': s[3], 'font_weight': s[4],
                           'font_italic': s[5], 'color': s[6]} for s in styles]
            dialog.populate_styles(style_list)
            if dialog.exec_():
                selected_style_index = dialog.get_selected_style()
                self.apply_style(style_list[selected_style_index])
        else:
            QMessageBox.warning(self.parent, "Error!", "At first make at least one style.")

    def apply_style(self, style):
        format = QTextCharFormat()
        font = QFont()
        if style['font_face']:
            font.setFamily(style['font_face'])
        if style['font_size']:
            font.setPointSize(style['font_size'])
        if style['font_weight']:
            font.setWeight(style['font_weight'])
        if style['font_italic']:
            font.setItalic(style['font_italic'])
        if style['color']:
            format.setForeground(QColor(style['color']))

        format.setFont(font)

        cursor = self.text_edit.textCursor()
        cursor.mergeCharFormat(format)
        self.text_edit.mergeCurrentCharFormat(format)
