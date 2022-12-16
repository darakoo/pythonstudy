'''
[문제]
구구단 2단부터 9단까지 출력하는 프로그램입니다.
중첩 while문을 사용하세요.
출력문 : print('{}×{}={}'.format(dan, n, dan * n))
[실행예]
2×1=2
2×2=4
2×3=6
...
9×7=63
9×8=72
9×9=81
'''

dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print('{}×{}={}'.format(dan, n, dan * n))
        n += 1
    dan += 1
