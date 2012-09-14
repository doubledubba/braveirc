# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/chat.ui'
#
# Created: Fri Sep 14 13:09:53 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_chat(object):
    def setupUi(self, chat):
        chat.setObjectName(_fromUtf8("chat"))
        chat.resize(583, 300)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(chat)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(chat)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(250, 10, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalScrollBar = QtGui.QScrollBar(chat)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.horizontalLayout_2.addWidget(self.verticalScrollBar)

        self.retranslateUi(chat)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pushButton.animateClick)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), chat.message)
        QtCore.QMetaObject.connectSlotsByName(chat)

    def retranslateUi(self, chat):
        chat.setWindowTitle(QtGui.QApplication.translate("chat", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("chat", "Submit", None, QtGui.QApplication.UnicodeUTF8))

