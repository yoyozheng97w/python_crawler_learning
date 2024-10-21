# 找出上一頁的 button，用 request 方法進入
import requests
from bs4 import BeautifulSoup

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
url =f'https://www.ptt.cc/bbs/movie/index.html'
for i in range(0, 3):    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')
    # print(article_title_html)

    for each_title in article_title_html:
        # 若文章被刪除，each_title.a.text 就不會有 a 的標籤，因此要用 try except 處理例外
        try:
            print(each_title.a.text)
            print("https://www.ptt.cc" + each_title.a['href'])
        except AttributeError as e:
            print("-----------------------------------")
            print(each_title)
            print(e.args)

last_page_url = soup.select('a[class="btn wide"]')[1]['href']
last_page_url = "https://www.ptt.cc/bbs" + last_page_url

url = last_page_url