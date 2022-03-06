# [문제]
# 자판기 프로그램을 구현하세요.
# [실행예]
# 3000원을 받았습니다. 음료수 2잔을 주문하였습니다.
# 거스름돈은 1600입니다.
# [힌트]
# def vending_machine(money, count):
#     juice_price = 700
#     balance = ???        # 잔액

#     ???
#     ???

# vending_machine(3000, 2)



def vending_machine(money, count):
    juice_price = 700
    balance = money - count * juice_price

    print('{}원을 받았습니다. 음료수 {}잔을 주문하였습니다.'.format(money, count))
    print('거스름돈은 {}입니다.'.format(balance))

vending_machine(3000, 2)
