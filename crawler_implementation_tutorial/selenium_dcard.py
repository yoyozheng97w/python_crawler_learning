from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

PATH = r"..\..\pike\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()

url = 'https://www.dcard.tw/f'
driver.get(url)
time.sleep(3)

# 在表單輸入特定關鍵字
driver.find_element(By.TAG_NAME, 'input').send_keys('攝影')
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]').click()

# 將網頁畫面往下滾動至離頂部 5000 高度的位子
driver.execute_script('var s = document.documentElement.scrollTop=5000')
time.sleep(3)

# 將網頁畫面往上滾動至頂部 
driver.execute_script('var s = document.documentElement.scrollTop=0')
time.sleep(3)

driver.execute_script('var s = document.documentElement.scrollTop=10000')
time.sleep(3)

# 取得目前的 html 字串
html = driver.execute_script("return document.getElementByTagName('html')[0].outerHTML")