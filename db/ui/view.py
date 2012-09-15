# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/view.ui'
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

class Ui_viewer(object):
    def setupUi(self, viewer):
        viewer.setObjectName(_fromUtf8("viewer"))
        viewer.setEnabled(True)
        viewer.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(viewer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(viewer)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.users = QtGui.QPlainTextEdit(viewer)
        self.users.setEnabled(False)
        self.users.setObjectName(_fromUtf8("users"))
        self.verticalLayout.addWidget(self.users)

        self.retranslateUi(viewer)
        QtCore.QMetaObject.connectSlotsByName(viewer)

    def retranslateUi(self, viewer):
        viewer.setWindowTitle(QtGui.QApplication.translate("viewer", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("viewer", "Users", None, QtGui.QApplication.UnicodeUTF8))

