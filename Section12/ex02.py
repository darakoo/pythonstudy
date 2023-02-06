# 표준 모듈 : 파이썬에서 기본적으로 제공된다.

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

##### time 모듈
import time
print(time.ctime())    # 형식있는 시간으로 반환
print('time.strftime():', time.strftime('%Y %m %d %a %H:%M:%S'))    # 형식을 갖춘 날짜 데이터(지시자는 교재 참고)
# time.sleep() : 전달된 초만큼 시스템을 일시 중지

##### datetime 모듈
# datetime이 두번 나오는 이유는 모듈안에 클래스가 있을 경우 이다.
import datetime
print(datetime.datetime.now())

