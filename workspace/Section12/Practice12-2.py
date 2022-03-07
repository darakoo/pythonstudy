# [문제]
# 1~100 사이의 정수를 알아 맞춥니다.
# [실행예]
# UpDown게임을 시작합니다.
# 어떤 값일까요? >>> 30
# Up
# 어떤 값일까요? >>> 50
# Down
# 어떤 값일까요? >>> 40
# Up
# 어떤 값일까요? >>> 48
# 정답입니다.
# 20초 만에 성공했습니다.
# [힌트]
# 1~100 사이의 임의의 정수 생성 : random.randint()
# 현재시간 : time.time()

import random
import time
import math

answer = random.randint(1, 100)

print('UpDown게임을 시작합니다.')
start = time.time()
while True:
    n = int(input('어떤 값일까요? >>> '))
    if answer == n:
        print('정답입니다.')
        break
    elif answer < n:
        print('Down')
    else:
        print('Up')
end = time.time()

elapse = end - start
print('{}초 만에 성공했습니다.'.format(math.floor(elapse)))
