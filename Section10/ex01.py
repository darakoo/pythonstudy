##### 문자열 메소드

# count() : 문자열에 포함된 특정 문자열의 개수를 반환
print('count()')
s = 'best of best'
print(s.count('best'))
print(s.count('best', 5))

# find() : 찾고자 하는 문자열의 인덱스를 반환, 없으면 -1
print('find()')
s = 'apple'
print(s.find('l'))
print(s.find('z'))

# index() : find() 와 동일, 찾는 문자열이 없을 경우 오류발생

# 대소문자 변환 메소드
s = 'BEST of best'
print('upper:', s.upper())    
print('lower:', s.lower())
print('capitalize:', s.capitalize())
print(s)                # 주의 : s의 값이 변경된 것은 아니다.

# join() : 객체의 요소사이에 문자열을 포함시켜 새로운 문자열을 만들고 반환
print('join()')
s = '-'.join('python')
print(s)
s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

# split() : 하나의 문자열을 분리하여 리스트로 반환
print('split()')
s = 'Life is too short'
s = s.split()
print(s)
s = '010-1111-2222'
s = s.split('-')
print(s)

# replace() : 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환
print('replace()')
s = 'Life is too short'
s = s.replace('short', 'long')
print(s)
s = '010-1111-2222'
s = s.replace('-', ':')
print(s)

# 불필요한 문자열 제거 메소드 : 문자열의 양끝에 있는 공백을 제거
print('strip()')
s = '   apple   '
print(':' + s.lstrip() + ':')
print(':' + s.rstrip() + ':')
print(':' + s.strip() + ':')
print(':' + s + ':')        # s는 변경되지 않는다.

s = '<head<'
s = s.strip('<')
print(s)

# find()
print('find()')
a = '951211-1234567'
print(a.find('-'))

# format()
# 지금 배워도 잊어 버리기 때문에 필요시 찾아서 사용
print("10자리 폭 왼 쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼 쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자 '{:*^10d}'".format(123))
