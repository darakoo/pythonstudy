# [문제]
# 영화인 랭킹을 1위~50위까지 출력하세요.

# 1. 외부모듈 import
# 2. html 소스 추출
# 3. BeautifulSoup 객체 생성
# 4. 데이터 분석
# 5. 파일쓰기

################################

from bs4 import BeautifulSoup
import requests

# 영화인 랭킹 1~50위
url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
response = requests.get(url)
html = response.text

# BeautifulSoup 객체생성
soup = BeautifulSoup(html, 'html.parser')
result_list = soup.find_all('td', class_='title')
# result_list = soup.find_all('td', attrs={'class': 'title'})

print(result_list)
result_str = '=====영화인랭킹50위=====\n'       # 파일쓰기에 저장할 변수
for result in result_list:
    # print(result.text.strip())
    result_str += result.text.strip() + '\n'

# 파일쓰기
file = open('C:/dev/python/pythonstudy/workspace/Section18/영화인랭킹50위.txt', 'wt')
file.write(result_str)
file.close()
