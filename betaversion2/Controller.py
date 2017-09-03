import sys
import os
import shutil
import random
import betaversion2.pdfMaker
from PyQt4.QtCore import *
from PyQt4.QtGui import *


from betaversion2 import Widgets, Database


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        print("[Gui] Initializing gui.")
        super(MainWindow, self).__init__(parent)

        self.move(50, 50)

        # initialize database
        self.db = Database.DatabaseController()

        # start app method
        self.start_list_menu()

    def start_list_menu(self):
        print("[Gui] Starting list menu.")
        list_menu = Widgets.ListWidget()

        self.setWindowTitle("AquaDB System - Lista de alumnos")
        self.setFixedSize(400, 400)

        self.setCentralWidget(list_menu)

        # component actions
        # list_menu.search_edit.textChanged.connect(self.start_list_menu())
        list_menu.add_button.clicked.connect(self.start_add_menu)

        print("nombres: " + str(len(list_menu.id_list)) + ". botones de agregar:" + str(len(list_menu.see_button_list)) +
              ". botones de eliminar:" + str(len(list_menu.delete_button_list)))
        for i in range(0, len(list_menu.see_button_list)):
            print(list_menu.id_list[i])
            list_menu.see_button_list[i].clicked.connect(
                lambda: self.show_student_data(list_menu.id_list[i]))
        for i in range(0, len(list_menu.delete_button_list)):
            list_menu.delete_button_list[i].clicked.connect(
                lambda: self.delete_student_data(list_menu.id_list[i]))
        list_menu.quit_button.clicked.connect(self.quit_app)

        self.show()

    def show_student_data(self, aidi):
        print("[Controller] Generate button clicked, now generating PDF with ID: " + str(aidi))
        student_data = self.db.get_a_student_data(aidi)
        betaversion2.pdfMaker.PDF(student_data)
        os.startfile(".\\resources\\pdf_output\\" + str(student_data[0]) + ".pdf")

    def delete_student_data(self, aidi):
        print("[Controller] Attemping deleting confirmation of " + str(aidi))

        choice = QMessageBox.question(self, 'Confirmar',
                                      "Realmente quiere eliminar este alumno?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("[Controller] Pressed yes: deleting studentm.")
            self.db.delete_a_student(aidi)
            self.start_list_menu()
        elif choice == QMessageBox.No:
            print("[Controller] Pressed no: deleting process cancelled.")

    def start_add_menu(self):
        print("[Controller] Starting add menu.")

        self.setWindowTitle("AquaDB System - Agregar nuevo alumno")
        self.setFixedSize(800, 600)

        self.add_menu = Widgets.AddWidget()

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
        print("[Controller] Selecting new student photo.")
        # should copy file and paste it on the student photo folder,
        # and then change path (when validate)
        old_path = QFileDialog.getOpenFileName(
            self, 'Selecciona la foto del alumno', 'c:\\', "Image files (*.jpg *.png)")

        # 1/9999999 possibilities that same photo name is made...
        self.add_menu.photo_path = ".\\resources\\photos\\" + str(self.db.get_last_id_number()) + old_path[-4:]

        shutil.copy(old_path, self.add_menu.photo_path)
        print("[Controller] Photo copied")

    def show_student_photo(self):
        print("[Controller] Showing student photo.")
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
        print("[Controller] Validating new student input.")
        """
        id=new_student_data[0]
        name=new_student_data[1]
        surname=new_student_data[2]
        birthday=new_student_data[3]
        start_date=new_student_data[4]
        photo_path=new_student_data[5]
        dni=new_student_data[6]
        address=new_student_data[7]
        phone=new_student_data[8]
        email=new_student_data[9]
        social_plan=new_student_data[10]
        affiliate_number=new_student_data[11]
        father_name=new_student_data[12]
        father_number=new_student_data[13]
        mother_name=new_student_data[14]
        mother_number=new_student_data[15]
        notes=new_student_data[16]
        """
        new_student_data = [
            0,
            self.add_menu.name_edit.text(),
            self.add_menu.surname_edit.text(),
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
        self.add_menu.name_edit.clear()
        self.add_menu.surname_edit.clear()
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
        print("[Controller] Confirm exit")
        choice = QMessageBox.question(self, 'Confirmar',
                                      "Realmente quiere salir?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("[Controller] Pressed yes: now exiting")
            self.db.finish_session()
            sys.exit()
        else:
            print("[Controller] Pressed no: quit cancelled.")
            return True

    def closeEvent(self, close_event):
        # override when close window is attempted
        print("[Controller] Clicked close window button.")
        if self.quit_app():
            close_event.ignore()
