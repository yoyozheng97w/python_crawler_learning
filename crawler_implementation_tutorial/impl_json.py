import requests
import json

# 露天
url = 'https://rtapi.ruten.com.tw/api/search/v3/index.php/core/prod?type=direct&cateid=002100010047&sort=rnk%2Fdc&offset=1&limit=100'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
res = requests.get(url, headers=headers)

json_str = res.text
json_data = json.loads(json_str)

# json_data 是一個字典
for d in json_data:
    print(d, json_data[d])

# Rows 字典是 json_data 字典裡的一個元素，
# print 出 Rows 裡的 key
for k in json_data['Rows'][0]:
    print(k)

