import sqlite3


print("initializing database")
connect = sqlite3.connect('aqua.db')
cursor = connect.cursor()


def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS students('
                   'nombre_completo REAL, nacimiento TEXT, fecha_de_inicio TEXT, direccion_foto TEXT,'
                   'telefono INT, domicilio TEXT, dni INT, email TEXT, '
                   'nombre_completo_padre TEXT, numero_padre INT, '
                   'nombre_completo_madre TEXT, numero_madre INT, '
                   'obra_social TEXT, numero_afiliado INT, observaciones TEXT)')


def insert_new_data(a_student_form):
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

    cursor.execute('INSERT INTO students (nombre_completo, nacimiento, fecha_de_inicio,'
                   'direccion_foto, telefono, domicilio, dni, email, nombre_completo_padre, '
                   'numero_padre, nombre_completo_madre, numero_madre, obra_social, '
                   'numero_afiliado, observaciones) '
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (complete_name, birthday, start_date, photo_path, phone, address, dni, email, social_plan,
                    affiliate_number, complete_name_father, fathers_phone,
                    complete_name_mother, mothers_phone, observations))

    connect.commit()


def get_single_student_data(complete_name):
    cursor.execute("SELECT * FROM students WHERE nombre_completo LIKE '" + complete_name + "'")
    # data = cursor.fetchall()
    data_list = []
    for i in cursor.fetchall()[0]:
        data_list.append(i)
    print(data_list)
    return data_list


def delete_single_student_data(complete_name):
    cursor.execute("DELETE FROM students WHERE nombre_completo LIKE '" + complete_name + "'")


def name_list():
    complete_name_list = []
    cursor.execute("SELECT nombre_completo FROM students")
    for i in cursor.fetchall():
        complete_name_list.append(i[0])
    return complete_name_list


def filtered_list_giver(filter):
    print("filtered list:")

    data_list = []
    cursor.execute("SELECT * FROM students WHERE nombre_completo LIKE " + filter)
    for row in cursor.fetchall():
        data_list.append(row)

    return data_list
    print(data_list)


def filtered_list_giver():
    print("filtered list")
    cursor.execute("SELECT * FROM students")
    data_list = []
    for row in cursor.fetchall():
        data_list.append(row)
    return data_list


def finish_session():
    print("closing database")
    cursor.close()
    connect.close()
