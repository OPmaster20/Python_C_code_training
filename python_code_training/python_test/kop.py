import sys
from PyQt5.Qtwidgets import QApplication,QMainWindow,QLabel
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,400,300)
win.setWindowTitle("qgc")
win.show()
sys.exit(app.exec_())
