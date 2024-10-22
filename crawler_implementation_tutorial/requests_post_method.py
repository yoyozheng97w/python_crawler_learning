# request
import requests
from bs4 import BeautifulSoup

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}

url = 'http://httpbin.org/post'

data = {'key1': 'value1', 'key2': 'value2'}
res = requests.post(url, data=data, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())