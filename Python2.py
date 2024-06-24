import requests
from bs4 import BeautifulSoup

def read(word):
    url = f"http://dict.cn/big5/{word}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    data = soup.find('div', class_='layout sort')
    try:
        english = data.find_all('li')
        en = [e.text for e in english]
        sen = '\n\n'.join(en)  # 使用 "\n" 換行符號來連接翻譯結果
        return sen
    except AttributeError:
        return "Error404"
