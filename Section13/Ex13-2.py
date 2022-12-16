#===== 텍스트 파일 읽기
#===== read()
# file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
# str = file.read()
# print(str)
# file.close()

#===== readline()
# 먼저 반복문을 빼고 한줄만 읽어본다.
file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
# 방법1
# while str != '':
#     str = file.readline()
#     print(str, end='')

# 방법2
# while True:
#     str = file.readline()
#     if str == '':
#         break
#     print(str, end='')
# file.close()

#===== readlines() - 실습1
file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
line_list = file.readlines()
for line in line_list:
    print(line.strip('\n'))     # 문자열 끝에 개행을 없앤다.
file.close()


#===== readlines() - 실습2 skip
# file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
# line_list = file.readlines()
# for no, line in enumerate(line_list):
#     print(f'{no+1}: {line}', end='')

# for line in enumerate(line_list):
#     print(f'{line[0]+1}: {line[1]}', end='')
# file.close()


'''
skip
[문제]
엄마돼지아기돼지.txt 파일을 읽어 '꿀'이라는 글자가 몇번 나오는지 코딩하세요.
[실행예]
꿀은 전체 54번 나타납니다.

# readlines() 이용하여 작성
file = open('.\Section13\엄마돼지아기돼지.txt', 'rt', encoding='utf-8')
line_list = file.readlines()
print(line_list)
count = 0
for line in line_list:
    for ch in line:
        if ch == '꿀':
            count += 1
print(f'꿀은 전체 {count}번 나타납니다.')

# read() 이용하여 작성
file = open('.\Section13\엄마돼지아기돼지.txt', 'rt', encoding='utf-8')
str = file.read()
count = 0
print(str)
for ch in str:
    if ch == '꿀':
        count += 1
print(f'꿀은 전체 {count}번 나타납니다.')
'''
