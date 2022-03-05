##### 문자열 메소드
# format()
# 지금 배워도 잊어 버리기 때문에 필요시 찾아서 사용

# count() : 문자열에 포함된 특정 문자열의 개수를 반환
s = 'best of best'
print(s.count('best'))
print(s.count('best', 5))

# find() : 찾고자 하는 문자열의 인덱스를 반환, 없으면 -1
s = 'apple'
print(s.find('l'))
print(s.find('z'))
s = 'best of best'
print("s.find('best', 5) : ", s.find('best', 5))

# index() : find() 와 동일, 찾는 문자열이 없을 경우 오류발생

# 대소문자 변환 메소드
s = 'BEST of best'
print(s.upper())    
print(s.lower())
print(s.capitalize())
print(s)                # 주의 : s의 값이 변경된 것은 아니다.

# join() : 객체의 요소사이에 문자열을 포함시켜 새로운 문자열을 만들고 반환
s = '-'.join('python')
print(s)
s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

# split() : 하나의 문자열을 분리하여 리스트로 반환
s = 'Life is too short'
s = s.split()
print(s)
s = '010-1111-2222'
s = s.split('-')
print(s)

# replace() : 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환
s = 'Life is too short'
s = s.replace('short', 'long')
print(s)
s = '010-1111-2222'
s = s.replace('-', '')
print(s)

# 불필요한 문자열 제거 메소드 : 문자열의 양끝에 있는 공백을 제거
s = '   apple   '
s = s.lstrip()
s = s.rstrip()
s = s.strip()
print(len(s))

s = '<head'
s = s.strip('<')
print(s)


##### 리스트 메소드
# append()
my_list = ['apple', 'banana']
my_list.append('cherry')

# extend()
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango'])

# insert()
my_list = ['apple', 'banana']
my_list.insert(0, 'cherry')

# clear()
my_list = ['apple', 'banana']
my_list.clear()

# pop()
my_list = ['apple', 'banana']
my_list.pop()

# remove()
my_list = ['apple', 'banana']
my_list.remove('apple')

##### 세트 메소드
# 교집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
# s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

# 합집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
# s3 = s1 | s2
s3 = s1.union(s2)
print(s3)

# 차집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
# s3 = s1 - s2
s3 = s1.difference(s2)
print(s3)