# requests 帶 cookies
import requests
import ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}

cookies = {'over18': '1'}
res = requests.get(url, headers = headers, cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())