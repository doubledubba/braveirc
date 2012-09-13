import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base_chat import Ui_main



class MainWindow(QMainWindow, Ui_main):
    def message(self):
        text = self.lineEdit.text() # get user input
        self.lineEdit.clear() # clear user input
        self.textEdit.append(text) # write user input to display

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


def main(argv):
    app = QApplication(argv,True)
    wnd = MainWindow()
    wnd.show()
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main(sys.argv)
