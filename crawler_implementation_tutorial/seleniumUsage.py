from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

PATH = r"..\..\pike\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()
url = 'https://www.ptt.cc/bbs/index.html'
driver.get(url)

driver.find_element(By.CLASS_NAME,'board-name').click()
driver.find_element(By.CLASS_NAME,'btn-big').click()

cookie = driver.get_cookies()

driver.close()

ss = requests.session()

# 設定 cookies
for c in cookie:
    ss.cookies.set(c['name'], c['value'])

res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text, 'html.paeser')
print(soup.prettify())