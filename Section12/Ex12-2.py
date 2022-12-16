##### 표준 모듈의 활용
##### math 모듈
import math
print('math.pi:', math.pi)
print('math.ceil:', math.ceil(1.1))         # 올림
print('math.floor:', math.floor(1.9))       # 내림

##### random 모듈: 임의의 수
import random
print(random.randint(1, 10))        # 1~10 임의의 정수
print(random.randrange(1, 10, 2))   # 1~10 임의의 홀수, randint() 와 차이는 옵션을 줄수 있다.
print(random.random())              # 0이상 1미만의 임의의 실수

if random.random() < 0.5:           # 50% 확률
    print('안녕하세요')
else:
    print('다음에 만나요')

s = [1, 2, 3, 4, 5]
print(random.choice(s))             # 시퀀스 자료형에서 임의의 값 리턴
print('sample():', random.sample(s, 3))             # 시퀀스 자료형에서 임의의 값을 매개변수개수만큼 리턴
print('sample():', random.sample(range(1, 47), 6))  # 로또 번호 생성
# random.shuffle(수정가능한시쿼스자료형)
# 주의 : 반환값이 없으며 자료형의 값을 변경 시킨다.
s = [5, 2, 4, 3, 1]
random.shuffle(s)
print('random.shuffle(s):', s)

##### 기본예제 02
# [실행예]
# 주사위 값은 얼마일까요? >>> 1
# 오답입니다. 다시 시도하세요.
# 주사위 값은 얼마일까요? >>> 3
# 오답입니다. 다시 시도하세요.
# 주사위 값은 얼마일까요? >>> 5
# 5! 정답입니다.
# [힌트]
# random.randint(1, 6)

import random

dice = random.randint(1, 6)
while True:
    user = int(input('주사위 값은 얼마일까요? >>> '))
    if dice == user:
        print('{}! 정답입니다.'.format(dice))
        break
    else:
        print('오답입니다. 다시 시도하세요.')