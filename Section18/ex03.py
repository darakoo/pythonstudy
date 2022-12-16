#============== 웹 페이지 분석 및 추출하기
# 외부모듈 import
import requests
from bs4 import BeautifulSoup

# html 소스 추출
url = 'https://www.naver.com'
res = requests.get(url)
html = res.text

# BeautifulSoup 객체생성
soup = BeautifulSoup(html, 'html.parser')

# 교재 322, 323 태그 설명 후 실습
# find() : 지정된 태그들 중 가장 첫 번째 태그만 가져온다.
# print('====find()=======')
# print(soup.find('a').text)
# print(soup.find('a').get('href'))

# find_all() : 지정한 태그들을 모두 가져온다. 
# print('====find_all()=======')
# print(soup.find_all('a')[0].text)
# print(soup.find_all('a')[0].get('href'))
# print(soup.find_all('a')[1].text)
# print(soup.find_all('a')[2].get('href'))

print('====find_all()-반복문=======')
href_list = soup.find_all('a')
# print(len(href_list))
for i in range(0, len(href_list)):
    if(len(href_list[i].text) == 0):
        break

    print(href_list[i].text)
    print(href_list[i].get('href'))
