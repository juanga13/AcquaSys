import sys

import AquaDB

from alphaversion2.GuiWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.home()

    def home(self):
        self.home_widget = HomeWidget()

        self.central_widget.addWidget(self.home_widget)
        self.central_widget.setCurrentWidget(self.home_widget)

        self.home_widget.add_button.clicked.connect(self.add)
        self.home_widget.search_button.clicked.connect(self.search)
        self.home_widget.quit_button.clicked.connect(self.quit_application)

    def add(self):
        self.add_widget = AddWidget()

        self.central_widget.addWidget(self.add_widget)
        self.central_widget.setCurrentWidget(self.add_widget)

        self.add_widget.photo_select_button.clicked.connect(self.select_photo)
        self.add_widget.photo_see_button.clicked.connect(self.see_photo)
        self.add_widget.accept_button.clicked.connect(self.validate_new_student)
        self.add_widget.back_button.clicked.connect(self.home)

        def select_photo():
            print("selecting photo")
            self.add_widget.photo_path = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',
                                                                     "Image files (*.jpg *.gif)")
            self.add_widget.photo_confirm_label = "Seleccionada"
            print(self.add_widget.photo_path + " is the path")

        def see_photo():
            print("showing photo... pass")

    def search(self):
        self.search_widget = SearchWidget()

        self.central_widget.addWidget(self.search_widget)
        self.central_widget.setCurrentWidget(self.search_widget)

        text = self.search_widget.search_edit.text()
        self.search_widget.search_edit.textChanged.connect(AquaDB.filtered_list_giver(self))
        self.search_widget.search_button.clicked.connect() # nothing for now

        # see buttons events
        for i in self.search_widget.see_button_list:
            names = self.search_widget.complete_name_list
            button = self.search_widget.see_button_list[i]

            button.clicked.connect(self.show_student_form(names[i]))

        self.asd = QDialog
        self.asd.setLayout()


        # delete buttons events
        for i in self.search_widget.delete_button_list:


        def show_student_form(complete_name):
            a_student_form = AquaDB.single_student_data(complete_name)

            complete_name = a_student_form[0]
            birthday = a_student_form[1]
            start_date = a_student_form[2]

            photo_path = a_student_form[3]

            phone = a_student_form[4]
            address = a_student_form[5]
            dni = a_student_form[6]
            email = a_student_form[7]
            social_plan = a_student_form[8]
            affiliate_number = a_student_form[9]

            complete_name_father = a_student_form[10]
            fathers_phone = a_student_form[11]
            complete_name_mother = a_student_form[12]
            mothers_phone = a_student_form[13]

            observations = a_student_form[14]




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