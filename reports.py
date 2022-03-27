from fpdf import FPDF


class PDF:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, period, flatmates):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=25, txt='Period: ', border=1)
        pdf.cell(w=150, h=25, txt=period, border=1, ln=1)
        # adding text to pdf

        pdf.set_font(family='Times', size=24)
        for i in len(flatmates):
            pdf.cell(w=100, h=40, txt=flatmates[i].name, border=1)
            pdf.cell(w=150, h=40, txt=str(bill), border=1, ln=1)

        pdf.output(self.filename)


