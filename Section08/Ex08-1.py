'''
[문제]
대한민국의 수도를 맞히는 프로그램입니다. 정답을 맞힐때까지 프로그램은 종료되지 않습니다.
[실행예]
대한민국의 수도는 어디인가요? >>> 부산
오답입니다. 다시 시도하세요.
대한민국의 수도는 어디인가요? >>> 서울
정답입니다.
'''

capital = ['서울', 'seoul', 'SEOUL']
while True:
    city = input('대한민국의 수도는 어디인가요? >>> ')
    city = city.strip()
    #if city in capital:
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요.')
