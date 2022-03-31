from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Dolar.xlsx")

plt.title("Cotação do dolar - Novembro - 2021")
plt.ylabel("Valor do dólar")
plt.xlabel("Dias do mês")

dolar = planilha['VALOR']

plt.plot(dolar, marker='o', linestyle='dashed', color='red')

plt.grid()

plt.show()