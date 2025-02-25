from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 820)
        MainWindow.setStyleSheet("")
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
        self.spinBox = QtWidgets.QSpinBox(self.toolBar)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(72)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
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
        self.imgInsertBut = QtWidgets.QPushButton(self.toolBar)
        self.imgInsertBut.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../icons/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imgInsertBut.setIcon(icon9)
        self.imgInsertBut.setObjectName("imgInsertBut")
        self.horizontalLayout_2.addWidget(self.imgInsertBut)
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
        self.indentBut = QtWidgets.QPushButton(self.toolBar)
        self.indentBut.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../icons/indent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.indentBut.setIcon(icon12)
        self.indentBut.setObjectName("indentBut")
        self.horizontalLayout_2.addWidget(self.indentBut)
        self.unindentBut = QtWidgets.QPushButton(self.toolBar)
        self.unindentBut.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../icons/unindent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unindentBut.setIcon(icon13)
        self.unindentBut.setObjectName("unindentBut")
        self.horizontalLayout_2.addWidget(self.unindentBut)
        self.lineSpacingBut = QtWidgets.QPushButton(self.toolBar)
        self.lineSpacingBut.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../icons/line-spacing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lineSpacingBut.setIcon(icon14)
        self.lineSpacingBut.setObjectName("lineSpacingBut")
        self.horizontalLayout_2.addWidget(self.lineSpacingBut)
        self.alignLeftBut = QtWidgets.QPushButton(self.toolBar)
        self.alignLeftBut.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../icons/align-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignLeftBut.setIcon(icon15)
        self.alignLeftBut.setObjectName("alignLeftBut")
        self.horizontalLayout_2.addWidget(self.alignLeftBut)
        self.alignCenterBut = QtWidgets.QPushButton(self.toolBar)
        self.alignCenterBut.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../icons/format.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignCenterBut.setIcon(icon16)
        self.alignCenterBut.setObjectName("alignCenterBut")
        self.horizontalLayout_2.addWidget(self.alignCenterBut)
        self.alignRightBut = QtWidgets.QPushButton(self.toolBar)
        self.alignRightBut.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../icons/align-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alignRightBut.setIcon(icon17)
        self.alignRightBut.setObjectName("alignRightBut")
        self.horizontalLayout_2.addWidget(self.alignRightBut)
        self.justifyBut = QtWidgets.QPushButton(self.toolBar)
        self.justifyBut.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../icons/justify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.justifyBut.setIcon(icon18)
        self.justifyBut.setObjectName("justifyBut")
        self.horizontalLayout_2.addWidget(self.justifyBut)
        self.linkBut = QtWidgets.QPushButton(self.toolBar)
        self.linkBut.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("../icons/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkBut.setIcon(icon19)
        self.linkBut.setObjectName("linkBut")
        self.horizontalLayout_2.addWidget(self.linkBut)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.toolBar)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1053, 1065))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 1043))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(793, 0))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
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
        self.menuInsert = QtWidgets.QMenu(self.menubar)
        self.menuInsert.setObjectName("menuInsert")
        self.menuStyle = QtWidgets.QMenu(self.menubar)
        self.menuStyle.setObjectName("menuStyle")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("../icons/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon20)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("../icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon21)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("../icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon22)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("../icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon23)
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
        self.actionImage = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("../icons/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImage.setIcon(icon24)
        self.actionImage.setObjectName("actionImage")
        self.actionLink = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("icons/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLink.setIcon(icon25)
        self.actionLink.setObjectName("actionLink")
        self.actionLink_2 = QtWidgets.QAction(MainWindow)
        self.actionLink_2.setIcon(icon25)
        self.actionLink_2.setObjectName("actionLink_2")
        self.actionIndent = QtWidgets.QAction(MainWindow)
        self.actionIndent.setIcon(icon12)
        self.actionIndent.setObjectName("actionIndent")
        self.actionUnindent = QtWidgets.QAction(MainWindow)
        self.actionUnindent.setIcon(icon13)
        self.actionUnindent.setObjectName("actionUnindent")
        self.actionLine_Spacing = QtWidgets.QAction(MainWindow)
        self.actionLine_Spacing.setIcon(icon14)
        self.actionLine_Spacing.setObjectName("actionLine_Spacing")
        self.actionAlign_Left = QtWidgets.QAction(MainWindow)
        self.actionAlign_Left.setIcon(icon15)
        self.actionAlign_Left.setObjectName("actionAlign_Left")
        self.actionAlign_Center = QtWidgets.QAction(MainWindow)
        self.actionAlign_Center.setIcon(icon16)
        self.actionAlign_Center.setObjectName("actionAlign_Center")
        self.actionAlign_Right = QtWidgets.QAction(MainWindow)
        self.actionAlign_Right.setIcon(icon17)
        self.actionAlign_Right.setObjectName("actionAlign_Right")
        self.actionAlign_Justify = QtWidgets.QAction(MainWindow)
        self.actionAlign_Justify.setIcon(icon18)
        self.actionAlign_Justify.setObjectName("actionAlign_Justify")
        self.actionNew_Style = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("../icons/new_style.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Style.setIcon(icon26)
        self.actionNew_Style.setObjectName("actionNew_Style")
        self.actionStyles = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("../icons/styles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStyles.setIcon(icon27)
        self.actionStyles.setObjectName("actionStyles")
        self.actionLink_3 = QtWidgets.QAction(MainWindow)
        self.actionLink_3.setIcon(icon19)
        self.actionLink_3.setObjectName("actionLink_3")
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
        self.menuFormat.addAction(self.actionIndent)
        self.menuFormat.addAction(self.actionUnindent)
        self.menuFormat.addAction(self.actionLine_Spacing)
        self.menuFormat.addAction(self.actionAlign_Left)
        self.menuFormat.addAction(self.actionAlign_Center)
        self.menuFormat.addAction(self.actionAlign_Right)
        self.menuFormat.addAction(self.actionAlign_Justify)
        self.menuInsert.addAction(self.actionImage)
        self.menuInsert.addAction(self.actionLink_3)
        self.menuStyle.addAction(self.actionNew_Style)
        self.menuStyle.addAction(self.actionStyles)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.menubar.addAction(self.menuStyle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Processor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuInsert.setTitle(_translate("MainWindow", "Insert"))
        self.menuStyle.setTitle(_translate("MainWindow", "Style"))
        self.actionOpen.setText(_translate("MainWindow", "Open      Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save       Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as   Ctrl+Shift+S"))
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
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionLink.setText(_translate("MainWindow", "Link"))
        self.actionLink_2.setText(_translate("MainWindow", "Link"))
        self.actionIndent.setText(_translate("MainWindow", "Indent"))
        self.actionUnindent.setText(_translate("MainWindow", "Unindent"))
        self.actionLine_Spacing.setText(_translate("MainWindow", "Line Spacing"))
        self.actionAlign_Left.setText(_translate("MainWindow", "Align Left"))
        self.actionAlign_Center.setText(_translate("MainWindow", "Align Center"))
        self.actionAlign_Right.setText(_translate("MainWindow", "Align Right"))
        self.actionAlign_Justify.setText(_translate("MainWindow", "Align Justify"))
        self.actionNew_Style.setText(_translate("MainWindow", "New Style"))
        self.actionStyles.setText(_translate("MainWindow", "Styles"))
        self.actionLink_3.setText(_translate("MainWindow", "Link"))
