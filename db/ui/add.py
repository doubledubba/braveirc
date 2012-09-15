# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add.ui'
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

class Ui_add(object):
    def setupUi(self, add):
        add.setObjectName(_fromUtf8("add"))
        add.resize(347, 221)
        add.setMinimumSize(QtCore.QSize(347, 221))
        self.verticalLayout = QtGui.QVBoxLayout(add)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(add)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.username_box = QtGui.QLineEdit(add)
        self.username_box.setObjectName(_fromUtf8("username_box"))
        self.horizontalLayout.addWidget(self.username_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(add)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_box = QtGui.QLineEdit(add)
        self.password_box.setEchoMode(QtGui.QLineEdit.Password)
        self.password_box.setObjectName(_fromUtf8("password_box"))
        self.horizontalLayout_2.addWidget(self.password_box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(add)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(add)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), add.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), add.reject)
        QtCore.QMetaObject.connectSlotsByName(add)

    def retranslateUi(self, add):
        add.setWindowTitle(QtGui.QApplication.translate("add", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("add", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("add", "Password", None, QtGui.QApplication.UnicodeUTF8))

