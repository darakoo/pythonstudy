# 한줄평 출력하기
# 주석 없는 소스만 주고 주석 달기

# 외부 모듈 가져오기
import requests
from bs4 import BeautifulSoup

# 웹페이지 정보 가져오기
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 207921}
response = requests.get(url, params=param)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# BeautifulSoup 객체를 이용하여 데이터 분석 및 추출
review_list = soup.find_all('div', class_='score_reple')
for review in review_list:
    print(review.find('p').text.strip())


##########################
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 207921}
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

review_list = soup.find_all('div', class_='score_reple')
for review in review_list:
    print(review.find('p').text.strip())