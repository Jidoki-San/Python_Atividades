import os, openpyxl

# criando uma nova planilha
planilha = openpyxl.Workbook()

# renomeando o titulo da página
pag_01 = planilha['Sheet']
pag_01.title = 'página_01'

# criando uma nova página
pag_02 = planilha.create_sheet("página_02")

pag_02.append(['Olá'])

# salvando o arquivo no computador
planilha.save("exemplo_01.xlsx")
print("Planilha criada com sucesso")

os.system("pause")