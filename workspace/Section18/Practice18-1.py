# [문제]
# 네이버 영화 사이트>영화랭킹>랭킹>*영화인* 메뉴를 통해서 영화인 랭킹을 1위~50위까지 출력하세요.

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
result_str = '=====영화인랭킹50위=====\n'       # 파일쓰기에 저장할 변수
for result in result_list:
    # print(result.text.strip())
    result_str += result.text.strip() + '\n'

# 파일쓰기
file = open('C:/dev/python/pythonstudy/workspace/Section18/영화인랭킹50위.txt', 'wt')
file.write(result_str)
file.close()
