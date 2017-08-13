from PyQt4.QtGui import *
import sys

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.w = QWidget()
        self.setCentralWidget(self.w)
        self.layout = QVBoxLayout()

        self.i = 3
        self.list_buttons = []

        buttonless = QPushButton("less it 1")
        buttonless.clicked.connect(lambda: self.changenumber(-1))
        self.layout.addWidget(buttonless)

        buttonmore = QPushButton("add it 1")
        buttonmore.clicked.connect(lambda: self.changenumber(1))
        self.layout.addWidget(buttonmore)
        self.new_list_layout = QVBoxLayout()

        self.update_list()
        self.w.setLayout(self.layout)

    def changenumber(self, j):
        if self.i is 0 and j > 0:
            self.i += j
        elif self.i is not 0:
            self.i += j
        print("index: " + str(self.i))
        self.update_list()

    def update_list(self):
        print("buttons length: " + str(len(self.list_buttons)))
        if len(self.list_buttons) > 0:
            for i in range(0, self.i):
                self.layout.removeWidget(self.list_buttons[i])
        self.list_buttons = []

        for i in range(0, self.i):
            self.list_buttons.append(QPushButton("button n" + str(i)))
        for i in range(0, self.i):
            self.new_list_layout.addWidget(self.list_buttons[i])
        print(str(self.list_buttons))

        self.layout.addLayout(self.new_list_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mySW = MainWindow()
    mySW.show()
    sys.exit(app.exec_())