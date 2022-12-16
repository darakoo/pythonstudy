'''
[파일명:pr04-2]
[문제]
1분은 60초이고, 1시간은 60분입니다. 따라서 1시간은 3600초입니다. 
임의의 초를 입력받아 해당 초를 시, 분, 초로 변환하여 출력하는 프로그램을 구현하세요.
[실행예]
초를 입력하세요 >>> 3690
변환 결과는 1시간 1분 30초입니다.
[힌트]
산술연산자 // %  활용
'''

times = int(input('초를 입력하세요 >>> '))
hour = times // 3600
minute = times % 3600 // 60
second = times % 60
print('변환 결과는 {}시간 {}분 {}초입니다.'.format(hour, minute, second))
