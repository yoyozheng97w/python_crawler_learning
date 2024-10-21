# 則找出網址規律，用 request 方法進入
import requests
from bs4 import BeautifulSoup
import os

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}

resource_path = r'./res'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)


page_number = 9999
while(page_number >= 9999):

    url =f'https://www.ptt.cc/bbs/movie/index{page_number}.html'

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_title in article_title_html:
        try:
            print(each_title.a.text)
            print("https://www.ptt.cc" + each_title.a['href'])

            article_url = 'https://www.ptt.cc' + each_title.a['href']
            article_text = each_title.a.text

            # 對文章提出請求
            article_res = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            article_content = article_soup.select('div#main-content')[0].text.split('--')[0]

            with open(f"{resource_path}/{article_text}.txt", 'w', encoding='utf-8') as w:
            # with open(r'%s/%s.txt' % (resource_path, article_text), 'w', encoding='utf-8') as w:
                w.write(article_content)
            print()
        except AttributeError as e:
            print(each_title)
            print(e.args)
        except FileNotFoundError as e:
            pass
        except OSError as e:
            pass
    page_number -= 1