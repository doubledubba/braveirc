import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.chat import Ui_chat
from gui.login import Ui_login
from client import authentic

DEBUG = True

from pprint import pprint

class ChatWindow(QDialog, Ui_chat):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def message(self):
        text = self.lineEdit.text() # get user input
        self.lineEdit.clear() # clear user input
        self.textEdit.append(text) # write user input to display

    def clear(self):
        print 'Cleared!'
        self.textEdit.clear()

    def exit(self):
        print 'Bye!'
        self.close()

class LoginWindow(QDialog, Ui_login):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def authenticate(self):
        get = lambda field: unicode(getattr(self, field).text())
        credentials = dict(username=get('username'), password=get('password'))
        self.close()
        if authentic(credentials) or DEBUG:
            main = ChatWindow()
            main.exec_()
            print 1

if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = LoginWindow()

    window.show()
    app.exec_()
