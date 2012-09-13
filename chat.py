
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from base_chat import Ui_main


class MainWindow(QMainWindow, Ui_main):

    done = False

    # custom slot
    def mymethod(self):
        text = self.lineEdit.text()
        self.lineEdit.clear()
        self.textEdit.setText(text + '\n')
        print 'User:', text

    def __init__(self):
        QMainWindow.__init__(self)
      
       # set up User Interface (widgets, layout...)
        self.setupUi(self)
        # custom slots connections
        QObject.connect(self.pushButton,SIGNAL("released()"),self.mymethod) # signal/slot connection

    
# Main entry to program.  Sets up the main app and create a new window.
def main(argv):
   
    # create Qt application
    app = QApplication(argv,True)
 
    # create main window
    wnd = MainWindow() # classname
    wnd.show()
    
    # Connect signal for app finish
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    
    # Start the app up
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main(sys.argv)
