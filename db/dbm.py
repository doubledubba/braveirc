import sys
import sqlite3
import hashlib

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.composite import Ui_composite

conn = sqlite3.connect('braveirc.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, '
        'username VARCHAR(255), password VARCHAR(255))')

digest = lambda password: hashlib.md5(password).hexdigest()

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


    def wreckit(self):
        print self
        username = self.userBox.currentText()
        print 'Deleted:', username # Update comboBox and/or success dialog
        cur.execute("DELETE FROM users WHERE username='%s'" %  username) #fix
        conn.commit()
        self.userBox.clear()
        self.update_info()

    def addIt(self):
        username = unicode(self.user.text())
        password = unicode(self.secret.text())
        password = digest(password)

        # check if this username exists
        cur.execute("SELECT username FROM users WHERE username='%s'" %
                username) # do it right!
        existing = cur.fetchone()
        if existing:
            print '%s already exists!' % username # failure dialog
            return
        cur.execute('INSERT INTO users (username, password) values (?, ?)',
                (username, password))
        conn.commit()
        print 'Added:', username
        self.update_info()


if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = CompositeWindow()

    app.exec_()

conn.close()

