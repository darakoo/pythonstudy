'''
[문제]
임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요.
[실행예]
n1 입력>>>300
n2 입력>>>23
n3 입력>>>567
가장 큰 수는 567입니다.
[힌트]
max 변수 이용하세요.
'''

n1 = int(input('정수1 입력>>>'))
n2 = int(input('정수2 입력>>>'))
n3 = int(input('정수3 입력>>>'))

# max를 n1으로 초기화
max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3

# max를 0으로 초기화 할 경우
max = 0
if n1 > max:
    max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3

print('가장 큰 수는 {}입니다.'.format(max))