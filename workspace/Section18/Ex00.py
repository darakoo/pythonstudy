#==============웹 크롤링 준비 : requests 라이브러리 설치, BeautifulSoup 패키지 설치
# 교재 314 : 모듈, 패키지, 라이브러리 차이점 확인하기
# pip install requests
# pip install BeautifulSoup4
    
#=============== html 이해
# 1. html01.html, html02.html 파일 만들고 문법 이해하기
# 2. class, id 속성의 차이 이해하기 (https://bangu4.tistory.com/26 참고)
# 3. naver 사이트 접속 => F12 개발자 도구에서 소스 확인하기

#==============일반 웹 페이지 정보 가져오기
#=== [requests 부분에서 오류 발생시 아래와 같이 처리:가상환경오류관련 오류임] 
# 1. vscode 실행
# 2. Ctrl + Shift + P
# 3. "Configure Language Specific" 입력, 엔터
# 4. "Python" 선택 --> settings.json 열림
# 5. "python.jediEnabled": False


#=== naver 소스 가져오기
import requests

url = 'https://www.naver.com'
response = requests.get(url)
print(f'응답코드:{response.status_code}')
print(response.text)


#==============검색 결과 웹 페이지 정보 가져오기
import requests

url = 'https://search.naver.com/search.naver'
param = {'query':'파이썬'}
response = requests.get(url)
print('응답코드:{}'.format(response.status_code))
print(response.text)

#============== 기본예제 01


#============== 웹 페이지 분석 및 추출하기
# 모듈 import
import requests
from bs4 import BeautifulSoup

# html 소스 추출
url = 'https://www.naver.com'
response = requests.get(url)
html = response.text

# BeautifulSoup 객체생성
soup = BeautifulSoup(html, 'html.parser')

# 교재 322, 323 태그 설명 후 실습
# find() : 지정된 태그들 중 가장 첫 번째 태그만 가져온다.
print('====find()=======')
print(soup.find('a').text)
print(soup.find('a').get('href'))

# find_all() : 지정한 태그들을 모두 가져온다. 
print('====find_all()=======')
print(soup.find_all('a')[0].text)
print(soup.find_all('a')[0].get('href'))
print(soup.find_all('a')[1].text)
print(soup.find_all('a')[2].get('href'))

print('====find_all()-반복문=======')
for i in range(0, len(soup.find_all('a'))):
    if(len(soup.find_all('a')[i].text) == 0):
        break

    print(soup.find_all('a')[i].text)
    print(soup.find_all('a')[i].get('href'))

#============== 기본예제 02


#============== 응용예제

