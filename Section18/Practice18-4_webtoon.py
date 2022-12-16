# [문제]
# 웹툰 조회

from bs4 import BeautifulSoup
import requests

# 웹툰1
url = 'https://comic.naver.com/webtoon/weekday'
# 웹툰2
# url = 'https://comic.naver.com/webtoon/list?titleId=747269&weekday=wed' 

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 웹툰1
result_list = soup.find_all('a', class_='title')
for result in result_list:
    print(result.text.strip())


# 웹툰2
# result_list = soup.find_all('td', class_='title')
# for result in result_list:
#     print(result.text.strip())
