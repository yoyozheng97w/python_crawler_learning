import requests
from bs4 import BeautifulSoup

url ='https://www.ptt.cc/bbs/movie/index.html'

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# prettify：排版
# print(soup.prettify())

article_title_html = soup.select('div[class="title"]')
# print(article_title_html)

for each_title in article_title_html:
    print(each_title.a.text)
    print("https://www.ptt.cc" + each_title.a['href'])