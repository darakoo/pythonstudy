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
