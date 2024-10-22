import requests
from bs4 import BeautifulSoup

url_target = ''

# 複製 From Data
post_data_str = """"""

post_data = {}
for row in post_data_str.split('\n'):
    post_data[row.split(': ')[0]] = row.split(': ')[1]

# 製作 headers
# 複製 Request Headers
headers_str = """"""

headers = {}
for row in headers_str.split('\n'):
    headers[row.split(': ')[0]] = row.split(': ')[1]

res = requests.post(url_target, headers=headers, data=post_data)
soup = BeautifulSoup(res.text, 'html.parser')

# 查詢 <div id="print_area"></div> 裡面的 <td align="left"> </td>
title = soup.select('div[id="print_area"] td[align="left"]')