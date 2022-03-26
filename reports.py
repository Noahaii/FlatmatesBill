from fpdf import FPDF


class PDF:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, all_flatmates):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # adding text to pdf
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=2)
        pdf.cell(w=100, h=40, txt='Period: ', border=1)
        pdf.cell(w=150, h=40, txt='March 2022', border=1, ln=1)
