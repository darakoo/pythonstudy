#=====인수(argument)와 매개변수(parameter)
# 인수 : 실제값
# 매개변수 : 변수

# 매개변수가 있는 함수
def introduce(name, age):   # 매개변수
    print('내 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))

# 함수에 넘겨주는 값을 인수라고 한다.
introduce('james', 25)      

# 가변 매개변수
# args type 확인하기
def add(*args):
    print(f'{args}의 합은 {sum(args)}입니다.')

add(1,2)
add(1,2,3)
add(1,2,3,4)

# 디폴트 매개변수
def greet(message='안녕하세요'):
    print(message)

greet('반갑습니다')     # 반갑습니다
greet()                # 안녕하세요

