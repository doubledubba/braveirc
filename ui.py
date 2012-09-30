import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.chat import Ui_chat
from gui.login import Ui_login
from gui.msg import Ui_msg

from threading import Thread
import socket
from settings import Communication, HOST




class MsgWindow(QDialog, Ui_msg): # I may just not use this.
    def __init__(self, msg, title=None):
        QDialog.__init__(self)
        self.setupUi(self)
        if not title:
            title = 'Brave IRC'
        else:
            title = 'Brave IRC: %s' % title

        self.label.setText(msg)
        self.setWindowTitle(QApplication.translate("msg", title, None, QApplication.UnicodeUTF8))
        self.exec_()

def notify(*args, **kwargs):
    print args
    print kwargs


class Update(QThread, Communication):
    def __init__(self, chat):
        self.chat = chat
        self.socket = chat.client.socket
        QThread.__init__(self)
        Communication.__init__(self, self.socket)

    def run(self):
        while True:
            text = self.recv()
            body = text['msg']
            print body
            line = '%s: %s' % (body['user'], body['body'])
            #self.chat.textEdit.appendPlainText(line)
            self.emit(SIGNAL('update(QString)'), line)



class ChatWindow(QMainWindow, Ui_chat):

    closed = pyqtSignal()

    def __init__(self, client):
        self.client = client
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("chat", "Brave IRC Chat", None, QApplication.UnicodeUTF8))

        self.update = Update(self)
        self.connect(self.update, SIGNAL('update(QString)'), self.printMsg)
        self.update.start()

    def addMsg(self):
        text = self.lineEdit.text() # get user input
        text = unicode(text)
        self.lineEdit.clear() # clear user input
        #self.textEdit.appendPlainText(text) # write user input to display
        string = {'msg': {'username': self.client.username, 'body': text}}
        self.client.send(string)

    def printMsg(self, line):
        self.textEdit.appendPlainText(line)

    def clear(self):
        self.textEdit.clear()

    def shutdown(self):
        self.close()

    def menu_settings(self):
        print 'Yay menu settings!'
        msg = MsgWindow('msg', 'title')
        msg.show()



class LoginWindow(QDialog, Ui_login):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("login", "Brave IRC Chat", None, QApplication.UnicodeUTF8))

    def authenticate(self):
        get = lambda field: unicode(getattr(self, field).text())
        credentials = get('username'), get('password')
        HOST = get('serverName').split(':')
        if len(HOST) < 2:
            HOST.append(1060)
        else:
            HOST[1] = int(HOST[1])
        HOST = tuple(HOST)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(HOST)
        self.client = Communication(sock)

        
        if self.authentic(*credentials):
            self.mainChat = ChatWindow(self.client)
            self.mainChat.closed.connect(self.show)
            self.mainChat.show()
            self.hide()
        else:
            notify('Authenticated failed!', 'Hmmmm...')
            self.close()

    def authentic(self, username, password):
        credentials = {'credentials': (username, password)}
        self.client.send(credentials)
        ok = self.client.recv()
        if ok:
            self.client.username = username
        return ok

if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = LoginWindow()

    window.show()
    app.exec_()
