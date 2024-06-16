{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "da26357e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "#word = input( '請輸入中文字:' )\n",
    "\n",
    "\n",
    "def read (word):\n",
    "        \n",
    "        url = f'https://dict.revised.moe.edu.tw/search.jsp?md=1&word={word}#order1'\n",
    "        html = requests.get( url )\n",
    "        \n",
    "        try:  \n",
    "            bs = BeautifulSoup(html.text,'lxml')\n",
    "            data = bs.find('table', id='searchL') \n",
    "            row = data.find_all('tr')[2]\n",
    "            chinese = row.find('cr').text\n",
    "            phones = row.find_all('code')\n",
    "            phone = [e.text for e in phones]\n",
    "            s = \" \".join( phone )\n",
    "            # s = row.find('sub')\n",
    "            return (chinese + '=>' + s)\n",
    "        except:\n",
    "            return ('查無此字')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
