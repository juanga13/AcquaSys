import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import AquaSys


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(100, 100, 500, 300)
        self.setFixedSize(500, 300)

        self.start_home_menu()

    def app_start(self):
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            w = MainWindow()
            sys.exit(app.exec_())

    def start_home_menu(self):
        self.home_menu_widget = HomeWidget(self)

        self.home_menu_widget.add_menu_button.clicked.connect(self.start_add_menu)
        self.home_menu_widget.search_menu_button.clicked.connect(self.start_search_menu)
        self.home_menu_widget.quit_button.clicked.connect(self.quit_app)

        self.setCentralWidget(self.home_menu_widget)

        # self.show()

    def start_add_menu(self):
        self.add_menu_widget = AddWidget(self)

        self.add_menu_widget.back_to_home_button.clicked.connect(self.start_home_menu)

        # self.add_menu_widget.accept_button.clicked.connect()



        self.setCentralWidget(self.add_menu_widget)

        # self.show()

    def validate_new_student(self, add_menu_widget):
        self.new_student = AquaSys.Student()
        self.new_student.complete_name = self.add_menu_widget.complete_name_lineedit.text()
        self.new_student.phone = self.add_menu_widget.phone_spinbox.value()
        print(self.new_student)

    def start_search_menu(self):
        self.start_menu_widget = SearchWidget(self)

        self.start_menu_widget.back_to_home_button.clicked.connect(self.start_home_menu)

        self.setCentralWidget(self.start_menu_widget)

        # self.show()

    def quit_app(self):
        print("clicked quit")
        choice = QMessageBox.question(self, 'Confirmar',
                                            "Realmente quiere salir?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            # log this
            print("pressed yes...\nnow exiting")
            sys.exit()
        else:
            print("pressed no...")
            return True

    def closeEvent(self, close_event):
        # override when close window is attempted
        print("clicked close window button")
        if self.quit_app():
            close_event.ignore()


class HomeWidget(QWidget):

    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)

        self.setWindowTitle("AquaDB System - Inicio")
        layout = QVBoxLayout()

        self.add_menu_button = QPushButton("Agregar nuevo alumno")
        self.search_menu_button = QPushButton("Buscar alumno")
        self.quit_button = QPushButton("Salir")

        self.add_menu_button.setGeometry(50, 50, 200, 50)
        self.search_menu_button.setGeometry(50, 150, 125, 50)
        self.quit_button.setGeometry(375, 225, 100, 50)

        # self.add_menu_button.setAligment(Qt.AlignRight)
        # self.search_menu_button.setAligment(Qt.AlignRight)
        # self.quit_button.setAligment(Qt.AlignRight)

        layout.addWidget(self.add_menu_button)
        layout.addWidget(self.search_menu_button)
        layout.addWidget(self.quit_button)


class AddWidget(QWidget):

    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        self.setWindowTitle("AquaDB System - Agregar nuevo alumno")
        layout = QLayout

        self.back_to_home_button = QPushButton("Volver", self)
        self.accept_button = QPushButton("Aceptar", self)
        self.complete_name_lineedit = QLineEdit("hola")
        self.phone_spinbox = QSpinBox()

        self.back_to_home_button.setGeometry(375, 225, 100, 50)
        self.accept_button.setGeometry(50, 225, 100, 50)
        self.complete_name_lineedit.setGeometry(50, 120, 100, 50)
        self.phone_spinbox.setGeometry(50, 20, 100, 50)

        layout.addWidget(self.back_to_home_button)

        self.setLayout(layout)





class SearchWidget(QWidget):

    def __init__(self, parent=None):
        super(SearchWidget, self).__init__(parent)

        self.setWindowTitle("AquaDB System - Buscar alumno")

        self.back_to_home_button = QPushButton("Volver", self)
        # add other stuff

        self.back_to_home_button.setGeometry(375, 225, 100, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())