import os, openpyxl
from openpyxl.styles import Alignment,Border, Side

planilha = openpyxl.Workbook()
page = planilha ['Sheet']
page.title = 'Produtos'

page.append(['NOME', 'QUANTIDADE', 'PREÇO' ])
page.append(['Leite', 3, 'R$ 5.30' ])
page.append(['Queijo', 2, 'R$ 4.50' ])
page.append(['Pão', 10, 'R$ 1.80' ])

# altera o tamanho das células
page.column.dimensions['A'].width = 20
page.column.dimensions['B'].width = 20
page.column.dimensions['C'].width = 20

# definindo o estilo da borda
estilo = Side(border_style='thin', color='000000') 

# 