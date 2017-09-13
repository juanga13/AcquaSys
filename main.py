import sys

from Controller import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.setWindowIcon(QIcon(".\\resources\\icon.jpg"))
    sys.exit(app.exec_())