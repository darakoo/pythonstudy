# for문과 range
# range(초기값, 종료값, 증감값))
# 초깃값부터 종료값 이전까지 숫자들의 컬렉션을 만든다.
# (초깃값 <= n <종료값)
# 초깃값 생략시 0부터 시작
# 종료값은 생략불가
# 증감값 생략시 1씩 증가
print('for문과 range')
print(type(range(5)))               # range는 타입이 list와 같은 시퀀스 자료형이 아니다. 따라서 출력시 list, tuple 등으로 변환해야 한다.
print(list(range(5)))               # 위 규칙을 보고 예상되는 값을 작성하세요.
print(list(range(1, 11)))
print(list(range(1, 10, 2)))

# while문과 다르게 증감값을 생략해도 된다.
for n in range(1, 11, 2):
    print(n)
for n in range(10):
    print(n, 'hello')


'''
# 기본문제
# 다음은 출력하고자 하는 구구단을 입력받아 해당 구구단을 출력하는 프로그램입니다.
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print('{} x {} = {}'.format(dan, n, dan * n))
'''