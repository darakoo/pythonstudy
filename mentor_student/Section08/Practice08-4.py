# [문제]
# 다음 조건을 만족하는 구구단을 출력하세요.
# [실행예]
# 3x1=3
# 3x2=6
# 3x3=9

# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

# 7x1=7
# 7x2=14
# 7x3=21
# 7x4=28
# 7x5=35
# 7x6=42
# 7x7=49

# 9x1=9
# 9x2=18
# 9x3=27
# 9x4=36
# 9x5=45
# 9x6=54
# 9x7=63
# 9x8=72
# 9x9=81
# [힌트]


for dan in range(2, 10):
    if dan % 2 == 0:
        print()
        continue
    for n in range(1, 10):
        if dan < n:
            break
        print('{}x{}={}'.format(dan, n, dan * n))
