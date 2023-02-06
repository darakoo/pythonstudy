##### 문자열 관련 내장 함수

# chr() : 유니코드를 문자로
print(chr(48))
print(chr(49))
print(chr(50))
print(chr(51))

# ord() : 문자를 유니코드로
print(ord('0'))
print(ord('a'))

# eval() : 문자열로 전달된 표현식의 결과값을 반환하는 함수
exp = '100 + 200'
print(f'{exp} = {eval(exp)}')


# format() : 숫자 포멧팅
print(format(10000))
print(format(10000, ','))

# str() : 전달받은 인수를 문자열로 변환
n = 1.5
print(str(n))
