# [문제]
# 임의로 생성된 1~100 사이의 정수 하나를 알아 맞춥니다.
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
# [힌트]
# 1~100 사이의 임의의 정수 생성 : random.randint()

import random

answer = random.randint(1, 100)
print('UpDown게임을 시작합니다.')
while True:
    n = int(input('어떤 값일까요? >>> '))
    if answer == n:
        print('정답입니다.')
        break
    elif n > answer:
        print('Down')
    else:
        print('Up')