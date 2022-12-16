# 변수, 기본자료형
a = 1
print(type(a))
a = 0.2
print(type(a))
a = True
print(type(a))
a = "hello"
print(type(a))

# 컬렉션 자료형
a = list()
a = []
print(type(a))

a = tuple()
a = ()
print(type(a))

a = set()
print(type(a))

a = dict()
a = {}
print(type(a))

a = [1, 0.2, 'hello', [1,2,3]]
print(a[0:2])
print(a[3])

# 출력함수
sum = 10
print('a + b = {}'.format(sum))
print('a + b = {}'.format('10'))

print(f'a + b = {sum}')

# 입력함수
# a = int(input('첫번째수>>>'))
# b = int(input('두번째수>>>'))
# print(f'{a} + {b} = {a + b}')

# 복합대입연산자
a = 10
a += 100
print(a)

# 관계연산자
# 논리연산자
# 비트연산자
# 시퀀스연산자
# 삼항연산자
a = 17
result = '미성년' if(a >= 19) else '성인'
print(result)