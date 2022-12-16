# [문제]
# 응용2번에서 나온 결과중 순위가 상승한 영화 제목만 크롤링 하세요.

from bs4 import BeautifulSoup
import requests


url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('tr')
up_list = []
up_list_gap = []

for movie in movie_list:
    target_list = movie.find_all('td', class_='ac')
    if target_list:
        if target_list[1].find('img', class_='arrow').get('alt') == 'up':
            up_list.append(movie.find('td', class_='title').text.strip())
            up_list_gap.append(movie.find('td', class_='range ac').text.strip())
            
for up_list_gap, up_list in zip(up_list_gap, up_list):
    print(up_list_gap + '\t' + up_list)
