#==============웹 크롤링 준비 : requests 라이브러리 설치, BeautifulSoup 패키지 설치
# 교재 314 : 모듈, 패키지, 라이브러리 차이점 확인하기
# pip install requests
# pip install BeautifulSoup4

# html 문서 작성 실습
# hello.html 만들고 탐색기에서 크롬브라우져로 실행하기

#==============일반 웹 페이지 정보 가져오기
#=== [requests 부분에서 오류 발생시 아래와 같이 처리:가상환경오류관련 오류임] 
# 1. vscode 실행
# 2. Ctrl + Shift + P
# 3. "Configure Language Specific" 입력, 엔터
# 4. "Python" 선택 --> settings.json 열림
# 5. "python.jediEnabled": False

#=== naver 소스 가져오기
# import requests

# url = 'https://www.naver.com'
# response = requests.get(url)
# print('응답코드:{}'.format(response.status_code))
# print(response.text)

#==============검색 결과 웹 페이지 정보 가져오기
import requests

url = 'https://search.naver.com/search.naver'
param = {'query':'파이썬'}
response = requests.get(url)
print('응답코드:{}'.format(response.status_code))
print(response.text)

#============== 기본예제 01

#============== 웹 페이지 분석 및 추출하기
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')
print(soup)

#=============== html 이해
# 1. hello.html 파일 만들고 문법 이해하기
# 2. class, id 속성의 차이 이해하기 (https://bangu4.tistory.com/26 참고)
# 3. naver 사이트 접속 => F12 개발자 도구에서 소스 확인하기

#============== 기본예제 02
#============== 응용예제


