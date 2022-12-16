'''
[문제]
임의의 정수 3개를 입력받아 그 중에서 가장 작은 수를 출력하는 프로그램을 구현하세요.
[실행예]
정수1 입력>>>300
정수2 입력>>>23
정수3 입력>>>567
가장 큰 수는 23입니다.
[힌트]
min 변수 이용하세요.
'''

n1 = int(input('정수1 입력>>>'))
n2 = int(input('정수2 입력>>>'))
n3 = int(input('정수3 입력>>>'))

# min를 n1으로 초기화
min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3

# min를 0으로 초기화 할 경우
# min = 9999999999
# if n1 < min:
#     min = n1
# if n2 < min:
#     min = n2
# if n3 < min:
#     min = n3

print('가장 작은 수는 {}입니다.'.format(min))