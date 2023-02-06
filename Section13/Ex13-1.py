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
    if not schedule: # if schedule == '':
        break
    file.write(schedule + '\n')

file.close()
