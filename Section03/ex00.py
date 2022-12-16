
#=====표준출력:이스케이프 문자
#교재 52쪽 이스케이프 문자 설명
#기본예제 3-1

#=====표준출력:print() 함수
print('hello')
print('hello', sep=':', end='!')
print('hello')

import sys
f = open('a.txt', 'w')
print(10, 20, 'abc', sep=':', end='\n', file=f, flush=False)

#기본예제 3-2 skip

#=====형식을 갖춘 문자열 : %연산자
print('형식을 갖춘 문자열')
a = 10
b =20
print('%d' %a) 
print('%f' %3.14) 
print('%s' %'python') 
print('%d, %d' %(a, b))

print('%5d' %123) 
print('%10d' %123)
print('%-5d' %123) 
print('%-10d' %123)
print('%-5.2f' %3.66) 
print('%-10.1f' %3.66)

#기본예제 3-3

#=====형식을 갖춘 문자열 : format() 메소드
print('Breakfast is {} and {}'.format('spam', 'eggs'))
print('Breakfast is {1} and {0}'.format('spam', 'eggs'))
#기본예제 3-4

#=====형식을 갖춘 문자열 : f-strings
who, how = 'you', 'happy'
print(f'{who} make me {how}')
age = 25
print(f'내년에는 {age+1}살이 됩니다.')

#=====표준입력 : input함수, 형변환
print('정수를 입력하세요.')
n = input()
print(n)
print(type(n))
#기본예제 3-5
#기본예제 3-6
