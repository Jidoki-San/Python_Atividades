import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://meusitetc.netlify.app/')
html = url.content

site = BeautifulSoup(html, 'html.parser')

print(site.prettify())

os.system("pause")