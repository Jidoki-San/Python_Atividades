import os, openpyxl
from openpyxl.styles import Alignment

planilha = openpyxl.Workbook()
page = planilha.active

# adicionando os valores em posições especificas na planilha
page['A1'].value = 'X'
page['B2'].value = 'X'
page['C3'].value = 'X'
page['D4'].value = 'X'

# alinhado o texto no centro da célula
page['A1'].alignment = Alignment(horizontal='center')
page['B2'].alignment = Alignment(horizontal='center')
page['C3'].alignment = Alignment(horizontal='center')
page['D4'].alignment = Alignment(horizontal='center')

planilha.save("exemplo_03.xlsx")

os.system("pause")