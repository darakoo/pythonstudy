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
