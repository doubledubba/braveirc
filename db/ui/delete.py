# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/delete.ui'
#
# Created: Fri Sep 14 18:11:19 2012
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
        deleter.resize(376, 99)
        self.horizontalLayout = QtGui.QHBoxLayout(deleter)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(deleter)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_2 = QtGui.QPushButton(deleter)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(deleter)
        QtCore.QMetaObject.connectSlotsByName(deleter)

    def retranslateUi(self, deleter):
        deleter.setWindowTitle(QtGui.QApplication.translate("deleter", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("deleter", "Delete", None, QtGui.QApplication.UnicodeUTF8))

