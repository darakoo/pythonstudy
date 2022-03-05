# section01~section04 review

# 변수
a = 1
a = 3.14
a = True
a = 'a'

# 인덱싱과 슬라이싱
a = 'hello'
print(a[0])
print(a[0:3])
print(a[3:])

# 컬렉션
a = list()
a.append(1)
a.append('hello')
print(a)
a = tuple()
a = (1,2,3)
print('a[0:2]:', a[0:2])
a = set()
a.add(10)
a.add('20')
print(a)
a = dict()
a['cat'] = '고양이'
a['dog'] = '강아지'
print(a)
a['dog'] = '개'
print(a)

#표준출력
print('hello', 'python',  sep=',', end=':')
print('hello', 'python',  sep=',', end=':')
print()

#형식을 갖춘 문자열
a = 10
b = 20
print('a=%d a=%d' %(a, b))
print('a={}, b={}'.format(a, b))
print(f'a={a}, b={b}')

# 표준입력
# input()
# input('입력하세요>>>')
# a = int(input('입력하세요>>>'))

# 연산자
# 산술
# 대입
a += 10
# 관계
a, b = -1, 20
print('a != b:', a != b)
print('a == b:', a == b)
print('a >= b:', a >= b)

# 논리
a, b = -1, 20
print('a > 0 and b > 0 : ', a > 0 and b > 0)

# 비트
# 시퀀스
print('hello' * 3)
# 기타
a, b = 10, 3
result = (a-b) if(a>=b) else (b-a)
print(result)

# 조건문
if (a>=b and a > 0):
    result = a-b
else:
    result = b-a

