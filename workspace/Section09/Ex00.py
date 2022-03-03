##### 문자열 내장 함수
# chr() : 유니코드를 문자로
print(chr(48))
print(chr(49))
print(chr(50))
print(chr(51))

# ord() : 문자를 유니코드로
print(ord('0'))
print(ord('a'))

# eval() : 문자열로 전달된 표현식의 결과값을 반환하는 함수
print(eval('100+200'))

# format() : 숫자 포멧팅
print(format(10000))
print(format(10000, ','))

# str() : 전달받은 인수를 문자열로 변환
print(str(1.5))

##### 숫자 내장 함수
# abs() : 절대값
print(abs(10))
print(abs(-10))

# divmod() : 몫과 나머지를 한쌍의 튜플로 반환 
print('divmod(10,3) =>', divmod(10,3))

# float() : 전달된 인수를 float로 반환
# int() : 전달된 인수를 int로 반환

# max() : 전달된 인수 중 가장 큰 값을 반환
print(max(1,4,6))

# min() : 전달된 인수 중 가장 작은 값을 반환
print(min(1,4,6))

# pow() : 거듭제곱 반환
print(pow(10,2))

# round() : 반올림 반환
print(round(2.555))
print(round(2.675, 2))
print(round(2.645, 2))

# sum() : 반복가능객체(list, tuple)의 합계를 반환
a = [1,2,3]
print(sum(a))

##### 시퀀스 내장 함수
# enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태(인덱스, 값)로 추출된다.
for item in enumerate([1,2,3]):
    print(item)

# range() : 시퀀스 데이타를 생성할 수도 있다.
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, 10, 3)))

# len() : 객체의 길이 반환
a = [1,2,3]
print(len(a))

# sorted() : 반복가능객체의 정렬 결과를 반환
a = [1,3,9,3,6,7,3]
print(sorted(a))
# print(sorted(a), reverse=True)

# zip() : 여러 개의 반복가능객체의 요소를 튜플로 묶어서 반환
names = ['korea', 'japan', 'china']
scores = [90, 30, 50]
for student in zip(names, scores):
    print(student)
