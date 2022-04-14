import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("Valor do Dolar.xlsx")
dias = planilha['DIAS']
dolar = planilha['DOLAR']

plt.bar(dias, dolar, color='green', width=0.5)

plt.savefig("Valor do Dolar.png")

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', 'i', 16)
pdf.cell(w=0, h=0, txt="Gráfico do valor do dolar", align="C")
pdf.line(10,15,200,15)

pdf.image(name="Valor do Dolar.png", x=0, y=20, w=200)
pdf.output("Valor do Dolar.pdf")

print("O PDF foi criado com sucesso!")
os.system("pause")