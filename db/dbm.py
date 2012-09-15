import sys
import sqlite3
import hashlib

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.main import Ui_main
from ui.add import Ui_add
from ui.delete import Ui_deleter
from ui.view import Ui_viewer

from ui.composite import Ui_composite

conn = sqlite3.connect('braveirc.db')
cur = conn.cursor()

digest = lambda password: hashlib.md5(password).hexdigest()

class AddWindow(QDialog, Ui_add):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def accept(self):
        username = unicode(self.username_box.text())
        password = unicode(self.password_box.text())
        password = digest(password)
        cur.execute('INSERT INTO users (username, password) values (?, ?)',
                (username, password))
        conn.commit()
        self.close()

class DeleteWindow(QDialog, Ui_deleter):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        users = list(cur.execute('SELECT username FROM users'))
        n = 0
        for username in users:
            self.comboBox.insertItem(n, username[0])
            n += 1

    def selectUser(self):
        username = self.comboBox.currentText()
        print 'Deleted:', username # Update comboBox and/or success dialog
        cur.execute("DELETE FROM users WHERE username='%s'" %  username)
        conn.commit()


class ViewWindow(QDialog, Ui_viewer):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        user_list = list(cur.execute('SELECT username FROM users'))
        users = ''
        for index, user in enumerate(user_list):
            users += '%d: %s' % (index, user[0])
        self.users.setPlainText(users)

class MainWindow(QMainWindow, Ui_main):
    def __init__(self, close_main=False):
        self.close_main = close_main
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("main", "Brave IRC DBM", None, QApplication.UnicodeUTF8))
        self.show()

    def addUser(self):
        add = AddWindow()
        if self.close_main:
            self.close()
        add.exec_()

    def deleteUser(self):
        delete = DeleteWindow()
        if self.close_main:
            self.close()
        delete.exec_()

    def viewUsers(self):
        view = ViewWindow()
        if self.close_main:
            self.close()
        view.exec_()

class CompositeWindow(QMainWindow, Ui_composite):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("main", "Brave IRC DBM", None, QApplication.UnicodeUTF8))
        self.show()

        user_list = list(cur.execute('SELECT username FROM users'))
        users = ''
        for index, user in enumerate(user_list):
            users += '%d: %s' % (index, user[0])
            self.userBox.insertItem(index, user[0])
        self.users.setPlainText(users)


    def wreckit(self):
        print self
        username = self.userBox.currentText()
        print 'Deleted:', username # Update comboBox and/or success dialog
        cur.execute("DELETE FROM users WHERE username='%s'" %  username)
        conn.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = CompositeWindow()

    app.exec_()

conn.close()

