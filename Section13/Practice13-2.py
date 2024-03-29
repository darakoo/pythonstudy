'''
[문제]
연락처.txt 파일에 저장된 연락처 중에서 011 을 010 으로 변경하세요.
[실행예]
총 2건의 011 데이터를 찾았습니다.
모든 데이터를 수정했습니다.
[연락처.txt]
"김나라", "목포시", "010-1111-1111"
"이나라", "서울시", "011-2222-2222"
"오나라", "전주시", "010-3333-3333"
"정나라", "속초시", "011-4444-4444"
"유나라", "제주시", "010-5555-5555"
'''


file_name = './Section13/연락처.txt'

# 파일 읽기
file = open(file_name, 'rt')
file_content = file.read()
file.close()

# count, replace 
count = file_content.count('011-')
file_content = file_content.replace('011-', '010-')

# 파일 쓰기
file = open(file_name, 'wt')
file.write(file_content)
file.close()

# 터미널 출력
print('총 {}건의 011 데이터를 찾았습니다.'.format(count))
print('모든 데이터를 수정했습니다.')
