import os

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Criança!")
elif idade >= 13 and idade <= 29:
    print("Jovem!")
elif idade >= 30 and idade <= 59:
    print("Adulto!")
else:
    print("Idoso!")

os.system("pause")