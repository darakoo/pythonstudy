'''
[문제]
점수를 입력받아서 학점을 출력하는 프로그램을 구현하세요. 
학점은 점수가 100~90점이면 'A', 89~80점이면 'B', 79~70점이면 'C', 69~60점이면 'D', 59~0점이면 'F'입니다.
'''

score = int(input('점수를 입력하세요>>>'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')