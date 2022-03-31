import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Empresa.xlsx")

setor = planilha['SETOR']
gasto = planilha['GASTO']

plt.title("Gastos do mês - Março - 2022")

# cria um gráfico de barras verticais
# plt.bar(setor, gasto, color='green', width=0.5)

plt.barh(setor, gasto, color='blue', height=0.5)

plt.show()