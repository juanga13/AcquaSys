import sqlite3

connect = sqlite3.connect('aqua.db')
cursor = connect.cursor()


def create_table():
    cursor.execute('CREATE TABLE IF NOT EXIS'
                   'TS stuffToPlot(nombre_completo REAL, telefono INTEGER)')


def insert_new_data():
    nombre_completo_ex = input("Diga nombre completo: ")
    telefono_ex = input("Ponga numero: ")
    cursor.execute('INSERT INTO stuffToPlot (nombre_completo, telefono) VALUES (?, ?)',
                   (nombre_completo_ex, telefono_ex))

    connect.commit()

def select_from_db():
    cursor.execute("SELECT * FROM stuffToPlot")
    # data = cursor.fetchall()
    data_list = []
    for row in cursor.fetchall():
        data_list.append(row)
    print(data_list)



create_table()
select_from_db()
cursor.close
connect.close()
