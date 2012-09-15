import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.chat import Ui_chat
from gui.login import Ui_login
from client import authentic


class ChatWindow(QMainWindow, Ui_chat):

    closed = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("chat", "Brave IRC Chat", None, QApplication.UnicodeUTF8))

    def addMsg(self):
        text = self.lineEdit.text() # get user input
        self.lineEdit.clear() # clear user input
        self.textEdit.append(text) # write user input to display

    def clear(self):
        self.textEdit.clear()

    def shutdown(self):
        self.close()

    def menu_settings(self):
        print 'Yay menu settings!'


class LoginWindow(QDialog, Ui_login):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("login", "Brave IRC Chat", None, QApplication.UnicodeUTF8))

    def authenticate(self):
        get = lambda field: unicode(getattr(self, field).text())
        credentials = dict(username=get('username'), password=get('password'))
        print credentials
        if authentic(credentials):
            self.mainChat = ChatWindow()
            self.mainChat.closed.connect(self.show)
            self.mainChat.show()
            self.hide()
        else:
            notify('Authenticated failed!', 'Hmmmm...')

if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = LoginWindow()

    window.show()
    app.exec_()
