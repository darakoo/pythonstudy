# 평점순(현재상영영화), 평점순(모든영화)

# [문제]
# 네이버 영화 사이트>영화랭킹>랭킹>*영화* 메뉴를 통해서 1위~50위까지 아래와 같이 출력하세요.
# [실행 예]
# 1위: 이상한 나라의 수학자
# 2위: 더 배트맨
# 3위: 인민을 위해 복무하라
# ...
# 49위: 웨스트 사이드 스토리
# 50위: 배니싱: 미제사건

from bs4 import BeautifulSoup
import requests

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('div', class_='tit3')

for idx, movie in enumerate(movie_list):
    print('{}위: {}'.format(idx + 1, movie.text.strip()))
