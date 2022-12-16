# skip

##### time 모듈
import time
print(time.ctime())    # 형식있는 시간으로 반환
print('time.strftime():', time.strftime('%Y %m %d %a %H:%M:%S'))    # 형식을 갖춘 날짜 데이터(지시자는 교재 참고)
# time.sleep() : 전달된 초만큼 시스템을 일시 중지

##### datetime 모듈
# 교재 설명은 skip 하고 기본예제로 확인만 한다.
# datetime이 두번 나오는 이유는 모듈안에 클래스가 있을 경우 이다.
import datetime
print(datetime.datetime.now())

##### 기본예제 03


# [문제설명]
# 1~천만까지의 합계를 구하고 소요시간을 출력하는 프로그램입니다.
# [실행예]
# 총 합은 50000005000000입니다.
# 총 0.891691초가 소요되었습니다.

# import datetime
from datetime import *

start = datetime.now()
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.now()

elapse = end - start
elapse = elapse.total_seconds()    # total_seconds() 함수를 통해 소요된 시간을 초단위로 변경한다.

print('총 합은 {}입니다.'.format(total, ','))
print('총 {}초가 소요되었습니다.'.format(elapse))
