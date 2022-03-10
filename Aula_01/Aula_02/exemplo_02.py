import os

semaforo = "laranja"

if semaforo == "verde":
    print("Siga em frente!")
elif semaforo == "laranja":
    print("Atenção!")
else:
    print("Espere!")

os.system("pause")