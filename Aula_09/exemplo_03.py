import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Empresa.xlsx")

setor = planilha['SETOR']
gasto = planilha['GASTO']

plt.title("Gastos do mês - Março - 2022")

plt.pie(gasto, labels=setor, autopct='%1.2f%%')

plt.show()