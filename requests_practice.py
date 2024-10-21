import requests

url =  'http://httpbin.org/get'
res = requests.get(url)     # 為字串

print(res.text)