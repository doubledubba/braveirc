import sys
import Tkinter

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.chat import Ui_main
from gui.login import Ui_login
from client import startChat


class MainWindow(QMainWindow, Ui_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def message(self):
        text = self.lineEdit.text() # get user input
        self.lineEdit.clear() # clear user input
        self.textEdit.append(text) # write user input to display


class LoginWindow(QDialog, Ui_login):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def authenticate(self):
        get = lambda field: unicode(getattr(self, field).text())
        credentials = dict(username=get('username'), password=get('password'))
        self.close()
        startChat(credentials)

if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = LoginWindow()

    window.show()
    app.exec_()
