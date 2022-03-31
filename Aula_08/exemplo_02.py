import os, openpyxl

planilha = openpyxl.Workbook()

page = planilha['Sheet']
page.title = 'Cadastros'

# adicionando as informações da planilha
page.append(['NOME', 'IDADE', 'TURAMA'])
page.append(['Jubileu', 45,'A'])
page.append(['Anna', 18, 'B'])
page.append(['Lucas', 17, 'B'])
page.append(['Luiz',22, 'C'])
page.append(['Paula', 35, 'C'])
page.append(['Henrique', 28, 'C'])

planilha.save("exemplo_02.xlsx")

os.system("pause")