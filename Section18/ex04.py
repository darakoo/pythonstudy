# [문제]한줄평 출력하기
# [과제]주석 없는 소스만 주고 주석 달기

# 1. 외부모듈 import
import requests
from bs4 import BeautifulSoup

# 2. html 소스 추출
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 207921}
response = requests.get(url, params=param)
html = response.text

# 3. BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 4. 데이터 분석
review_list = soup.find_all('div', class_='score_reple')
for review in review_list:
    print(review.find('p').text.strip())
