import sys

from PyQt4.QtGui import *

from betaversion1 import Widgets
from betaversion1 import AquaDB


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # set changeable menus
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # initialize menus
        self.add_widget = Widgets.AddWidget()

        # start method
        self.list_menu()

    def list_menu(self):
        # change the menu visually
        self.list_widget = Widgets.ListWidget()
        self.central_widget.addWidget(self.list_widget)
        self.central_widget.setCurrentWidget(self.list_widget)

        # set components actions
        # self.list_widget.search_edit.textChanged.connect()
        self.list_widget.add_button.clicked.connect(self.add_menu)
        for i in range(0, len(self.list_widget.name_list)):
            self.list_widget.see_button_list[i].clicked.connect(
                lambda: self.show_student_data(str(self.list_widget.name_list[i])))
        for i in range(0, len(self.list_widget.name_list)):
            self.list_widget.delete_button_list[i].clicked.connect(
                lambda: AquaDB.delete_single_student_data(self.list_widget.name_list[i])
            )
        self.list_widget.quit_button.clicked.connect(self.quit_application)

        self.show()

    def update_list(self, name_list):
        print("updating list of students")

        for i in range(0, len(AquaDB.get_students_name_list())):

            temp_layout = QHBoxLayout()
            temp_layout.addWidget(QLabel(self.name_list[i]), 0)

            see_button = QPushButton("Ver alumno")
            self.see_button_list.append(see_button)
            temp_layout.addWidget(see_button, 1)

            delete_button = QPushButton("Eliminar alumno")
            self.delete_button_list.append(delete_button)
            temp_layout.addWidget(delete_button, 2)

            scroll_area_widget_layout.addLayout(temp_layout)

        name_list = new_name_list

    def add_menu(self):
        # change the menu visually
        self.central_widget.addWidget(self.add_widget)
        self.central_widget.setCurrentWidget(self.add_widget)

        # set components actions
        self.add_widget.photo_select_button.clicked.connect(self.select_student_photo)
        self.add_widget.photo_see_button.clicked.connect(self.show_student_photo)
        self.add_widget.birthday_calendar.selectionChanged.connect(
            lambda: self.add_widget.birthday_ind_label.setText(
                self.add_widget.birthday_calendar.selectedDate().toString()
            )
        )
        self.add_widget.start_date_calendar.selectionChanged.connect(
            lambda: self.add_widget.start_date_ind_label.setText(
                self.add_widget.start_date_calendar.selectedDate().toString()
            )
        )
        self.add_widget.accept_button.clicked.connect(self.validate_student)
        self.add_widget.back_button.clicked.connect(self.list_menu)

    def show_student_data(self, student_name):
        popup_window = QDialog()
        popup_layout = QVBoxLayout()
        student_data = AquaDB.get_single_student_data(student_name)

        """
        1 nombre_completo, 2 nacimiento, 3 fecha_de_inicio,
        4 direccion_foto, 5 telefono, 6 domicilio, 7 dni, 8 email, 
        9 nombre_completo_padre, 10 numero_padre, 11 nombre_completo_madre, 
        12 numero_madre, 13 obra_social, 14 numero_afiliado, 15 observaciones
        """

        complete_name = QLabel(student_data[0])
        birthday = QLabel(student_data[1])
        start_date = QLabel(student_data[2])
        print(student_data[3])
        photo_pixmap = QPixmap(student_data[3])
        photo = QLabel()
        photo.setPixmap(photo_pixmap)
        phone = QLabel(str(student_data[4]))
        address = QLabel(student_data[5])
        dni = QLabel(str(student_data[6]))
        email = QLabel(student_data[7])
        father_complete_name = QLabel(student_data[8])
        father_phone = QLabel(str(student_data[9]))
        mother_complete_name = QLabel(student_data[10])
        mother_phone = QLabel(str(student_data[11]))
        social_plan = QLabel(student_data[12])
        affiliate_number = QLabel(str(student_data[13]))
        observations = QLabel(student_data[14])

        complete_name_and_photo_layout = QHBoxLayout()
        complete_name_and_photo_layout.addWidget(complete_name)
        complete_name_and_photo_layout.addWidget(photo)
        birthday_and_start_date_layout = QHBoxLayout()
        birthday_and_start_date_layout.addWidget(birthday)
        birthday_and_start_date_layout.addWidget(start_date)
        phone_and_address_layout = QHBoxLayout()
        phone_and_address_layout.addWidget(phone)
        phone_and_address_layout.addWidget(address)
        dni_and_email_layout = QHBoxLayout()
        dni_and_email_layout.addWidget(dni)
        dni_and_email_layout.addWidget(email)
        father_layout = QHBoxLayout()
        father_layout.addWidget(father_complete_name)
        father_layout.addWidget(father_phone)
        mother_layout = QHBoxLayout()
        mother_layout.addWidget(mother_complete_name)
        mother_layout.addWidget(mother_phone)
        social_plan_and_affiliate_number_layout = QHBoxLayout()
        social_plan_and_affiliate_number_layout.addWidget(social_plan)
        social_plan_and_affiliate_number_layout.addWidget(affiliate_number)

        popup_layout.addLayout(complete_name_and_photo_layout, 0)
        popup_layout.addLayout(birthday_and_start_date_layout, 1)
        popup_layout.addLayout(phone_and_address_layout, 2)
        popup_layout.addLayout(dni_and_email_layout, 3)
        popup_layout.addLayout(father_layout, 4)
        popup_layout.addLayout(mother_layout, 5)
        popup_layout.addLayout(social_plan_and_affiliate_number_layout, 6)
        popup_layout.addWidget(observations, 7)

        popup_window.setLayout(popup_layout)

        popup_window.exec_()

    def select_student_photo(self):
        self.add_widget.photo_path = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.png)")
        # copyfile(self.add_widget.photo_path, "alphaversion2/student_photos/")

    def show_student_photo(self):
        photo_popup_window = QDialog()
        photo_popup_window_layout = QVBoxLayout()
        photo = QLabel()
        photo_pixmap = QPixmap(self.add_widget.photo_path)
        photo.setPixmap(photo_pixmap)
        accept_button = QPushButton("Aceptar")
        accept_button.clicked.connect(photo_popup_window.accept)

        photo_popup_window_layout.addWidget(photo, 0)
        photo_popup_window_layout.addWidget(accept_button, 1)

        photo_popup_window.setLayout(photo_popup_window_layout)

        photo_popup_window.exec_()

    def validate_student(self):
        new_student_data = []
        """
        1 nombre_completo, 2 nacimiento, 3 fecha_de_inicio,
        4 direccion_foto, 5 telefono, 6 domicilio, 7 dni, 8 email, 
        9 nombre_completo_padre, 10 numero_padre, 11 nombre_completo_madre, 
        12 numero_madre, 13 obra_social, 14 numero_afiliado, 15 observaciones
        """
        nombre_completo = self.add_widget.complete_name_edit.text()
        nacimiento = self.add_widget.birthday_ind_label.text()
        fecha_de_inicio = self.add_widget.start_date_ind_label.text()
        direccion_foto = self.add_widget.photo_path
        telefono = self.add_widget.phone_edit.text()
        domicilio = self.add_widget.address_edit.text()
        dni = self.add_widget.dni_edit.text()
        email = self.add_widget.email_edit.text()
        nombre_completo_padre = self.add_widget.complete_name_father_edit.text()
        numero_padre = self.add_widget.father_phone_edit.text()
        nombre_completo_madre = self.add_widget.complete_name_mother_edit.text()
        numero_madre = self.add_widget.mother_phone_edit.text()
        obra_social = self.add_widget.social_plan_edit.text()
        numero_afiliado = self.add_widget.affiliate_edit.text()
        observaciones = self.add_widget.observation_edit.toPlainText()

        new_student_data.append(nombre_completo)
        new_student_data.append(nacimiento)
        new_student_data.append(fecha_de_inicio)
        new_student_data.append(direccion_foto)
        new_student_data.append(telefono)
        new_student_data.append(domicilio)
        new_student_data.append(dni)
        new_student_data.append(email)
        new_student_data.append(nombre_completo_padre)
        new_student_data.append(numero_padre)
        new_student_data.append(nombre_completo_madre)
        new_student_data.append(numero_madre)
        new_student_data.append(obra_social)
        new_student_data.append(numero_afiliado)
        new_student_data.append(observaciones)

        AquaDB.insert_new_data(new_student_data)

        if self.add_again_confirmation():
            self.add_widget.complete_name_edit.setText("")
            self.add_widget.photo_path = ""
            self.add_widget.email_edit.setText("")
            self.add_widget.dni_edit.setText("")
            self.add_widget.phone_edit.setText("")
            self.add_widget.address_edit.setText("")
            self.add_widget.social_plan_edit.setText("")
            self.add_widget.affiliate_edit.setText("")
            self.add_widget.complete_name_father_edit.setText("")
            self.add_widget.father_phone_edit.setText("")
            self.add_widget.complete_name_mother_edit.setText("")
            self.add_widget.mother_phone_edit.setText("")
            self.add_widget.observation_edit.setText("")
        else:
            self.list_menu()

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

if __name__ == '__main__':
    AquaDB.create_table()
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())