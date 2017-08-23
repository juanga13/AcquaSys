import sys
from PyQt4.QtCore import QSize
from PyQt4.QtGui import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(100,100,300,200)
        self.setFixedSize(600, 600)

        oImage = QImage("background.png")
        sImage = oImage.scaled(QSize(self.size()))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())