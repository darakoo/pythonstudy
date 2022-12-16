# [문제]
# 구구단을 출력하세요.
# [실행예]
# [2단]
# 2x1=2
# 2x2=4
# 2x3=6
# ......
# 9x8=72
# 9x9=81


# # 구구단 출력 (중첩 for문 이용) 
# for dan in range(2, 10):
#     print(f'[{dan}단]')
#     for n in range(1, 10):
#         print('{}x{}={}'.format(dan, n, dan * n))

# # 짝수단만 출력(위 코드에서 continue문 사용)
# for dan in range(2, 10):
#     if dan%2 == 1:
#         continue

#     print(f'[{dan}단]')
#     for n in range(1, 10):
#         print('{}x{}={}'.format(dan, n, dan * n))

# 구구단 출력 (while문 중요!!!)
n1 = 2
while n1 <= 9:
    print(f'[{n1}단]')
    n2 = 1
    while n2 <= 9:
        print('{}x{}={}'.format(n1, n2, n1 * n2))
        n2 += 1
    n1 += 1
