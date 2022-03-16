# [문제]
# 네이버 영화 사이트>영화랭킹>랭킹>*영화인* 메뉴를 통해서 영화인 랭킹을 1위~50위까지 출력하세요.

from bs4 import BeautifulSoup
import requests

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
result_list = soup.find_all('td', class_='title')
# result_list = soup.find_all('td', attrs={'class': 'title'})
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip())
                    
for person in movie_in:
    print(person)
