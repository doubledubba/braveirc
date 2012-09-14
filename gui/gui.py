import sys
import Tkinter

import easygui as eg
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base_chat import Ui_main
from base_login import Ui_login

DEBUG = False
msgbox = eg.msgbox

def getCredentials():
    '''Query user for username and password. Return as a dict

    Future: Add secure password caching
    '''

    msg = "Enter login information"
    title = "Brave IRC Network"
    fieldNames = ['Username', 'Password']
    fieldValues = []  # we start with blanks for the values
    fieldValues = eg.multpasswordbox(msg, title, fieldNames) if not DEBUG else None

    # make sure that none of the fields was left blank
    while True:
        if fieldValues == None or DEBUG: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": 
            break # no problems found
        else:
            # show the box again, with the errmsg as the message
            fieldValues = eg.multpasswordbox(errmsg, title, fieldNames, fieldValues)

    if DEBUG:
        fieldValues = 'jnaranjo', 'test'

    credentials = {'username': fieldValues[0], 'password': fieldValues[1]}

    return credentials


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
        return credentials

if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = LoginWindow()

    window.show()
    app.exec_()
