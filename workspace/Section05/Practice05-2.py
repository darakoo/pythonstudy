# [문제]
# 임의의 정수를 입력받은 뒤 해당 값이 3의 배수인지 아닌지 판별하는 프로그램을 구현하세요.
# [실행예]
# 정수를 입력하세요>>>15
# 15은 3의 배수입니다.
# --------------------------
# 정수를 입력하세요>>>14
# 14은 3의 배수가 아닙니다.

n = int(input('정수를 입력하세요>>>'))
if n%3 == 0:
    print('{}는 3의 배수입니다.'.format(n))
else:
    print('{}는 3의 배수가 아닙니다.'.format(n))
