# skip
# [문제]
# 1부터 99사이의 모든 정수를 대상으로 369게임의 결과를 출력하는 프로그램을 구현하세요.
# [실행예]
# 1       2       짝      4       5       짝      7       8       짝      10
# 11      12      짝      14      15      짝      17      18      짝      20
# 21      22      짝      24      25      짝      27      28      짝      짝
# 짝      짝      짝짝    짝      짝      짝짝    짝      짝      짝짝    40
# 41      42      짝      44      45      짝      47      48      짝      50
# 51      52      짝      54      55      짝      57      58      짝      짝
# 짝      짝      짝짝    짝      짝      짝짝    짝      짝      짝짝    70
# 71      72      짝      74      75      짝      77      78      짝      80
# 81      82      짝      84      85      짝      87      88      짝      짝
# 짝      짝      짝짝    짝      짝      짝짝    짝      짝      짝짝
# [힌트]


for n in range(1, 400):
    units = n % 10
    tens = n // 10
    condition1 = units % 3 == 0 and units != 0
    condition2 = tens % 3 == 0 and tens != 0 
    if condition1 and condition2:
        print('짝짝', end='\t')
    elif condition1 or condition2:
        print('짝', end='\t')
    else:
        print(n, end='\t')
    if n % 10 == 0:
        print()
