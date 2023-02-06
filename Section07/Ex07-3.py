# 다음은 출력하고자 하는 구구단을 입력받아 해당 구구단을 출력하는 프로그램입니다.
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print('{} x {} = {}'.format(dan, n, dan * n))