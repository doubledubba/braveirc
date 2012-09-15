import sys
import sqlite3
import hashlib

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.composite import Ui_composite
from ui.msg import Ui_msg

conn = sqlite3.connect('braveirc.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, '
        'username VARCHAR(255), password VARCHAR(255))')

digest = lambda password: hashlib.md5(password).hexdigest()

class MsgWindow(QDialog, Ui_msg):
    def __init__(self, msg, title=None):
        if title:
            title = 'Brave IRC: %s' % title
        else:
            title = 'Brave IRC'
        QDialog.__init__(self)
        self.setupUi(self)
        self.label.setText(msg)
        self.setWindowTitle(QApplication.translate("msg", title, None, QApplication.UnicodeUTF8))
        self.show()


def notify(msg, title=None):
    window = MsgWindow(msg, title)
    window.exec_()

class CompositeWindow(QMainWindow, Ui_composite):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("main", "Brave IRC DBM", None, QApplication.UnicodeUTF8))
        self.show()
        self.update_info()

    def update_info(self):
        user_list = list(cur.execute('SELECT id, username FROM users'))
        users = ''
        for index, user in user_list:
            users += '%d: %s\n' % (index, user)
            self.userBox.insertItem(index, user)
        self.users.setPlainText(users)


    def wreckit(self): #ralph
        username = self.userBox.currentText()
        if username:
            notify('DELETED USER: %s' % username, 'success')
        else:
            notify('There are no users left in the database!', 'Uh oh')
        cur.execute("DELETE FROM users WHERE username='%s'" %  username) #fix
        conn.commit()
        self.userBox.clear()
        self.update_info()

    def addIt(self):
        username = unicode(self.user.text())
        password = unicode(self.secret.text())
        # check if this username exists
        cur.execute("SELECT username FROM users WHERE username='%s'" %
                username) # do it right!
        existing = cur.fetchone()
        if existing:
            notify('Username "%s" already exists!' % username, 'error')
            return

        if not password:
            notify('You need to enter a password first!', 'Woops!')
            return


        password = digest(password)
        cur.execute('INSERT INTO users (username, password) values (?, ?)',
                (username, password))
        conn.commit()
        notify('NEW USER: %s' % username, 'Welcome!')
        self.update_info()


def run():
    app = QApplication(sys.argv, True)
    window = CompositeWindow()
    app.exec_()

if __name__ == '__main__':
    run()

conn.close()

