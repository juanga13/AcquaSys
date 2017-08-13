from PyQt4.QtGui import *

from version2 import AquaDB


class GuiLayouts:

    def home_layout(self):
        layout = QGridLayout()

        add_button = QPushButton("Agregar nuevo alumno")
        search_button = QPushButton("Buscar un alumno")
        quit_button = QPushButton("Salir")

        layout.addWidget(add_button, 0, 0)
        layout.addWidget(search_button, 1, 0)
        layout.addWidget(quit_button, 2, 1)

        return layout


    def add_layout(self):
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

        complete_name_label = QLabel("Nombre completo:")
        complete_name_edit = QLineEdit()
        photo_label = QLabel("Foto:")
        photo_select_button = QPushButton("Seleccionar foto")
        photo_see_button = QPushButton("Ver foto")
        start_date_label = QLabel("Fecha de inicio:")
        start_date_calendar = QCalendarWidget()
        start_date_ind_label = QLabel()
        birthday_label = QLabel("Fecha de nacimiento:")
        birthday_calendar = QCalendarWidget()
        birthday_ind_label = QLabel()
        email_label = QLabel("e-mail:")
        email_edit = QLineEdit()
        phone_label = QLabel("Telefono:")
        phone_edit = QLineEdit()  # only int
        dni_label = QLabel("DNI:")
        dni_edit = QLineEdit()  # only int
        address_label = QLabel("Domicilio:")
        address_edit = QLineEdit()
        social_plan_label = QLabel("Obra social:")
        social_plan_edit = QLineEdit()
        affiliate_label = QLabel("Numero de afiliado:")
        affiliate_edit = QLineEdit()  # only int
        complete_name_father_label = QLabel("Nombre completo (padre):")
        complete_name_father_edit = QLineEdit()
        father_phone_label = QLabel("Telefono (padre):")
        father_phone_edit = QLineEdit()
        complete_name_mother_label = QLabel("Nombre completo (madre):")
        complete_name_mother_edit = QLineEdit()
        mother_phone_label = QLabel("Telefono (madre):")
        mother_phone_edit = QLineEdit()
        observation_label = QLabel("Observaciones:")
        observation_edit = QTextEdit()
        accept_button = QPushButton("Aceptar")
        back_button = QPushButton("Volver")

        name_and_photo_layout.addWidget(complete_name_label)
        name_and_photo_layout.addWidget(complete_name_edit)
        name_and_photo_layout.addWidget(photo_label)
        name_and_photo_layout.addWidget(photo_select_button)
        name_and_photo_layout.addWidget(photo_see_button)
        calendars_layout.addLayout(calendar_1_layout)
        calendars_layout.addLayout(calendar_2_layout)

        calendar_1_layout.addWidget(start_date_label)
        calendar_1_layout.addWidget(start_date_calendar)
        calendar_1_layout.addWidget(start_date_ind_label)

        calendar_2_layout.addWidget(birthday_label)
        calendar_2_layout.addWidget(birthday_calendar)
        calendar_2_layout.addWidget(birthday_ind_label)

        phone_and_address_layout.addWidget(phone_label)
        phone_and_address_layout.addWidget(phone_edit)
        phone_and_address_layout.addWidget(address_label)
        phone_and_address_layout.addWidget(address_edit)

        dni_and_email_layout.addWidget(dni_label)
        dni_and_email_layout.addWidget(dni_edit)
        dni_and_email_layout.addWidget(email_label)
        dni_and_email_layout.addWidget(email_edit)

        social_plan_layout.addWidget(social_plan_label)
        social_plan_layout.addWidget(social_plan_edit)
        social_plan_layout.addWidget(affiliate_label)
        social_plan_layout.addWidget(affiliate_edit)

        father_layout.addWidget(complete_name_father_label)
        father_layout.addWidget(complete_name_father_edit)
        father_layout.addWidget(father_phone_label)
        father_layout.addWidget(father_phone_edit)

        mother_layout.addWidget(complete_name_mother_label)
        mother_layout.addWidget(complete_name_mother_edit)
        mother_layout.addWidget(mother_phone_label)
        mother_layout.addWidget(mother_phone_edit)

        observation_layout.addWidget(observation_label)
        observation_layout.addWidget(observation_edit)

        buttons_layout.addWidget(accept_button)
        buttons_layout.addWidget(back_button)

        layout.addWidget(name_and_photo_layout)
        layout.addWidget(calendars_layout)
        layout.addWidget(phone_and_address_layout)
        layout.addWidget(dni_and_email_layout)
        layout.addWidget(social_plan_layout)
        layout.addWidget(father_layout)
        layout.addWidget(mother_layout)
        layout.addWidget(observation_layout)
        layout.addWidget(buttons_layout)

        return layout


def __init__(self, parent=None):
        super(SearchWidget, self).__init__(parent)
        self.setFixedSize(500, 700)

        self.layout = QVBoxLayout()

        self.search_tab_layout = QGridLayout()

        self.search_edit = QLineEdit()
        self.search_button = QPushButton()

        # widget > layout > scroll box > widget > layout
        self.scroll = QScrollArea()

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()

        self.all_data_list = AquaDB.filtered_list_giver("")
        self.complete_name_list = AquaDB.name_list()

        self.see_button_list = []
        self.delete_button_list = []

        for i in self.all_data_list:
            see_button = QPushButton("Ver")
            delete_button = QPushButton("Eliminar")
            self.see_button_list.append(see_button)
            self.delete_button_list.append(delete_button)
            self.scroll_layout.addWidget(QLabel(self.all_data_list[i]), i, 0)
            self.scroll_layout.addWidget(see_button, i, 1)
            self.scroll_layout.addWidget(delete_button, i, 2)

        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll.setWidget(self.scroll_widget)

        self.setLayout(self.layout)


def do_layout(a_student_form):
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





