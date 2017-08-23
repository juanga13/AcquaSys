from PyQt4.QtGui import *
from PyQt4.QtCore import QSize
from betaversion2 import Database


class ListWidget(QWidget):

    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)

        # initialize database
        db = Database.DatabaseController()

        # main layout
        list_layout = QVBoxLayout()

        # sub-layouts
        search_and_add_layout = QHBoxLayout()
        list_layout.addLayout(search_and_add_layout)

        # components
        self.search_edit = QLineEdit()
        search_and_add_layout.addWidget(self.search_edit)
        self.search_button = QPushButton()
        self.add_button = QPushButton("Agregar nuevo alumno")
        search_and_add_layout.addWidget(self.add_button)
        self.quit_button = QPushButton("Salir")

        # scroll area thing
        scroll_area = QScrollArea()
        scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout()

        self.see_button_list = []
        self.delete_button_list = []

        # first time list
        self.name_list = db.get_students_name_list()
        if len(self.name_list) is not 0:
            for i in range(0, len(self.name_list)):
                temp_layout = QHBoxLayout()
                temp_layout.addWidget(QLabel(self.name_list[i]), 0)

                see_button = QPushButton("Ver alumno")
                self.see_button_list.append(see_button)
                temp_layout.addWidget(see_button, 1)

                delete_button = QPushButton("Eliminar alumno")
                self.delete_button_list.append(delete_button)
                temp_layout.addWidget(delete_button, 2)

                self.scroll_area_layout.addLayout(temp_layout)
        print(self.see_button_list)
        print(self.delete_button_list)

        scroll_area_widget.setLayout(self.scroll_area_layout)
        scroll_area.setWidget(scroll_area_widget)
        list_layout.addWidget(scroll_area)

        list_layout.addWidget(self.quit_button)

        self.setLayout(list_layout)

    def update_list(self):
        print("[Layout] Updating list.")
        for i in range(0, len(self.name_list)):
            print(str(self.name_list) + "name list")
            print("now adding to list: " + self.name_list[i])
            temp_layout = QHBoxLayout()
            temp_layout.addWidget(QLabel(self.name_list[i]), 0)

            see_button = QPushButton("Ver alumno")
            self.see_button_list.append(see_button)
            temp_layout.addWidget(see_button, 1)

            delete_button = QPushButton("Eliminar alumno")
            self.delete_button_list.append(delete_button)
            temp_layout.addWidget(delete_button, 2)

            self.list_list_layout = temp_layout


class AddWidget(QWidget):

    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        # main layout
        add_layout = QVBoxLayout()

        # sub-layouts
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

        # components
        complete_name_label = QLabel("Nombre completo:")
        self.complete_name_edit = QLineEdit()
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
        name_and_photo_layout.addWidget(complete_name_label)
        name_and_photo_layout.addWidget(self.complete_name_edit)
        name_and_photo_layout.addWidget(photo_label)
        name_and_photo_layout.addWidget(self.photo_select_button)
        name_and_photo_layout.addWidget(self.photo_see_button)
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
        add_layout.addLayout(name_and_photo_layout)
        add_layout.addLayout(calendars_layout)
        add_layout.addLayout(phone_and_address_layout)
        add_layout.addLayout(dni_and_email_layout)
        add_layout.addLayout(social_plan_layout)
        add_layout.addLayout(father_layout)
        add_layout.addLayout(mother_layout)
        add_layout.addLayout(observation_layout)
        add_layout.addLayout(buttons_layout)

        self.setLayout(add_layout)