import os

#  index      0         1       2       3
lista =  ["Jubileu", "Maria", "Ana", "Lucas"]

print(lista)

nome = input("Digite um nome para deletar: ")
# removendo valor da lista
lista.remove(nome)

print(lista)

os.system("pause")