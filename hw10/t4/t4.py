from bs4 import BeautifulSoup
import requests

url = "https://www.pcmag.com/"
respons = requests.get(url)

html_content = respons.text

bs = BeautifulSoup(html_content, features='lxml')
ps = bs.find_all('p')
with open("paragraph.txt",'w') as f:
    for i in ps:
        f.write(str(i)+'\n')
print(*ps,sep = '\n')



