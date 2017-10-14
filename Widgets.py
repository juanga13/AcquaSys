from PyQt4.QtGui import *
from PyQt4.QtCore import QSize

import Database


class ListWidget(QWidget):

    def __init__(self, logger, search_filter=None, *args, **kwargs):
        self.logger = logger
        self.search_filter = search_filter
        if search_filter is None:
            self.search_filter = ''
        super(ListWidget, self).__init__(*args, **kwargs)

        # initialize database controller
        self.db = Database.DatabaseController(self.logger)
        self.list_list_size = 600

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
        self.scroll_area = QScrollArea()
        scroll_area_widget = QWidget()

        # scroll area background
        background_image = QImage("./resources/fill.jpg")
        background_image = background_image.scaled(QSize(self.size()))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(background_image))
        self.setPalette(palette)

        self.scroll_area_layout = QVBoxLayout()

        # button list
        self.edit_button_list = []
        self.generate_pdf_button_list = []
        self.delete_button_list = []

        self.id_list = self.db.get_students_id_list(self.search_filter)

        # log updating list
        self.logger.log_into_file("[Widgets] Creating list for first time.")
        self.logger.log_into_file("\tList widget: id_list is: " + str(self.id_list) + ".")

        if len(self.id_list) is not 0:
            for i in range(0, len(self.id_list)):
                temp_layout = QHBoxLayout()

                temp_layout.addWidget(QLabel(str(self.id_list[i])))
                temp_layout.addWidget(QLabel(self.db.get_name_or_surname(self.id_list[i], 2)))

                edit_button = IdButton("Editar alumno", self.id_list[i])
                self.edit_button_list.append(edit_button)
                temp_layout.addWidget(edit_button)

                see_button = IdButton("Generar archivo PDF", self.id_list[i])
                self.generate_pdf_button_list.append(see_button)
                temp_layout.addWidget(see_button)

                delete_button = IdButton("Eliminar alumno", self.id_list[i])
                self.delete_button_list.append(delete_button)
                temp_layout.addWidget(delete_button)

                self.scroll_area_layout.addLayout(temp_layout)

        scroll_area_widget.setLayout(self.scroll_area_layout)
        self.list_list_size = scroll_area_widget.sizeHint().width()
        self.scroll_area.setWidget(scroll_area_widget)
        list_layout.addWidget(self.scroll_area)

        list_layout.addWidget(self.quit_button)

        self.setLayout(list_layout)


class IdButton(QPushButton):

    def __init__(self, string, an_id):
        self.an_id = an_id
        super(IdButton, self).__init__(string)


class AddEditWidget(QWidget):

    def __init__(self, logger, *args, **kwargs):
        self.logger = logger
        super(AddEditWidget, self).__init__(*args, **kwargs)

        # initialize
        self.db = Database.DatabaseController(self.logger)

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
        dni_label = QLabel("DNI:")
        self.dni_edit = QLineEdit()  # only int
        address_label = QLabel("Domicilio:")
        self.address_edit = QLineEdit()
        social_plan_label = QLabel("Obra social:")
        self.social_plan_edit = QLineEdit()
        affiliate_label = QLabel("Numero de afiliado:")
        self.affiliate_edit = QLineEdit()  # only int
        complete_name_father_label = QLabel("Nombre completo (padre):")
        self.complete_name_father_edit = QLineEdit()
        father_phone_label = QLabel("Telefono (padre):")
        self.father_phone_edit = QLineEdit()  # only int
        complete_name_mother_label = QLabel("Nombre completo (madre):")
        self.complete_name_mother_edit = QLineEdit()
        mother_phone_label = QLabel("Telefono (madre):")
        self.mother_phone_edit = QLineEdit()  # only int
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

    def change_values(self, aidi):
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
        self.name_edit.setText(student_data[1])
        self.surname_edit.setText(student_data[2])
        self.photo_path = student_data[5]
        self.start_date_ind_label.setText(student_data[4])
        self.birthday_ind_label.setText(student_data[3])
        self.phone_edit.setText(student_data[8])
        self.address_edit.setText(student_data[7])
        self.dni_edit.setText(student_data[6])
        self.email_edit.setText(student_data[9])
        self.social_plan_edit.setText(student_data[10])
        self.affiliate_edit.setText(student_data[11])
        self.complete_name_father_edit.setText(student_data[12])
        self.father_phone_edit.setText(student_data[13])
        self.complete_name_mother_edit.setText(student_data[14])
        self.mother_phone_edit.setText(student_data[15])
        self.observation_edit.setText(student_data[16])
