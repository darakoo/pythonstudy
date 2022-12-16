'''
[파일명:pr04-5]
[문제]
국,영,수 점수를 입력 받아 평균을 구하고, 평균이 80점 이상이면 '합격', 아니면 '불합격'을 출력하는 프로그램을 구현하세요.
[실행예]
국어 점수를 입력하세요 >>> 85
영어 점수를 입력하세요 >>> 83
수학 점수를 입력하세요 >>> 81
평균은 83.0점이고, 결과는 합격입니다.
'''

kor = int(input('국어 점수를 입력하세요 >>> '))
eng = int(input('영어 점수를 입력하세요 >>> '))
mat = int(input('수학 점수를 입력하세요 >>> '))
avg = (kor + eng + mat) / 3
result = '합격' if avg >= 80 else '불합격'
print('평균은 {}점이고, 결과는 {}입니다.'.format(avg, result))
