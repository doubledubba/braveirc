import sys
from PyQt4.QtGui import QApplication, QMainWindow, QGridLayout
from chat import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
#ui.verticalScrollBar.setWidget(ui.textBrowser)
ui.setupUi(window)

'''
window.show()
sys.exit(app.exec_())'''
