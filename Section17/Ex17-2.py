# hello.txt 파일명을 읽어서 터미널에 출력하기
# 물음표 채우기

'''
# else문과 finally문
try:
    filename = input('열고자 하는 파일명을 입력하세요 >>> ')
    file = open(filename, '??', encoding='???')
except ???:
    print(f'{filename} 파일이 존재하지 않습니다.')
????:
    # 정상처리
    buffer = file.read()
    print(buffer, end='')
    print()
    file.close()
???????:
    print('프로그램을 종료합니다.')
'''
################################################################33    
try:
    filename = input('열고자 하는 파일명을 입력하세요 >>> ')
    file = open(filename, 'rt', encoding='utf-8')
except FileNotFoundError:
    print(f'{filename} 파일이 존재하지 않습니다.')
else:
    buffer = file.read()
    print(buffer, end='')
    print()
    file.close()
finally:
    print('프로그램을 종료합니다.')
