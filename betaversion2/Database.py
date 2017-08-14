import sqlite3


class DatabaseController:

    def __init__(self):
        print("[Database] Initializing database.")
        self.connect = sqlite3.connect('aqua.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS students('
                            'name TEXT, '
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

    def insert_new_student(self, new_student_data):
        print("[Database] Adding " + str(new_student_data))
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
        self.cursor.execute(
            'INSERT INTO students '
            '(name, birthday, start_date, photo_path, '
            'dni, address, phone, email, social_plan, affiliate_number,'
            'father_name, father_number, mother_name, mother_number, notes)'
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (new_student_data[0], new_student_data[1], new_student_data[2], new_student_data[3],
             new_student_data[4], new_student_data[5], new_student_data[6], new_student_data[7],
             new_student_data[8], new_student_data[9], new_student_data[10], new_student_data[11],
             new_student_data[12], new_student_data[13], new_student_data[14]))

        self.connect.commit()

    def delete_a_student(self, complete_name):
        print("[Database] Deleting " + complete_name)
        self.cursor.execute(
            "DELETE FROM students WHERE name LIKE '" + complete_name + "'")

    def get_students_name_list(self):
        self.cursor.execute("SELECT name FROM students ")
        selection = self.cursor.fetchall()
        name_list = []
        if len(selection) is not 0:
            for i in range(0, len(selection)):
                name_list.append(selection[i][0])
        print("[Database] returning all students names in a list:\n"
              "[Database]" + str(name_list))
        return name_list

    def get_a_student(self, complete_name):
        self.cursor.execute(
            "SELECT * FROM students WHERE name LIKE'" + complete_name + "'")
        selection = self.cursor.fetchall()[0]
        print("[Database] returning all data from a single student:\n"
              "[Database]" + str(selection))
        return selection

    def finish_session(self):
        print("[Database] Closing database.")
        self.cursor.close()
        self.connect.close()




