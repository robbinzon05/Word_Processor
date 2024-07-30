from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBar = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setStyleSheet("QPushButton{\n"
"    background-color: #F0F0F0;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(247, 247, 247);\n"
"}")
        self.toolBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBar.setObjectName("toolBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.toolBar)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newFileBut = QtWidgets.QPushButton(self.toolBar)
        self.newFileBut.setStyleSheet("background-color: ;")
        self.newFileBut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/new-document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFileBut.setIcon(icon)
        self.newFileBut.setObjectName("newFileBut")
        self.horizontalLayout_2.addWidget(self.newFileBut)
        self.openFileBut = QtWidgets.QPushButton(self.toolBar)
        self.openFileBut.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFileBut.setIcon(icon1)
        self.openFileBut.setObjectName("openFileBut")
        self.horizontalLayout_2.addWidget(self.openFileBut)
        self.saveBut = QtWidgets.QPushButton(self.toolBar)
        self.saveBut.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBut.setIcon(icon2)
        self.saveBut.setObjectName("saveBut")
        self.horizontalLayout_2.addWidget(self.saveBut)
        self.fontBut = QtWidgets.QPushButton(self.toolBar)
        self.fontBut.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fontBut.setIcon(icon3)
        self.fontBut.setObjectName("fontBut")
        self.horizontalLayout_2.addWidget(self.fontBut)
        self.textSizeBut = QtWidgets.QPushButton(self.toolBar)
        self.textSizeBut.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/text-size.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.textSizeBut.setIcon(icon4)
        self.textSizeBut.setObjectName("textSizeBut")
        self.horizontalLayout_2.addWidget(self.textSizeBut)
        self.colorBut = QtWidgets.QPushButton(self.toolBar)
        self.colorBut.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorBut.setIcon(icon5)
        self.colorBut.setObjectName("colorBut")
        self.horizontalLayout_2.addWidget(self.colorBut)
        self.boldBut = QtWidgets.QPushButton(self.toolBar)
        self.boldBut.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boldBut.setIcon(icon6)
        self.boldBut.setObjectName("boldBut")
        self.horizontalLayout_2.addWidget(self.boldBut)
        self.italicBut = QtWidgets.QPushButton(self.toolBar)
        self.italicBut.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../icons/italic-font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italicBut.setIcon(icon7)
        self.italicBut.setObjectName("italicBut")
        self.horizontalLayout_2.addWidget(self.italicBut)
        self.underlineBut = QtWidgets.QPushButton(self.toolBar)
        self.underlineBut.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../icons/underline-text-option.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underlineBut.setIcon(icon8)
        self.underlineBut.setObjectName("underlineBut")
        self.horizontalLayout_2.addWidget(self.underlineBut)
        self.pushButton = QtWidgets.QPushButton(self.toolBar)
        self.pushButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../icons/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon9)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.redoBut = QtWidgets.QPushButton(self.toolBar)
        self.redoBut.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../icons/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoBut.setIcon(icon10)
        self.redoBut.setObjectName("redoBut")
        self.horizontalLayout_2.addWidget(self.redoBut)
        self.undoBut = QtWidgets.QPushButton(self.toolBar)
        self.undoBut.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoBut.setIcon(icon11)
        self.undoBut.setObjectName("undoBut")
        self.horizontalLayout_2.addWidget(self.undoBut)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.toolBar)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../icons/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon12)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon13)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon14)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon15)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.actionColor = QtWidgets.QAction(MainWindow)
        self.actionColor.setObjectName("actionColor")
        self.actionSize = QtWidgets.QAction(MainWindow)
        self.actionSize.setObjectName("actionSize")
        self.actionFont_2 = QtWidgets.QAction(MainWindow)
        self.actionFont_2.setIcon(icon3)
        self.actionFont_2.setObjectName("actionFont_2")
        self.actionSize_2 = QtWidgets.QAction(MainWindow)
        self.actionSize_2.setIcon(icon4)
        self.actionSize_2.setObjectName("actionSize_2")
        self.actionColor_2 = QtWidgets.QAction(MainWindow)
        self.actionColor_2.setIcon(icon5)
        self.actionColor_2.setObjectName("actionColor_2")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuFormat.addAction(self.actionFont_2)
        self.menuFormat.addAction(self.actionSize_2)
        self.menuFormat.addAction(self.actionColor_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Processor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.actionOpen.setText(_translate("MainWindow", "Open      Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save       Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy   Ctrl+C"))
        self.actionCopy.setIconText(_translate("MainWindow", "Copy   Ctrl+C"))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy   Ctrl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut      Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste   Ctrl+V"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionSize.setText(_translate("MainWindow", "Size"))
        self.actionFont_2.setText(_translate("MainWindow", "Font"))
        self.actionSize_2.setText(_translate("MainWindow", "Size"))
        self.actionColor_2.setText(_translate("MainWindow", "Color"))
        self.actionNew.setText(_translate("MainWindow", "New       Ctrl+N"))
