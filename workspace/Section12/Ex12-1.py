# 모듈로 분리 하는 이유 : 공통된 기능을 공유하기위해, 작업의 분배를 위해

from my_secure import *

print(secure_name('김철수'))
print(secure_no('951012-1234567'))
print(secure_phone('010-1234-5678'))

