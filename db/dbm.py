import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.main import Ui_main
from ui.add import Ui_add

class MainWindow(QMainWindow, Ui_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QApplication.translate("main", "Brave IRC DBM", None, QApplication.UnicodeUTF8))
        self.show()

class AddWindow(QDialog, Ui_add):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv, True)

    window = AddWindow()

    app.exec_()

