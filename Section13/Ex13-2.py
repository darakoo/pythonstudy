'''
[문제]
엄마돼지아기돼지.txt 파일을 읽어 '꿀'이라는 글자가 몇번 나오는지 코딩하세요.
[실행예]
꿀은 전체 54번 나타납니다.
'''

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
