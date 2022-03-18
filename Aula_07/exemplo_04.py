import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://meusitetc.netlify.app/')
html = url.content

site = BeautifulSoup(html, 'html.parser')
t1 = site.find('div', attrs={'class': 'box_2'})

if t1:
    t2 = t1.find('h2')

    resp = t2.text
    resp = resp.replace("Jogos ", "")
    resp = resp.replace(" para ficar de olho!", "")

    print(resp)
else:
    print("O elemento não foi encontrado no HTML!")

os.system("pause")