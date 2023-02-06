#===== 텍스트 파일 읽기

#===== read()
file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
str = file.read()
print(str)
file.close()

#===== readline()
# 먼저 반복문을 빼고 한줄만 읽어본다.
file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
# 방법1
while str != '':
    str = file.readline()
    print(str, end='')

# 방법2
while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')
file.close()

#===== readlines()
file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
line_list = file.readlines()
for line in line_list:
    print(line.strip('\n'))     # 문자열 끝에 개행을 없앤다.
file.close()

#===== readlines()
file = open('./Section13/hello.txt', 'rt', encoding='utf-8')
line_list = file.readlines()
for no, line in enumerate(line_list):
    print(f'{no+1}: {line}', end='')

for line in enumerate(line_list):
    print(f'{line[0]+1}: {line[1]}', end='')
file.close()

