import os

nome = "texto_02.txt"
arquivo = open(nome, "w")

t = input("Digite um texto: ")
arquivo.write(t)

print("o texto",t,"foi salvo no arquivo!")

arquivo.close()

os.system("pause")