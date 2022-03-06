
# 함수 만들기
# 함수를 먼저 만들고 난 후 호출을 해야 한다.
# 들여쓰기 주의
def welcome():
    print('Hello Python')
    print('Nice to meet you')

welcome()  # welcome() 함수 호출

# 매개변수가 있는 함수
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))

introduce('james', 25)

# 가변 매개변수
# args type 확인하기
def show(*args):
    for item in args:
        print(item)

# show('python') # show 함수 호출, 인수가 1개입니다.
show('happy', 'birthday') # show 함수 호출, 인수가 2개입니다.

# 디폴트 매개변수
# def greet(message='안녕하세요'):
#     print(message)

# greet('반갑습니다')  # 반갑습니다
# greet( )  # 안녕하세요


# def greet(message='안녕하세요', name):   # 오류발생
def greet(name, message='안녕하세요'):
    print('{}님 {}'.format(name, message))

greet('김철수')

############################# 기본예제 01을 풀어본다.

# 반환값이 없는 함수를 출력해본다.
# print(greet('김철수'))

# 반환값이 있는 함수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

print(address())

# 다중 반환
# result는 4개의 반환값을 저장하는 튜플입니다.
# 반환값이 가변으로 반환되지는 않는다.
def calculator(*args):
    return sum(args), sum(args)/len(args), max(args), min(args)

a, b, c, d = calculator(1, 2, 3, 4, 5)
print('합계', a)
print('평균', b)
print('최댓값', c)
print('최솟값', d)

result = calculator(1, 2, 3, 4, 5)
print('합계', result[0])
print('평균', result[1])
print('최댓값', result[2])
print('최솟값', result[3])

# 함수 종료를 위한 return
# 값을 반환 한다는 의미가 아니라 함수실행을 종료하는 의미이다.
# 자주 사용되는 기능이다.
def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전할 수 없습니다.')
        return  # charge( ) 함수의 종료, 아래 코드가 실행되지 않는 것을 확인한다.
    print('에너지가 충전되었습니다.')

charge(1)
charge(-1)
############################# 기본예제 02을 풀어본다.

# 지역변수와 전역변수
# 지역변수
def f():
    a = 10
    print(a)

f()
# print(a) # 접근이 안된다.

# 전역변수
b = 10
def f():
    print(b)

f()
print(b)


# 전역변수의 값을 변경하는 경우
# 전역변수는 반드시 필요한 경우가 아니면 사용하지 않는 것을 추천한다.
a = 0
def f():
    # global a
    a = 10
    print(a)

f()
print(a)