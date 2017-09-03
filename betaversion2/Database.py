import sqlite3


class DatabaseController:

    def __init__(self):
        print("[Database] Initializing database.")
        self.connect = sqlite3.connect('aqua.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS students('
                            'id INT, '
                            'name TEXT, '
                            'surname TEXT, '
                            'birthday TEXT, '
                            'start_date TEXT, '
                            'photo_path TEXT, '
                            'dni INT, '
                            'address TEXT, '
                            'email TEXT, '
                            'phone INT, '
                            'social_plan TEXT, '
                            'affiliate_number INT, '
                            'father_name TEXT, '
                            'father_number INT, '
                            'mother_name TEXT, '
                            'mother_number INT, '
                            'notes TEXT)')

        self.id_counter = self.get_last_id_number()

    def get_last_id_number(self):
        self.cursor.execute(
            "SELECT count(*) FROM students")
        id_counter = self.cursor.fetchall()[0][0]
        print("[Database] ID counter is now: " + str(id_counter))
        return id_counter

    def insert_new_student(self, new_student_data):
        print("[Database] Adding " + str(new_student_data))
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
        self.id_counter += 1
        new_student_data[0] = self.id_counter
        self.cursor.execute(
            'INSERT INTO students '
            '(id, name, surname, birthday, start_date, photo_path, '
            'dni, address, phone, email, social_plan, affiliate_number,'
            'father_name, father_number, mother_name, mother_number, notes)'
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (new_student_data[0], new_student_data[1], new_student_data[2], new_student_data[3],
             new_student_data[4], new_student_data[5], new_student_data[6], new_student_data[7],
             new_student_data[8], new_student_data[9], new_student_data[10], new_student_data[11],
             new_student_data[12], new_student_data[13], new_student_data[14], new_student_data[15],
             new_student_data[16]))

        self.connect.commit()

    def get_name_or_surname(self, aidi, choice):
        # choice: 0==name, 1==surname, 2==complete_name
        if choice is 0:
            print("[Database] Getting name of student with ID " + str(aidi) + ".")
            self.cursor.execute(
                "SELECT name FROM students WHERE id LIKE '" + str(aidi) + "'")
            selection = self.cursor.fetchall()[0][0]
            print("\tName is: " + str(selection) + ".")
            return str(selection)

        elif choice is 1:
            print("[Database] Getting surname of student with ID " + str(aidi) + ".")
            self.cursor.execute(
                "SELECT surname FROM students WHERE id LIKE '" + str(aidi) + "'")
            selection = self.cursor.fetchall()[0][0]
            print("\tSurname is: " + str(selection) + ".")
            return str(selection)

        elif choice is 2:
            print("[Database] Getting complete name of student with ID " + str(aidi) + ".")
            self.cursor.execute(
                "SELECT name FROM students WHERE id LIKE '" + str(aidi) + "'")
            name_selection = self.cursor.fetchall()[0][0]
            self.cursor.execute(
                "SELECT surname FROM students WHERE id LIKE '" + str(aidi) + "'")
            surname_selection = self.cursor.fetchall()[0][0]
            print("\tComplete name is: " + str(name_selection) + " " + str(surname_selection) + ".")
            return str(name_selection) + " " + str(surname_selection)

    def delete_a_student(self, aidi):
        print("[Database] Deleting " + str(self.get_name_or_surname(aidi, 2)))
        self.cursor.execute(
            "DELETE FROM students WHERE id LIKE '" + str(aidi) + "'")
        self.connect.commit()

    def get_students_id_list(self):
        print("[Database] Getting students id list.")
        self.cursor.execute(
            "SELECT id FROM students")
        selection = self.cursor.fetchall()
        id_list = []
        if len(selection) is not 0:
            for i in range(0, len(selection)):
                id_list.append(selection[i][0])
        print("\tReturning all students id in a list: " + str(id_list) + ".")
        return id_list

    def get_a_student_data(self, aidi):
        self.cursor.execute(
            "SELECT * FROM students WHERE id LIKE'" + str(aidi) + "'")
        selection = self.cursor.fetchall()[0]
        print("\t[Database] Returning all data from a single student: " + str(selection) + ".")
        return selection

    def finish_session(self):
        print("[Database] Closing successfully database.")
        self.cursor.close()
        self.connect.close()




