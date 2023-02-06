##### 기본자료형
a1 = 10         # 정수(int) 
a2 = 10.3       # 실수(float)
a3 = "50"       # 문자열(str)
a4 = "hello"    # 문자열(str)
a5 = True       # 논리(bool)

# 자료형 확인하기
print(type(a1 + a2))
print(type(a2))
print(type(a3 + a4))
print(type(a5))

# 연산, 타입변환
print(a1 + int(a3))
print(a2 + float(a3))

# 문자열
s = 'hello'
print(s[0] + s[1] + s[2] + s[3] + s[4])
print(s[-5] + s[-4] + s[-3] + s[-2] + s[-1])
print(s[0:3])   
print(s[-3:])