# 상영예정작 / 이상한 수학자
# cls 명령어 이용
# 원하는 영화 크롤링하기

import requests

url = 'https://movie.naver.com/movie/running/current.naver#'
param = {'code': 190991}
response = requests.get(url, params=param)
print(response.text)
