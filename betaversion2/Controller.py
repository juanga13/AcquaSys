import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from betaversion2 import Widgets, Database


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        print("[Gui] Initializing gui.")
        super(MainWindow, self).__init__(parent)

        # initialize database
        self.db = Database.DatabaseController()

        # start app method
        self.start_list_menu()

    def start_list_menu(self):
        print("[Gui] Starting list menu.")
        list_menu = Widgets.ListWidget()

        self.setWindowTitle("AquaDB System - Lista de alumnos")
        self.setFixedSize(400, 200)

        self.setCentralWidget(list_menu)

        # component actions
        list_menu.search_edit.textChanged.connect(list_menu.update_list)
        list_menu.add_button.clicked.connect(self.start_add_menu)

        print("nombres: " + str(len(list_menu.name_list)) + ". botones de agregar:" + str(len(list_menu.see_button_list)) +
              ". botones de eliminar:" + str(len(list_menu.delete_button_list)))
        for i in range(0, len(list_menu.see_button_list)):
            list_menu.see_button_list[i].clicked.connect(
                lambda: self.show_student_data(str(list_menu.name_list[i])))
        for i in range(0, len(list_menu.delete_button_list)):
            list_menu.delete_button_list[i].clicked.connect(
                lambda: self.delete_student_data(str(list_menu.name_list[i])))
        list_menu.quit_button.clicked.connect(self.quit_app)

        self.show()

    # warning, this is awful, generate a nice pdf please!
    def show_student_data(self, complete_name):
        print("[Gui] Showing attempted student data.")
        student_data_list = self.db.get_a_student(complete_name)
        """
        name=new_student_data[0]
        birthday=new_student_data[1]
        start_date=new_student_data[2]
        photo_path=new_student_data[3]
        dni=new_student_data[4]
        address=new_student_data[5]
        phone=new_student_data[6]
        email=new_student_data[7]
        social_plan=new_student_data[8]
        affiliate_number=new_student_data[9]
        father_name=new_student_data[10]
        father_number=new_student_data[11]
        mother_name=new_student_data[12]
        mother_number=new_student_data[13]
        notes=new_student_data[14]
        """

        # in future make a pdf or something
        student_data_dialog = QDialog()
        student_data_dialog.setWindowTitle("Planilla de " + student_data_list[0])
        student_data_dialog.setFixedSize(446, 631)
        dialog_layout = QVBoxLayout()
        student_data_dialog.setLayout(dialog_layout)

        first_and_photo_layout = QHBoxLayout()
        dialog_layout.addLayout(first_and_photo_layout, 0)

        first_text_layout = QVBoxLayout()
        first_and_photo_layout.addLayout(first_text_layout, 0)
        name_layout = QHBoxLayout()
        name_text = QLabel("Nombre completo:")
        name_layout.addWidget(name_text, 0)
        name = QLabel(student_data_list[0])
        name_layout.addWidget(name, 1)
        first_text_layout.addLayout(name_layout, 0)

        birthday_layout = QHBoxLayout()
        birthday_text = QLabel("Fecha de nacimiento:")
        birthday_layout.addWidget(birthday_text, 0)
        birthday = QLabel(student_data_list[1])
        birthday_layout.addWidget(birthday, 1)
        first_text_layout.addLayout(birthday_layout, 1)

        start_date_layout = QHBoxLayout()
        start_date_text = QLabel("Fecha de inicio:")
        start_date_layout.addWidget(start_date_text, 0)
        start_date = QLabel(student_data_list[2])
        start_date_layout.addWidget(start_date, 1)
        first_text_layout.addLayout(start_date_layout, 2)

        dni_layout = QHBoxLayout()
        dni_text = QLabel("DNI:")
        dni_layout.addWidget(dni_text, 0)
        dni = QLabel(str(student_data_list[4]))
        dni_layout.addWidget(dni, 1)
        first_text_layout.addWidget(dni, 3)

        photo_layout = QHBoxLayout()
        first_and_photo_layout.addLayout(photo_layout, 1)
        photo_text = QLabel("Foto:")
        photo_text.setScaledContents(True)
        photo_pixmap = QPixmap(student_data_list[3])
        photo_text.setPixmap(photo_pixmap)

        second_text_layout = QHBoxLayout()
        dialog_layout.addLayout(second_text_layout, 1)
        address_text = QLabel("Domicilio:")
        address = QLabel(student_data_list[5])
        second_text_layout.addWidget(address_text, 0)
        second_text_layout.addWidget(address, 1)
        phone_text = QLabel("Telefono:")
        phone = QLabel(student_data_list[6])
        second_text_layout.addWidget(phone_text, 2)
        second_text_layout.addWidget(phone, 3)
        email_text = QLabel("email:")
        email = QLabel(str(student_data_list[7]))
        second_text_layout.addWidget(email_text, 4)
        second_text_layout.addWidget(email, 5)

        social_layout = QHBoxLayout()
        dialog_layout.addLayout(social_layout, 2)
        social_plan_text = QLabel("Obra social:")
        social_plan = QLabel(student_data_list[8])
        social_layout.addWidget(social_plan_text, 0)
        social_layout.addWidget(social_plan, 1)
        affiliate_number_text = QLabel("Numero de asociado:")
        affiliate_number = QLabel(str(student_data_list[9]))
        social_layout.addWidget(affiliate_number_text, 2)
        social_layout.addWidget(affiliate_number, 3)

        father_mother_widget = QWidget()
        father_mother_layout = QVBoxLayout()
        father_mother_widget.setLayout(father_mother_layout)
        father_layout = QHBoxLayout()
        mother_layout = QHBoxLayout()
        father_mother_layout.addLayout(father_layout)
        father_mother_layout.addLayout(mother_layout)
        father_name_text = QLabel("Nombre del padre:")
        father_name = QLabel(student_data_list[10])
        father_layout.addWidget(father_name_text, 0)
        father_layout.addWidget(father_name, 1)
        father_number_text = QLabel("Telefono padre:")
        father_number = QLabel(str(student_data_list[11]))
        father_layout.addWidget(father_number_text, 2)
        father_layout.addWidget(father_number, 3)
        mother_name_text = QLabel("Nombre de la madre:")
        mother_name = QLabel(student_data_list[12])
        mother_layout.addWidget(mother_name_text, 0)
        mother_layout.addWidget(mother_name, 1)
        mother_number_text = QLabel("Telefono madre:")
        mother_number = QLabel(str(student_data_list[13]))
        mother_layout.addWidget(mother_number_text, 2)
        mother_layout.addWidget(mother_number, 3)

        dialog_layout.addLayout(first_and_photo_layout, 0)
        dialog_layout.addLayout(second_text_layout, 1)
        dialog_layout.addLayout(social_layout, 2)
        dialog_layout.addLayout(father_mother_layout, 3)

        confirm_buttons = QDialogButtonBox(QDialogButtonBox.Ok, Qt.Horizontal, self)
        confirm_buttons.accepted.connect(student_data_dialog.accept)
        dialog_layout.addWidget(confirm_buttons)

        student_data_dialog.exec_()

    def delete_student_data(self, complete_name):
        print("[Gui] Attemping deleting confirmation of " + complete_name)
        print("does nothing lol")
        pass

    def start_add_menu(self):
        print("[Gui] Starting add menu.")
        self.add_menu = Widgets.AddWidget()

        self.setWindowTitle("AquaDB System - Agregar nuevo alumno")
        self.setFixedSize(800, 600)

        self.setCentralWidget(self.add_menu)

        # component actions
        self.add_menu.photo_select_button.clicked.connect(self.select_student_photo)
        self.add_menu.photo_see_button.clicked.connect(self.show_student_photo)
        self.add_menu.birthday_calendar.selectionChanged.connect(
            lambda: self.add_menu.birthday_ind_label.setText(
                self.add_menu.birthday_calendar.selectedDate().toString()
            )
        )
        self.add_menu.start_date_calendar.selectionChanged.connect(
            lambda: self.add_menu.start_date_ind_label.setText(
                self.add_menu.start_date_calendar.selectedDate().toString()
            )
        )
        self.add_menu.accept_button.clicked.connect(self.validate_student)
        self.add_menu.back_button.clicked.connect(self.start_list_menu)

    def select_student_photo(self):
        print("[Gui] Selecting new student photo.")
        # should copy file and paste it on the student photo folder,
        # and then change path (when validate)
        self.add_menu.photo_path = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.png)")

    def show_student_photo(self):
        print("[Gui] Showing student photo.")
        photo_dialog = QDialog()
        photo_dialog.setFixedSize(300, 350)
        photo_dialog_layout = QVBoxLayout()
        photo_dialog.setLayout(photo_dialog_layout)

        photo_label = QLabel()
        photo_label.setScaledContents(True)
        photo_pixmap = QPixmap(self.add_menu.photo_path)
        photo_label.setPixmap(photo_pixmap)

        confirm_button = QPushButton("Aceptar")
        confirm_button.clicked.connect(photo_dialog.accept)

        photo_dialog_layout.addWidget(photo_label, 0)
        photo_dialog_layout.addWidget(confirm_button, 1)

        photo_dialog.exec_()

    def validate_student(self):
        print("[Gui] Validating new student input.")
        """
        name=new_student_data[0]
        birthday=new_student_data[1]
        start_date=new_student_data[2]
        photo_path=new_student_data[3]
        dni=new_student_data[4]
        address=new_student_data[5]
        phone=new_student_data[6]
        email=new_student_data[7]
        social_plan=new_student_data[8]
        affiliate_number=new_student_data[9]
        father_name=new_student_data[10]
        father_number=new_student_data[11]
        mother_name=new_student_data[12]
        mother_number=new_student_data[13]
        notes=new_student_data[14]
        """
        new_student_data = [
            self.add_menu.complete_name_edit.text(),
            self.add_menu.birthday_ind_label.text(),
            self.add_menu.start_date_ind_label.text(),
            self.add_menu.photo_path,
            self.add_menu.dni_edit.text(),
            self.add_menu.address_edit.text(),
            self.add_menu.phone_edit.text(),
            self.add_menu.email_edit.text(),
            self.add_menu.social_plan_edit.text(),
            self.add_menu.affiliate_edit.text(),
            self.add_menu.complete_name_father_edit.text(),
            self.add_menu.father_phone_edit.text(),
            self.add_menu.complete_name_mother_edit.text(),
            self.add_menu.mother_phone_edit.text(),
            self.add_menu.observation_edit.toPlainText()
        ]

        self.db.insert_new_student(new_student_data)

        self.add_another()

    def add_another(self):
        choice = QMessageBox.question(self, 'Confirmar',
                                      "Quiere agregar otro alumno?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.clear_inputs()
        elif choice == QMessageBox.No:
            self.clear_inputs()
            self.start_list_menu()

    def clear_inputs(self):
        self.add_menu.complete_name_edit.clear()
        self.add_menu.birthday_ind_label.clear()
        self.add_menu.start_date_ind_label.clear()
        self.add_menu.photo_path = ""
        self.add_menu.dni_edit.clear()
        self.add_menu.address_edit.clear()
        self.add_menu.phone_edit.clear()
        self.add_menu.email_edit.clear()
        self.add_menu.social_plan_edit.clear()
        self.add_menu.affiliate_edit.clear()
        self.add_menu.complete_name_father_edit.clear()
        self.add_menu.father_phone_edit.clear()
        self.add_menu.complete_name_mother_edit.clear()
        self.add_menu.mother_phone_edit.clear()
        self.add_menu.observation_edit.clear()

    def quit_app(self):
        print("[Gui] Confirm exit")
        choice = QMessageBox.question(self, 'Confirmar',
                                      "Realmente quiere salir?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("[Gui] Pressed yes: now exiting")
            self.db.finish_session()
            sys.exit()
        else:
            print("[Gui] Pressed no: quit cancelled.")
            return True

    def closeEvent(self, close_event):
        # override when close window is attempted
        print("[Gui] Clicked close window button.")
        if self.quit_app():
            close_event.ignore()
