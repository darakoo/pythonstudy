# request 를 이용하여 html 소스 얻기
'''
#=== naver
import requests

url = 'https://www.naver.com'
response = requests.get(url)
print(f'응답코드:{response.status_code}')
print(response.text)
'''
#==============naver 검색
import requests

url = 'https://search.naver.com/search.naver'
param = {'query':'파이썬'}
response = requests.get(url=url, params=param)
print('응답코드!!:{}'.format(response.status_code))
print(response.text)
'''
#==============기본예제 1 skip
# 상영예정작 / 이상한 수학자
# cls 명령어 이용
# 원하는 영화 크롤링하기

import requests

url = 'https://movie.naver.com/movie/running/current.naver'
param = {'code': 190991}
response = requests.get(url, params=param)
print(response.text)
'''