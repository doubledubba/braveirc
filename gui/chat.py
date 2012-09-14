# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/chat.ui'
#
# Created: Fri Sep 14 14:13:23 2012
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
        chat.resize(560, 330)
        chat.setMinimumSize(QtCore.QSize(560, 330))
        self.verticalLayout_2 = QtGui.QVBoxLayout(chat)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.buttonBar = QtGui.QHBoxLayout()
        self.buttonBar.setObjectName(_fromUtf8("buttonBar"))
        self.clear_button = QtGui.QCommandLinkButton(chat)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.buttonBar.addWidget(self.clear_button)
        self.quit_button = QtGui.QCommandLinkButton(chat)
        self.quit_button.setObjectName(_fromUtf8("quit_button"))
        self.buttonBar.addWidget(self.quit_button)
        self.verticalLayout_2.addLayout(self.buttonBar)
        self.chatBar = QtGui.QHBoxLayout()
        self.chatBar.setObjectName(_fromUtf8("chatBar"))
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
        self.submitButton = QtGui.QPushButton(self.frame)
        self.submitButton.setMaximumSize(QtCore.QSize(100, 80))
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.horizontalLayout.addWidget(self.submitButton)
        self.verticalLayout.addWidget(self.frame)
        self.chatBar.addWidget(self.widget)
        self.scrollBar = QtGui.QScrollBar(chat)
        self.scrollBar.setOrientation(QtCore.Qt.Vertical)
        self.scrollBar.setObjectName(_fromUtf8("scrollBar"))
        self.chatBar.addWidget(self.scrollBar)
        self.verticalLayout_2.addLayout(self.chatBar)

        self.retranslateUi(chat)
        QtCore.QObject.connect(self.submitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), chat.message)
        QtCore.QObject.connect(self.quit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), chat.shutdown)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), chat.clear)
        QtCore.QMetaObject.connectSlotsByName(chat)
        chat.setTabOrder(self.lineEdit, self.submitButton)
        chat.setTabOrder(self.submitButton, self.clear_button)
        chat.setTabOrder(self.clear_button, self.quit_button)
        chat.setTabOrder(self.quit_button, self.textEdit)

    def retranslateUi(self, chat):
        chat.setWindowTitle(QtGui.QApplication.translate("chat", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_button.setText(QtGui.QApplication.translate("chat", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_button.setText(QtGui.QApplication.translate("chat", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("chat", "Submit", None, QtGui.QApplication.UnicodeUTF8))

