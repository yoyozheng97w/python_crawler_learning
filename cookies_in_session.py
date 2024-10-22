import requests

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()
# 設定 cookies
ss.cookies['over18'] = '1'
res = ss.get(url, headers=headers)

print(res.text)