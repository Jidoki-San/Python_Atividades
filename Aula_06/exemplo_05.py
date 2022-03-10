import os

nome = "texto_01.txt"
cont = 0

if os.path.exists(nome):
    arquivo = open(nome, "r")
    t= arquivo.read()

    for x in range(len(t)):
        if t[x] != "\n" and t[x] != 

    arquivo.close()
    print("Toltal de caracteres:", cont)
else:
    print("Arquivo não foi encontrado!")


os.system("pause")