'''
[문제]
아래와 같이 출력되게 코딩하세요. 선언된 변수를 사용하세요.
[실행예]
이름을 입력하세요 >>> 홍길동
나이를 입력하세요 >>> 28
입력된 이름은 홍길동입니다.
입력된 나이는 28살입니다.
'''

name = input('이름을 입력하세요 >>>')
age = input('나이를 입력하세요 >>>')

print(f'입력된 이름은 {name}입니다.')
print(f'입력된 나이는 {age}살입니다.')