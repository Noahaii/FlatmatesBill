import webbrowser
from fpdf import FPDF


class PDF:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, flatmates, number_of_flatmates, days_sum):
        total = 0
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=25, txt='Period: ', border=0)
        pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)
        # adding text to pdf

        pdf.set_font(family='Times', size=12)
        for i in range(number_of_flatmates):
            this_flat_bill = str(round(flatmates[i].pays(bill.amount, days_sum), 2))
            pdf.cell(w=100, h=40, txt=f'{flatmates[i].name}: ', border=0)
            pdf.cell(w=150, h=40, txt=this_flat_bill, border=0, ln=1)
            total += float(this_flat_bill)
        difference = round(bill.amount - total, 2)
        pdf.cell(w=250, h=25, txt=f'difference left over that was overlooked by rounding error {str(difference)}',
                 border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
