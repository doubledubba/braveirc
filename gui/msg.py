# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/msg.ui'
#
# Created: Fri Sep 14 22:10:50 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_msg(object):
    def setupUi(self, msg):
        msg.setObjectName(_fromUtf8("msg"))
        msg.resize(272, 156)
        msg.setMinimumSize(QtCore.QSize(272, 156))
        msg.setMaximumSize(QtCore.QSize(272, 156))
        self.verticalLayout = QtGui.QVBoxLayout(msg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(msg)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtGui.QPushButton(msg)
        self.pushButton.setMaximumSize(QtCore.QSize(222, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(msg)
        QtCore.QMetaObject.connectSlotsByName(msg)

    def retranslateUi(self, msg):
        msg.setWindowTitle(QtGui.QApplication.translate("msg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("msg", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("msg", "Close", None, QtGui.QApplication.UnicodeUTF8))

