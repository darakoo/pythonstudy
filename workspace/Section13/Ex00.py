# 텍스트 파일 인코딩 설정 체크하기
# Preferences - Settings -Text Editor - Files - Auto Guess Encoding
# 파일 - 기본설정 - 텍스트 편집기 - 파일 - Auto Guess Encoding
# 한글 입출력에서 깨짐 현상이 있을 경우 옵션추가하기 : encoding='utf-8' 

##### 파일 출력
# 텍스트 파일 생성하기
# 파일명만 지정할 경우는 열기한 폴더가 root가 된다.
# 한글처리시 encoding 설정을 한다.

# file = open('C:/dev/python/pythonstudy/workspace/Section13/hello.txt', 'wt')
# file = open('./Section13/hello.txt', 'wt')
# file.write('안녕하세요.')
# file.write('\n')
# file.write('반갑습니다.')
# file.write('\n')
# file.close()

# 텍스트 파일에 내용 추가하기
# file = open('./Section13/hello.txt', 'at')
# file.write('내용을 추가합니다.')
# file.write('\n')
# file.close()

##### 기본예제 01


##### 텍스트 파일 입력(파일 읽기)
### read()
# file = open('./Section13/hello.txt', 'rt')
# str = file.read()
# print(str)
# file.close()

### readline()
# 먼저 반복문을 빼고 한줄만 읽어본다.
# file = open('./Section13/hello.txt', 'rt')
# while True:
#     str = file.readline()
#     if str == '':
#         break
#     print(str, end='')
# file.close()

### readlines() - 실습1
# file = open('./Section13/hello.txt', 'rt')
# line_list = file.readlines()
# print(line_list)
# for line in line_list:
#     print(line, end='')
# file.close()

### readlines() - 실습2
# file = open('./Section13/hello.txt', 'rt')
# line_list = file.readlines()
# for no, line in enumerate(line_list):
#     print('{}: {}'.format(no+1, line), end='')
# file.close()

##### 응용문제0번 먼저 풀기 
