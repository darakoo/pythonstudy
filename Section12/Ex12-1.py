##### 사용자 모듈 생성 및 활용

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


'''
[문제]
문자열 슬라이싱 기능을 이용하여 아래와 같이 실행되게 하세요.
[실행예]
김**
951012-1######
010-###*-5678
'''

# 모듈로 분리 하는 이유 : 공통된 기능을 공유하기위해, 작업의 분배를 위해

from my_secure import *

print(secure_name('김철수'))
print(secure_no('951012-1234567'))
print(secure_phone('010-1234-5678'))

