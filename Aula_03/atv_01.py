import os 

repete = "s"

while repete == "s" or repete == "S":

    n = int(input("Digite um número: "))

    for x in range(1,11):
        print(n,"x",x,"=",n*x)

    repete = input("Deseja fazer uma nova tabuada? (s/n):")
    # código abaixo limpa a tela do terminal
    # ante de começar um novo ciclo
    os.system("cls")

os.system("pause")