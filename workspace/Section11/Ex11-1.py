# [실행예]
# (1, 2)의 합은 3입니다.
# (1, 2, 3)의 합은 6입니다.
# (1, 2, 3, 4)의 합은 10입니다.
# [힌트]
# 함수명 : adder()
# sum() : 합계구하기


def adder(*args):
    print('{}의 합은 {}입니다.'.format(args, sum(args)))

adder(1, 2)
adder(1, 2, 3)
adder(1, 2, 3, 4)
