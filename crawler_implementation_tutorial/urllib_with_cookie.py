# urllib 帶 cookies
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent,
           'Cookies' : 'over18=1'}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf-8'))
