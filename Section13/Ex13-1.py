#===== 텍스트 파일 쓰기
# 파일명만 지정할 경우는 열기한 폴더가 root가 된다.
# 파일명 생성시 \'를 사용할 경우 \\'으로 처리해야 한다.

# file = open('C:/dev/python/pythonstudy/workspace/Section13/hello.txt', 'wt', encoding='utf-8')
# file = open('./Section13/hello.txt', 'wt', encoding='utf-8')
# file.write('안녕하세요.')
# file.write('\n')
# file.write('반갑습니다.')
# file.write('\n')
# file.close()

# 텍스트 파일에 내용 추가하기
# file = open('./Section13/hello.txt', 'at', encoding='utf-8')
# file.write('내용을 추가합니다.')
# file.write('\n')
# file.close()


'''
[실행예]
오늘의 스케줄을 입력하세요 >>> 장보기
오늘의 스케줄을 입력하세요 >>> 업무마무리
오늘의 스케줄을 입력하세요 >>> 책대출
오늘의 스케줄을 입력하세요 >>>

현재날짜로 파일생성 => '2020-10-22.txt'
[힌트]
time.strftime('%Y-%m-%d') => 2020-10-22
'''

import time

file = open('./Section13/' + time.strftime('%Y-%m-%d') + '.txt', 'at', encoding="utf-8")
while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>> ')
    # if schedule == '':
    if not schedule:
        break
    file.write(schedule + '\n')

file.close()
