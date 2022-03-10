import os

nome = input("Digite o nome do arquivo: ")
nome += ".txt"

arquivo = open(nome, "a")

n = input("Digite um nome:")
n = "\n"
arquivo.write(n)

print("Arquivo criado com sucesso!")
arquivo.close()

os.system("pause")