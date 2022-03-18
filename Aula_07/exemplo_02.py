import os, requests

url = requests.get('https://meusitetc.netlify.app/')
nome = "teste.txt"

arquivo = open(nome, "w")

arquivo.write("Status: "+str(url.status_code)+"\n")
arquivo.write("Header: "+str(url.headers)+"\n")
arquivo.write("HTML: "+str(url.content)+"\n")

arquivo.close()

os.system("pause")