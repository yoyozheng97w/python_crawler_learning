from urllib import request

# url =  'http://httpbin.org/get'
url ='https://www.ptt.cc/bbs/joke/index.html'

# res = request.urlopen(url)
# 使用 headers
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)      # 為字串

print(f"res.read: \n{res.read().decode('utf8')}")