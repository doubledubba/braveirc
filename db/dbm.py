import sys
import sqlite3

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.main import Ui_main
from ui.add import Ui_add
from ui.delete import Ui_deleter

conn = sqlite3.connect('braveirc.db')
cur = conn.cursor()

class AddWindow(QDialog, Ui_add):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    def accept(self):
        username = unicode(self.username_box.text())
        password = unicode(self.password_box.text())
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


class MainWindow(QMainWindow, Ui_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("main", "Brave IRC DBM", None, QApplication.UnicodeUTF8))
        self.show()

    def addUser(self):
        add = AddWindow()
        self.close()
        add.exec_()

    def deleteUser(self):
        delete = DeleteWindow()
        self.close()
        delete.exec_()

    def viewUsers(self):
        print 'Here are all of the users!'


if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = MainWindow()

    app.exec_()

conn.close()

