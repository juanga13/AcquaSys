import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import AquaDB


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # self.setGeometry(0, 0, 500, 300)
        # self.setFixedSize(500, 300)

        # stacked widget nad 3 menus behaviour here
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.start_home_menu()

    def start_home_menu(self):
        self.home_widget = HomeWidget()

        self.central_widget.addWidget(self.home_widget)
        self.central_widget.setCurrentWidget(self.home_widget)

        self.home_widget.add_button.clicked.connect(self.start_add_menu)
        self.home_widget.search_button.clicked.connect(self.start_search_menu)
        self.home_widget.quit_button.clicked.connect(self.quit_application)

        self.show()

    def start_add_menu(self):
        self.add_widget = AddWidget()

        self.central_widget.addWidget(self.add_widget)
        self.central_widget.setCurrentWidget(self.add_widget)

        self.add_widget.photo_button.clicked.connect(self.change_photo_path_label)
        self.add_widget.see_photo_button.clicked.connect(self.show_photo)

        self.add_widget.birthday_calendar.clicked.connect(
            lambda: self.change_date_to_label(self.add_widget.birthday_label)
        )
        self.add_widget.start_date_calendar.clicked.connect(
            lambda: self.change_date_to_label(self.add_widget.start_date_label)
        )

        self.add_widget.accept_button.clicked.connect(self.validate_new_student)
        self.add_widget.back_to_home_menu_button.clicked.connect(self.start_home_menu)

    def change_date_to_label(self, label):
        label.setText(self.add_widget.birthday_calendar.selectedDate().toString())

    def change_photo_path_label(self):
        self.add_widget.photo_path_lineedit.setText(QFileDialog.getOpenFileName(self, 'Open file',
                                                    'c:\\', "Image files (*.jpg *.gif)"))
    
    def show_photo(self):
        popup = QDialog()
        popup.setWindowTitle("Ver foto")
        popup.setStandardButtons(QMessageBox.Ok)

        self.add_widget.photo_path_lineedit

    def validate_new_student(self):

        a = self.add_widget

        new_student_form = [
            a.complete_name_lineedit.text(),
            a.birthday_label.text(),
            a.start_date_label.text(),
            a.photo_path,
            a.phone_lineedit.text(),
            a.address_lineedit.text(),
            a.dni_lineedit.text(),
            a.email_lineedit.text(),
            a.social_plan_lineedit.text(),
            a.afiliate_number_lineedit.text(),
            a.complete_name_father_lineedit.text(),
            a.fathers_phone_lineedit.text(),
            a.complete_name_mother_lineedit.text(),
            a.mothers_phone_lineedit.text(),
            a.observations_textedit.toPlainText()
        ]

        AquaDB.insert_new_data(new_student_form)
        AquaDB.select_from_db()

    def start_search_menu(self):
        # self.search_widget = SearchWidget()
        pass

    def quit_application(self):
        print("clicked quit")
        choice = QMessageBox.question(self, 'Confirmar',
                                      "Realmente quiere salir?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            # log this
            print("pressed yes...\nnow exiting")
            AquaDB.finish_session()
            sys.exit()
        else:
            print("pressed no...")
            return True

    def closeEvent(self, close_event):
        # override when close window is attempted
        print("clicked close window button")
        if self.quit_application():
            close_event.ignore()


class HomeWidget(QWidget):
    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)

        self.add_button = QPushButton("Agregar nuevo alumno")
        self.search_button = QPushButton("Buscar alumno")
        self.quit_button = QPushButton("Salir")

        layout = QGridLayout()

        layout.addWidget(self.add_button, 1, 1)
        layout.addWidget(self.search_button, 2, 1)
        layout.addWidget(self.quit_button, 3, 2)

        self.setLayout(layout)
        self.setWindowTitle("AquaDB System - Inicio")

        # self.show()


class AddWidget(QWidget):
    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        self.complete_name_lineedit = QLineEdit()
        self.birthday_calendar = QCalendarWidget()
        self.birthday_label = QLabel()
        self.start_date_calendar = QCalendarWidget()
        self.start_date_label = QLabel()

        self.photo_button = QPushButton("Seleccionar foto")
        self.photo_path_lineedit = QLabel()
        self.see_photo_button = QPushButton("Ver foto")

        self.phone_lineedit = QLineEdit()
        self.phone_lineedit.setValidator(QIntValidator())

        self.address_lineedit = QLineEdit()

        self.dni_lineedit = QLineEdit()
        self.dni_lineedit.setValidator(QIntValidator())

        self.email_lineedit = QLineEdit()

        self.social_plan_lineedit = QLineEdit()
        self.afiliate_number_lineedit = QLineEdit()
        self.afiliate_number_lineedit.setValidator(QIntValidator())

        self.observations_textedit = QTextEdit()

        self.complete_name_father_lineedit = QLineEdit()
        self.fathers_phone_lineedit = QLineEdit()
        self.fathers_phone_lineedit.setValidator(QIntValidator())
        self.complete_name_mother_lineedit = QLineEdit()
        self.mothers_phone_lineedit = QLineEdit()
        self.mothers_phone_lineedit.setValidator(QIntValidator())

        self.accept_button = QPushButton("Aceptar")
        self.back_to_home_menu_button = QPushButton("Volver")

        layout = QVBoxLayout()

        name_and_photo_layout = QHBoxLayout()
        calendars_layout = QHBoxLayout()
        calendar_1_layout = QVBoxLayout()
        calendar_2_layout = QVBoxLayout()
        phone_and_address_layout = QHBoxLayout()
        dni_and_email_layout = QHBoxLayout()
        social_plan_layout = QHBoxLayout()
        father_layout = QHBoxLayout()
        mother_layout = QHBoxLayout()
        observation_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        calendars_layout.addLayout(calendar_1_layout, 0)
        calendars_layout.addLayout(calendar_2_layout, 1)

        layout.addLayout(name_and_photo_layout, 0)
        layout.addLayout(calendars_layout, 1)
        layout.addLayout(phone_and_address_layout, 2)
        layout.addLayout(dni_and_email_layout, 3)
        layout.addLayout(social_plan_layout, 4)
        layout.addLayout(father_layout, 5)
        layout.addLayout(mother_layout, 6)
        layout.addLayout(observation_layout, 7)
        layout.addLayout(buttons_layout, 8)

        name_and_photo_layout.addWidget(QLabel("Nombre completo:"))
        name_and_photo_layout.addWidget(self.complete_name_lineedit)
        name_and_photo_layout.addWidget(self.photo_button)
        name_and_photo_layout.addWidget(self.photo_path_lineedit)

        calendar_1_layout.addWidget(QLabel("Fecha de nacimiento:"))
        calendar_1_layout.addWidget(self.birthday_calendar)
        calendar_1_layout.addWidget(self.birthday_label)

        calendar_2_layout.addWidget(QLabel("Fecha de inicio:"))
        calendar_2_layout.addWidget(self.start_date_calendar)
        calendar_2_layout.addWidget(self.start_date_label)

        phone_and_address_layout.addWidget(QLabel("Telefono"))
        phone_and_address_layout.addWidget(self.phone_lineedit)
        phone_and_address_layout.addWidget(QLabel("Domicilio"))
        phone_and_address_layout.addWidget(self.address_lineedit)

        dni_and_email_layout.addWidget(QLabel("DNI:"))
        dni_and_email_layout.addWidget(self.dni_lineedit)
        dni_and_email_layout.addWidget(QLabel("e-mail:"))
        dni_and_email_layout.addWidget(self.email_lineedit)

        social_plan_layout.addWidget(QLabel("Obra social:"))
        social_plan_layout.addWidget(self.social_plan_lineedit)
        social_plan_layout.addWidget(QLabel("Numero de afiliado:"))
        social_plan_layout.addWidget(self.afiliate_number_lineedit)

        father_layout.addWidget(QLabel("Nombre del padre:"))
        father_layout.addWidget(self.complete_name_father_lineedit)
        father_layout.addWidget(QLabel("Numero (padre):"))
        father_layout.addWidget(self.fathers_phone_lineedit)

        mother_layout.addWidget(QLabel("Nombre de la madre:"))
        mother_layout.addWidget(self.complete_name_mother_lineedit)
        mother_layout.addWidget(QLabel("Numero (madre):"))
        mother_layout.addWidget(self.mothers_phone_lineedit)

        observation_layout.addWidget(QLabel("Observaciones"))
        observation_layout.addWidget(self.observations_textedit)

        buttons_layout.addWidget(self.accept_button)
        buttons_layout.addWidget(self.back_to_home_menu_button)

        self.setLayout(layout)
        self.setWindowTitle("AquaDB System - Agregar un nuevo alumno")


if __name__ == '__main__':
    AquaDB.create_table()
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
