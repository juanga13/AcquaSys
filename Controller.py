import os
import sys
import shutil
import pdfMaker
from PyQt4.QtGui import *
from PyQt4.QtCore import QSize
from functools import partial
import Widgets
import Database


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        print("[Gui] Initializing gui.")
        super(MainWindow, self).__init__(parent)

        self.move(50, 50)

        # initialize database
        self.db = Database.DatabaseController()

        # variable
        self.show_bool = False

        # start app method
        self.start_list_menu()

    # main menu / list menu
    def start_list_menu(self):
        # log entered list_menu window
        print("[Gui] Starting list menu.")

        # instance of widget with layout
        self.list_menu = Widgets.ListWidget()

        # window specific settings
        self.setWindowTitle("AquaDB System - Lista de alumnos")
        self.setFixedSize(400, 400)

        background_image = QImage("./resources/background.jpg")
        background_image = background_image.scaled(QSize(self.size()))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(background_image))  # 10 = Windowrole
        self.setPalette(palette)

        # show list_menu
        self.setCentralWidget(self.list_menu)

        # component actions
        self.list_menu.add_button.clicked.connect(self.start_add_menu)

        # log number of names and buttons in list
        print("nombres: " + str(len(self.list_menu.id_list)) + ". botones de agregar:" +
              str(len(self.list_menu.generate_pdf_button_list)) +
              ". botones de eliminar:" + str(len(self.list_menu.delete_button_list)))
        # log all id's
        print("id_label_list: " + str(self.list_menu.id_list))

        # log buttons actions
        print("[Controller] Iterating buttons to add event)")

        # buttons actions
        for i in range(0, len(self.list_menu.generate_pdf_button_list)):
            print("\tNow in: " + str(self.list_menu.id_list[i]))
            button_1 = self.list_menu.generate_pdf_button_list[i]
            button_1.clicked.connect(partial(self.generate_pdf, button_1))
            button_2 = self.list_menu.delete_button_list[i]
            button_2.clicked.connect(partial(self.delete_student_data, button_2))
            button_3 = self.list_menu.edit_button_list[i]
            button_3.clicked.connect(partial(self.start_edit_menu, button_3))

        # more action
        self.list_menu.quit_button.clicked.connect(self.quit_app)

        self.list_menu.search_button.clicked.connect(
            lambda: self.list_menu.update_list(self.list_menu.search_edit.text))

        # show window (does not need to be called more than once)
        if self.show_bool is False:
            self.show()

    def generate_pdf(self, button):
        aidi = button.an_id
        # log entered to function
        print("[Controller] Generate button clicked, now generating PDF with ID: " + str(aidi))

        # get student data list
        student_data = self.db.get_a_student_data(aidi)

        # make the pdf
        pdfMaker.PDF(student_data)

        # os-depending "open the pdf file"
        # if on_ubuntu is True:
        #     try:
        os.startfile("./resources/pdf_output/" + str(student_data[0]) + ".pdf")
        #     except AttributeError:
        #         pass
        # elif on_ubuntu is False:
        #     opener = "open" if sys.platform == "darwin" else "xdg-open"
        #     subprocess.call([opener, "./resources/pdf_output/" + str(student_data[0]) + ".pdf"])

    def delete_student_data(self, button):
        aidi = button.an_id

        # log entered to function
        print("[Controller] Attempting deleting confirmation of " + str(aidi))

        # confirmation window before delete
        choice = QMessageBox.question(self, 'Confirmar',
                                      "Realmente quiere eliminar este alumno?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            # log delete accepted
            print("[Controller] Pressed yes: deleting studentm.")

            self.db.delete_a_student(aidi)
            self.list_menu.update_list()

        elif choice == QMessageBox.No:
            # log delete rejected
            print("[Controller] Pressed no: deleting process cancelled.")

    # add menu
    def start_add_menu(self):
        # log add_menu window
        print("[Controller] Starting add menu.")

        # initialize add_menu widget with layout
        self.add_menu = Widgets.AddWidget()

        # window specific settings
        self.setWindowTitle("AquaDB System - Agregar nuevo alumno")
        self.setFixedSize(800, 600)

        background_image = QImage("./resources/background_2.jpg")
        background_image = background_image.scaled(QSize(self.size()))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(background_image))  # 10 = Windowrole
        self.setPalette(palette)

        # set widget on window
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
            self, 'Selecciona la foto del alumno', 'c:/', "Image files (*.jpg *.png)")

        # 1/9999999 possibilities that same photo name is made...
        self.add_menu.photo_path = "./output/photos/" + str(self.db.get_last_id_number()) + old_path[-4:]

        shutil.copy(old_path, self.add_menu.photo_path)
        print("[Controller] Photo copied on: " + self.add_menu.photo_path)

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

    # edit menu
    def start_edit_menu(self, button):
        # takes the button given and makes an editable
        aidi = button.an_id
        student_data = self.db.get_a_student_data(aidi)
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

    # default behavior
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
