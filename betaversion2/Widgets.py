on_ubuntu = False

from PyQt4.QtGui import *
import sys
import os
if os.name is not 'nt':
    import subprocess
    on_ubuntu = True
import betaversion2.pdfMaker
from betaversion2 import Database


class ListWidget(QWidget):

    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)

        # initialize database controller
        self.db = Database.DatabaseController()

        # main window layout
        list_layout = QVBoxLayout()

        # sub-layouts
        search_and_add_layout = QHBoxLayout()
        list_layout.addLayout(search_and_add_layout)

        # components
        self.search_edit = QLineEdit()
        search_and_add_layout.addWidget(self.search_edit)
        self.search_button = QPushButton("SEARCH")
        search_and_add_layout.addWidget(self.search_button)
        self.add_button = QPushButton("Agregar nuevo alumno")
        search_and_add_layout.addWidget(self.add_button)
        self.quit_button = QPushButton("Salir")

        # scroll area thing
        scroll_area = QScrollArea()
        scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout()

        self.generate_pdf_button_list = []
        self.delete_button_list = []

        # first time list
        self.id_list = self.db.get_students_id_list()
        print("[Widgets] Creating list for first time.")
        print("\tList widget: id_list is: " + str(self.id_list) + ".")
        if len(self.id_list) is not 0:
            for i in range(0, len(self.id_list)):
                temp_layout = QHBoxLayout()

                temp_layout.addWidget(QLabel(str(self.id_list[i])))
                temp_layout.addWidget(QLabel(self.db.get_name_or_surname(self.id_list[i], 2)))

                see_button = IdButton("Generar archivo PDF", self.id_list[i])
                self.generate_pdf_button_list.append(see_button)
                temp_layout.addWidget(see_button, 1)

                delete_button = IdButton("Eliminar alumno", self.id_list[i])
                self.delete_button_list.append(delete_button)
                temp_layout.addWidget(delete_button, 2)

                self.scroll_area_layout.addLayout(temp_layout)

        scroll_area_widget.setLayout(self.scroll_area_layout)
        scroll_area.setWidget(scroll_area_widget)
        list_layout.addWidget(scroll_area)

        list_layout.addWidget(self.quit_button)

        self.setLayout(list_layout)

    def update_list(self, name_surname_filter):
        # needs improvement
        print("[Layout] Updating list (method).")
        for i in range(0, len(self.id_list)):
            if name_surname_filter in self.db.get_name_or_surname(self.id_list[i], 2):
                print("\tCreating row of list with ID: " + str(self.id_list[i]) + ".")
                temp_layout = QHBoxLayout()

                temp_layout.addWidget(QLabel(str(self.id_list[i])))
                temp_layout.addWidget(QLabel(self.db.get_name_or_surname(self.id_list[i], 2)))

                see_button = IdButton("Generar archivo PDF", self.id_list[i])
                self.generate_pdf_button_list.append(see_button)
                temp_layout.addWidget(see_button, 1)

                # edit_button = QPushButton("Editar alumno", self.id_list[i])
                # self.edit_button_list.append(edit_button)
                # temp_layout.addWidget(edit_button, 2)

                delete_button = IdButton("Eliminar alumno", self.id_list[i])
                self.delete_button_list.append(delete_button)
                temp_layout.addWidget(delete_button, 2)

                self.list_list_layout = temp_layout

                self.QtGui.QApplication.processEvents()


class IdButton(QPushButton):

    def __init__(self, string, an_id):
        self.an_id = an_id
        super(IdButton, self).__init__(string)


class AddWidget(QWidget):

    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        # main layout
        add_layout = QVBoxLayout()

        # sub-layouts
        name_surname_and_photo_layout = QHBoxLayout()
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

        # components
        name_label = QLabel("Nombre:")
        self.name_edit = QLineEdit()
        surname_label = QLabel("Apellido:")
        self.surname_edit = QLineEdit()
        photo_label = QLabel("Foto:")
        self.photo_select_button = QPushButton("Seleccionar foto")
        self.photo_see_button = QPushButton("Ver foto")
        self.photo_path = ""
        start_date_label = QLabel("Fecha de inicio:")
        self.start_date_calendar = QCalendarWidget()
        self.start_date_ind_label = QLabel()
        birthday_label = QLabel("Fecha de nacimiento:")
        self.birthday_calendar = QCalendarWidget()
        self.birthday_ind_label = QLabel()
        email_label = QLabel("e-mail:")
        self.email_edit = QLineEdit()
        phone_label = QLabel("Telefono:")
        self.phone_edit = QLineEdit()  # only int
        self.phone_edit.setValidator(QIntValidator())
        dni_label = QLabel("DNI:")
        self.dni_edit = QLineEdit()  # only int
        self.dni_edit.setValidator(QIntValidator())
        address_label = QLabel("Domicilio:")
        self.address_edit = QLineEdit()
        social_plan_label = QLabel("Obra social:")
        self.social_plan_edit = QLineEdit()
        affiliate_label = QLabel("Numero de afiliado:")
        self.affiliate_edit = QLineEdit()  # only int
        self.affiliate_edit.setValidator(QIntValidator())
        complete_name_father_label = QLabel("Nombre completo (padre):")
        self.complete_name_father_edit = QLineEdit()
        father_phone_label = QLabel("Telefono (padre):")
        self.father_phone_edit = QLineEdit()  # only int
        self.father_phone_edit.setValidator(QIntValidator())
        complete_name_mother_label = QLabel("Nombre completo (madre):")
        self.complete_name_mother_edit = QLineEdit()
        mother_phone_label = QLabel("Telefono (madre):")
        self.mother_phone_edit = QLineEdit()  # only int
        self.mother_phone_edit.setValidator(QIntValidator())
        observation_label = QLabel("Observaciones:")
        self.observation_edit = QTextEdit()
        self.accept_button = QPushButton("Aceptar")
        self.back_button = QPushButton("Volver")

        # adding to sub-layout
        name_surname_and_photo_layout.addWidget(name_label)
        name_surname_and_photo_layout.addWidget(self.name_edit)
        name_surname_and_photo_layout.addWidget(surname_label)
        name_surname_and_photo_layout.addWidget(self.surname_edit)
        name_surname_and_photo_layout.addWidget(photo_label)
        name_surname_and_photo_layout.addWidget(self.photo_select_button)
        name_surname_and_photo_layout.addWidget(self.photo_see_button)
        calendars_layout.addLayout(calendar_1_layout)
        calendars_layout.addLayout(calendar_2_layout)

        calendar_1_layout.addWidget(start_date_label)
        calendar_1_layout.addWidget(self.start_date_calendar)
        calendar_1_layout.addWidget(self.start_date_ind_label)

        calendar_2_layout.addWidget(birthday_label)
        calendar_2_layout.addWidget(self.birthday_calendar)
        calendar_2_layout.addWidget(self.birthday_ind_label)

        phone_and_address_layout.addWidget(phone_label)
        phone_and_address_layout.addWidget(self.phone_edit)
        phone_and_address_layout.addWidget(address_label)
        phone_and_address_layout.addWidget(self.address_edit)

        dni_and_email_layout.addWidget(dni_label)
        dni_and_email_layout.addWidget(self.dni_edit)
        dni_and_email_layout.addWidget(email_label)
        dni_and_email_layout.addWidget(self.email_edit)

        social_plan_layout.addWidget(social_plan_label)
        social_plan_layout.addWidget(self.social_plan_edit)
        social_plan_layout.addWidget(affiliate_label)
        social_plan_layout.addWidget(self.affiliate_edit)

        father_layout.addWidget(complete_name_father_label)
        father_layout.addWidget(self.complete_name_father_edit)
        father_layout.addWidget(father_phone_label)
        father_layout.addWidget(self.father_phone_edit)

        mother_layout.addWidget(complete_name_mother_label)
        mother_layout.addWidget(self.complete_name_mother_edit)
        mother_layout.addWidget(mother_phone_label)
        mother_layout.addWidget(self.mother_phone_edit)

        observation_layout.addWidget(observation_label)
        observation_layout.addWidget(self.observation_edit)

        buttons_layout.addWidget(self.accept_button)
        buttons_layout.addWidget(self.back_button)

        # add to main layout
        add_layout.addLayout(name_surname_and_photo_layout)
        add_layout.addLayout(calendars_layout)
        add_layout.addLayout(phone_and_address_layout)
        add_layout.addLayout(dni_and_email_layout)
        add_layout.addLayout(social_plan_layout)
        add_layout.addLayout(father_layout)
        add_layout.addLayout(mother_layout)
        add_layout.addLayout(observation_layout)
        add_layout.addLayout(buttons_layout)

        self.setLayout(add_layout)

    def header(self):
        # image("path", posX, posY, width, height)
        self.image("acqua_logo", 0, 0)
        self.set_font("Calibri")
