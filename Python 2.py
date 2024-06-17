import requests
from bs4 import BeautifulSoup

def read (word):
    url= f"http://dict.cn/big5/{word}"
    html = requests.get( url )
    soup = BeautifulSoup(html.text,'lxml')
    data = soup.find('div', class_='layout sort')
    try:
        english = data.find_all('li')
        en = [e.text for e in english]
        return( "例句：" )
        return( en )
    except:
        return("Error404")