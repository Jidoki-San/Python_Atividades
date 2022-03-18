import os, requests

url = requests.get('https://meusitetc.netlify.app/') 

print("Status: ", url.status_code, "\n")
print("Header: ", url.headers, "\n")
print("HTML: ", url.content, "\n")

os.system("pause")