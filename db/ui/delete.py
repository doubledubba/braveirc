# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/delete.ui'
#
# Created: Fri Sep 14 17:39:08 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_deleter(object):
    def setupUi(self, deleter):
        deleter.setObjectName(_fromUtf8("deleter"))
        deleter.resize(363, 99)
        self.horizontalLayout = QtGui.QHBoxLayout(deleter)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(deleter)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtGui.QPushButton(deleter)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(deleter)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), deleter.selectUser)
        QtCore.QMetaObject.connectSlotsByName(deleter)

    def retranslateUi(self, deleter):
        deleter.setWindowTitle(QtGui.QApplication.translate("deleter", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("deleter", "Delete", None, QtGui.QApplication.UnicodeUTF8))

