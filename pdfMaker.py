from fpdf import *


class PDF:

    def __init__(self, student_data):
        self.pdf = FPDF()
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

        # cell(width, height, text, border?, wat do next, align, fill, link)
        self.pdf.add_page()

        self.pdf.set_y(10)
        self.pdf.set_font("Arial", "B", 20)
        self.pdf.cell(0, 10, "Planilla de", 0, 1, "C")

        self.pdf.set_font("Arial", "B", 15)
        self.pdf.cell(0, 10, str(student_data[1]) + " " + str(student_data[2]), 0, 1, "C")

        line_space = 3
        self.pdf.set_font("Arial", "", 12)
        self.pdf.cell(100, 6, "Fecha de inicio: " + str(student_data[4]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Domicilio: " + str(student_data[7]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Telefono: " + str(student_data[8]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Fecha de nacimiento: " + str(student_data[3]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "DNI" + str(student_data[6]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "email: " + str(student_data[9]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Obra social: " + str(student_data[10]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Numero de Afiliado: " + str(student_data[11]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Nombre padre: " + str(student_data[12]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Tel.: " + str(student_data[13]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Nombre madre: " + str(student_data[14]), 1, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.cell(100, 6, "Tel.: " + str(student_data[15]), 1, 1, "L")
        self.pdf.ln(line_space)
        for i in range(12):
            self.pdf.set_x(20)
            self.pdf.cell(100, 6, "Fecha:___________________. Pago:___________________." + str(i), 0, 1, "L")
        self.pdf.ln(line_space)
        self.pdf.set_x(10)
        self.pdf.cell(100, 6, "Observaciones: " + str(student_data[16]), 0, 1, "L")

        observation_string = str(student_data[14])
        for i in range(len(student_data[14]), 330):
            observation_string += "_"
        self.pdf.write(10, observation_string)

        # image(path, posx, posy, width, height, filetype, link)
        if student_data[5] is not "":
            self.pdf.image(student_data[5], 120, 30, 80, 80, student_data[5][-3:])

        self.pdf.output("./output/pdf_output/" + str(student_data[0]) + ".pdf", "f")
