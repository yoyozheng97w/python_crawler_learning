# 則找出網址規律，用 request 方法進入
import requests
from bs4 import BeautifulSoup

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}

page_number = 9999
while(page_number >= 9990):

    url =f'https://www.ptt.cc/bbs/movie/index{page_number}.html'

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_title in article_title_html:
        # 若文章被刪除，each_title.a.text 就不會有 a 的標籤，因此要用 try except 處理例外
        try:
            print(each_title.a.text)
            print("https://www.ptt.cc" + each_title.a['href'])
        except AttributeError as e:
            print(each_title)
            print(e.args)
    page_number -= 1