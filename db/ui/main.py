# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Fri Sep 14 15:36:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(189, 186)
        main.setMinimumSize(QtCore.QSize(189, 186))
        main.setMaximumSize(QtCore.QSize(189, 186))
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 189, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBrave_IRC_DBM = QtGui.QMenu(self.menubar)
        self.menuBrave_IRC_DBM.setObjectName(_fromUtf8("menuBrave_IRC_DBM"))
        main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(main)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuBrave_IRC_DBM.addAction(self.actionQuit)
        self.menubar.addAction(self.menuBrave_IRC_DBM.menuAction())

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        main.setWindowTitle(QtGui.QApplication.translate("main", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("main", "Add User", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("main", "Delete User", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("main", "View Users", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBrave_IRC_DBM.setTitle(QtGui.QApplication.translate("main", "Brave IRC DBM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("main", "Quit", None, QtGui.QApplication.UnicodeUTF8))

