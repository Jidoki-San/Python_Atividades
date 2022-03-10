import os

nome = "texto_01.txt"
arquivo = open(nome, "r")

print(arquivo.read(9))

arquivo.close()

os.system("pause")