# [문제]
# 네이버 영화 사이트>영화랭킹>랭킹>*영화인* 메뉴를 통해서 영화인 랭킹을 1위~50위까지 출력하세요.

from bs4 import BeautifulSoup
import requests

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 영화인 랭킹 1~50위
ranking50_list = soup.find_all('td', class_='title')
# ranking50_list = soup.find_all('td', attrs={'class': 'title'})
for result in ranking50_list:
    print(result.text.strip())

