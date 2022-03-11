##### 모듈 생성
# converter.py 파일을 생성한다. 소스는 전달

##### 모듈사용
# case1 : converter 모듈 import
import converter

pounds = converter.gram_to_pounds(1000)
print('pounds:', pounds)
miles = converter.kilometer_to_miles(150)
print('miles:', miles)

# case2 : converter 모듈 import *
# 모듈의 함수 사용시 모듈명을 기재하지 않아도 된다.
from converter import *
pounds = gram_to_pounds(1000)
print('pounds:', pounds)
miles = kilometer_to_miles(150)
print('miles:', miles)

##### 별명 사용하기 : as 
# case1
import converter as cvt

pounds = cvt.gram_to_pounds(1000)
print('pounds:', pounds)
miles = cvt.kilometer_to_miles(150)
print('miles:', miles)

# case2
from converter import kilometer_to_miles as k_to_m
miles = k_to_m(150)
print('miles:', miles)

##### 기본예제01
# Ex01.py 파일제공, my_secure.py 파일생성

##### 표준 모듈의 활용
##### math 모듈
import math
print('math.pi:', math.pi)
print('math.ceil:', math.pi)
print('math.floor:', math.pi)

##### random 모듈: 임의의 수
import random
print('random.randint(1, 10):', random.randint(1, 10))
print('random.randrange(1, 10, 2):', random.randrange(1, 10, 2)) # 1~10 사이 홀수

# random.random()
print(random.random())
# 50% 확률
if random.random() < 0.5:
    print('안녕하세요')
else:
    print('다음에 만나요')

# random.choice()
s = [1, 2, 3]
print(random.choice(s))
print('random.sample(s, 1):', random.sample(s, 1))

# random.sample(시퀀스자료형, 갯수) 
# 로또 번호 생성
print('로또:', random.sample(range(1, 47), 6))

# random.shuffle(수정가능한시쿼스자료형)
# 주의 : 반환값이 없으며 자료형의 값을 변경 시킨다.
s = [5, 2, 4, 3, 1]
random.shuffle(s)
print('random.shuffle(s):', s)

##### 기본예제 02

##### time 모듈
# time.time() : 1970년1월1일 자정에서 지금까지 경과된 시간을 반환

# time.ctime() : 형식있는 시간으로 반환
import time
print('time.ctime():', time.ctime(time.time()))

# time.strftime(지시자) : 형식을 갖춘 날짜 데이터
# 지시자는 교재 참고
print('time.strftime():', time.strftime('%Y %m %d %a %H:%M:%S'))

# time.sleep() : 전달된 초만큼 시스템을 일시 중지

##### datetime 모듈
# 교재 설명은 skip 하고 기본예제로 확인만 한다.
# datetime이 두번 나오는 이유는 모듈안에 클래스가 있을 경우 이다.
import datetime
print(datetime.datetime.now())

##### 기본예제 03

##### 외부 모듈의 활용
# pip 명령어는 명령프롬프트 창에서 실행해야 한다.
# pip --help
# pip list
# pip show numpy
# pip install numpy

import numpy as np
s = [1, 2, 3, 4, 5]
print(np.sum(s))

# pip uninstall numpy

