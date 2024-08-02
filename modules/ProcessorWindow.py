from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from WordProcessorDesign import Ui_MainWindow
from FileOperations import FileOperations
from EditOperations import EditOperations
from FormatOpeartions import FormatOperations
from InsertOperations import InsertOperations


class ProcessorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ProcessorWindow, self).__init__(parent)
        self.setupUi(self)

        self.file_ops = FileOperations(self.textEdit)
        self.edit_ops = EditOperations(self.textEdit)
        self.format_ops = FormatOperations(self, self.textEdit, self.spinBox)
        self.insert_ops = InsertOperations(self.textEdit)

        # FILE OPERATIONS
        self.actionNew.triggered.connect(self.file_ops.new_file)
        self.actionOpen.triggered.connect(self.file_ops.open_file)
        self.actionSave.triggered.connect(self.file_ops.save_file)

        QShortcut(QKeySequence("Ctrl+N"), self, self.file_ops.new_file)
        QShortcut(QKeySequence("Ctrl+O"), self, self.file_ops.open_file)
        QShortcut(QKeySequence("Ctrl+S"), self, self.file_ops.save_file)

        # EDIT OPERATIONS
        self.actionCopy.triggered.connect(self.edit_ops.copy)
        self.actionPaste.triggered.connect(self.edit_ops.paste)
        self.actionCut.triggered.connect(self.edit_ops.cut)

        QShortcut(QKeySequence("Ctrl+C"), self, self.edit_ops.copy)
        QShortcut(QKeySequence("Ctrl+V"), self, self.edit_ops.paste)
        QShortcut(QKeySequence("Ctrl+X"), self, self.edit_ops.cut)

        # FORMAT OPERATIONS
        self.actionFont_2.triggered.connect(self.format_ops.select_font)
        self.actionSize_2.triggered.connect(self.format_ops.select_size)
        self.actionColor_2.triggered.connect(self.format_ops.select_color)
        self.actionIndent.triggered.connect(self.format_ops.increase_indent)
        self.actionUnindent.triggered.connect(self.format_ops.decrease_indent)
        self.actionLine_Spacing.triggered.connect(self.format_ops.show_line_spacing_dialog)
        self.actionAlign_Left.triggered.connect(self.format_ops.align_left)
        self.actionAlign_Center.triggered.connect(self.format_ops.align_center)
        self.actionAlign_Right.triggered.connect(self.format_ops.align_right)
        self.actionAlign_Justify.triggered.connect(self.format_ops.justify)

        # INSERT OPERATIONS
        self.actionImage.triggered.connect(self.insert_ops.insert_image)

        # STYLES OPERATIONS
        self.actionNew_Style.triggered.connect(self.format_ops.show_new_style_dialog)
        self.actionStyles.triggered.connect(self.format_ops.show_styles_dialog)

        # TOOLBAR BUTTONS
        self.newFileBut.clicked.connect(self.file_ops.new_file)
        self.openFileBut.clicked.connect(self.file_ops.open_file)
        self.saveBut.clicked.connect(self.file_ops.save_file)
        self.fontBut.clicked.connect(self.format_ops.select_font)
        self.textSizeBut.clicked.connect(self.format_ops.select_size)
        self.colorBut.clicked.connect(self.format_ops.select_color)
        self.imgInsertBut.clicked.connect(self.insert_ops.insert_image)
        self.redoBut.clicked.connect(self.textEdit.redo)
        self.undoBut.clicked.connect(self.textEdit.undo)
        self.boldBut.clicked.connect(self.format_ops.toggle_bold)
        self.italicBut.clicked.connect(self.format_ops.toggle_italic)
        self.underlineBut.clicked.connect(self.format_ops.toggle_underline)
        self.indentBut.clicked.connect(self.format_ops.increase_indent)
        self.unindentBut.clicked.connect(self.format_ops.decrease_indent)
        self.lineSpacingBut.clicked.connect(self.format_ops.show_line_spacing_dialog)
        self.alignLeftBut.clicked.connect(self.format_ops.align_left)
        self.alignCenterBut.clicked.connect(self.format_ops.align_center)
        self.alignRightBut.clicked.connect(self.format_ops.align_right)
        self.justifyBut.clicked.connect(self.format_ops.justify)
