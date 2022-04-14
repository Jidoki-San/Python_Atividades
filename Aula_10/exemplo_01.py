import os
from fpdf import FPDF

# Na criação de pdf podemos utilizar os seguintes códigos:
# 1°- Orientação usamos: 'L' para imagem deitada e 'P' para imagem em pé;
# 2°- Na segunda coluna é a medida: 'mm' para milimitros, 'cm' para centimetros e 'in' para polegadas;
# 3°- E a quarta coluna é o tipo de papel, que são: 'A3','A4','A5' e 'Latter'.
pdf = FPDF('P', 'mm', 'A4')

# Cria uma nova página pdf.
pdf.add_page()

# Aqui iremos colocar algumas informações para começar a escrever no excel:
#            fonte|estilo|tamanho
pdf.set_font('Times', 'i', 16)

#    largura|altura|escrita        orientação da escrita: 'L','C' e 'R'
pdf.cell(w=0,h=0, txt='Olá mundo!',align='C')

# Sai o pdf(termina de ser criado e salva)
pdf.output("Teste_01.pdf")

print("O pdf foi criado com sucesso!")
os.system("pause")