# urllib，python 內建函示庫，比較底層、較麻煩
from urllib import request, parse
from bs4 import BeautifulSoup

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}

url = 'http://httpbin.org/post'

data = {'key1': 'value1', 'key2': 'value2'}
# 把 data 轉成字串形式
data = bytes(parse.urlencode(data), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers)
res = request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')

print(soup.prettify())