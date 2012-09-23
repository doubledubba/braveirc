# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/chat.ui'
#
# Created: Sat Sep 22 22:17:25 2012
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
        chat.resize(668, 462)
        self.centralwidget = QtGui.QWidget(chat)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearButton = QtGui.QCommandLinkButton(self.widget)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.quitButon = QtGui.QCommandLinkButton(self.widget)
        self.quitButon.setObjectName(_fromUtf8("quitButon"))
        self.horizontalLayout.addWidget(self.quitButon)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QPlainTextEdit(self.widget_3)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.frame = QtGui.QFrame(self.widget_3)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.submitButton = QtGui.QPushButton(self.frame)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.horizontalLayout_2.addWidget(self.submitButton)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.verticalScrollBar = QtGui.QScrollBar(self.widget_2)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.horizontalLayout_3.addWidget(self.verticalScrollBar)
        self.verticalLayout_2.addWidget(self.widget_2)
        chat.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(chat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setTearOffEnabled(True)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        chat.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(chat)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        chat.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(chat)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout = QtGui.QAction(chat)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(chat)
        QtCore.QObject.connect(self.quitButon, QtCore.SIGNAL(_fromUtf8("clicked()")), chat.close)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QObject.connect(self.submitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), chat.addMsg)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.submitButton.animateClick)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("activated()")), chat.menu_settings)
        QtCore.QMetaObject.connectSlotsByName(chat)

    def retranslateUi(self, chat):
        chat.setWindowTitle(QtGui.QApplication.translate("chat", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("chat", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButon.setText(QtGui.QApplication.translate("chat", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("chat", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("chat", "Additional", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("chat", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("chat", "&About", None, QtGui.QApplication.UnicodeUTF8))

