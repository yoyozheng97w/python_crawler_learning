from urllib import request
from bs4 import BeautifulSoup

url ='https://www.ptt.cc/bbs/joke/index.html'


# 使用 headers
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

# 不為字串，為 BeautifulSoup 物件
# soup = BeautifulSoup(res)       # 會有警告，因 parser 不明確

soup = BeautifulSoup(res, 'html.parser')
print(soup)