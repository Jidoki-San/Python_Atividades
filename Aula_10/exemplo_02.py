import os
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

pdf.set_font('Times', 'i', 16)

texto = "Morte: \n\nCaso o paciente não melhorasse, geralmente eles não precisavam voltar ao médico, porque no quarto dia   eles morriam, até porque com esse tipo de tratamento médico, melhorar seria um verdadeiro milagre."

pdf.multi_cell(w=0, h=7, txt=texto)

pdf.output("Texte_02.pdf")

# Adiciona uma imagem no pdf:
pdf.image(name="teste_02.png", x=0, y=0, w=0)

print("O pdf foi criado com sucesso!")
os.system("pause")