# [문제]
# 오늘의 스케줄을 입력하면 해당 내용으로 파일이 생성됩니다.
# 내용을 입력하지 않고 엔터를 치면 입력이 종료된다.
# 파일명은 현재날짜이며 '2020-10-22.txt' 이다.

# 주의
# 파일명 생성시 \'를 사용할 경우 \\'으로 처리해야 한다.
# IDE 인코딩 처리로도 안되는 경우는 encoding='utf-8' 옵션 추가한다.

import time

# file = open('./Section13/' + time.strftime('%Y-%m-%d') + '.txt', 'at', encoding="utf-8")
file = open('./Section13/' + time.strftime('%Y-%m-%d') + '.txt', 'at', encoding="utf-8")
while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>> ')
    if not schedule:
        break
    file.write(schedule + '\n')

file.close()
