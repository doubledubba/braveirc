import sys
import Tkinter

import easygui as eg
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base_chat import Ui_main

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
    def message(self):
        text = self.lineEdit.text() # get user input
        self.lineEdit.clear() # clear user input
        self.textEdit.append(text) # write user input to display

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


def runApp(MainWindow, argv=sys.argv):
    app = QApplication(argv, True)
    wnd = MainWindow()
    wnd.show()
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    print getCredentials()
    runApp(MainWindow)
