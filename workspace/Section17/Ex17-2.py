# Section17/Ex01.py 파일명을 읽어서 터미널에 출
'''
try:
    filename = input('열고자 하는 파일명을 입력하세요 >>> ')
    file = open(filename, '??', encoding='???')
except ???:
    print('{} 파일이 존재하지 않습니다.'.format(filename))
???:
    # 정상처리
    buffer = file.read()
    print(buffer, end='')
    print()
    file.close()
???:
    print('프로그램을 종료합니다.')
'''
################################################################33    
try:
    filename = input('열고자 하는 파일명을 입력하세요 >>> ')
    file = open(filename, 'rt', encoding='utf8')
except FileNotFoundError:
    print('{} 파일이 존재하지 않습니다.'.format(filename))
else:
    buffer = file.read()
    print(buffer, end='')
    print()
    file.close()
finally:
    print('프로그램을 종료합니다.')
