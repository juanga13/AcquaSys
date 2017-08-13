import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__()
        self.setFixedHeight(200)

        # Container Widget
        widget = QWidget()
        # Layout of Container Widget
        layout = QVBoxLayout(self)
        for _ in range(20):
            btn = QPushButton("test")
            layout.addWidget(btn)
        widget.setLayout(layout)

        # Scroll Area Properties
        scroll = QScrollArea()
        scroll.setWidget(widget)

        # Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = Widget()
    dialog.show()

    app.exec_()