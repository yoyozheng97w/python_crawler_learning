import requests
from bs4 import BeautifulSoup

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}

url = 'https://web.pcc.gov.tw/prkms/tender/common/agent/indexTenderAgent##'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

for i in soup.select('input[type="hidden"]'):
    # 有些隱藏標籤沒有值，因此會出現錯誤訊息
    try:
        print(f"{i['name']}: {i['value']}")
    except:
        pass