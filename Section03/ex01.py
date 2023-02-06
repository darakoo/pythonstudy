# 출력함수

# 표준출력함수
print('hello')
print('hello', sep=':', end='!')
print('hello')

import sys
f = open('a.txt', 'w')
print(10, 20, 'abc', sep=':', end='\n', file=f, flush=False)

# %연산자 : 형식을 갖춘 문자열
a = 10
b = 20
s = "hello"
print("%d" %a)
print("python %s" %"hello")
print("%s" %s)

# format() 메소드
print("Breakfast is {} and {}".format("meat", "rice"))

# f-strings
food1 = "meat"
food2 = "rice"
print(f"Breakfast is {food1} and {food2}")

age = 25
print(f"내년에는 {age+1}살이 됩니다.")
