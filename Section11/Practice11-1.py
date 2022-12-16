'''
[문제]
잔액을 리턴하는 자판기 프로그램을 구현하세요.
[실행예]
잔액은 1600입니다.
[함수정의]
함수이름 : vending_machine(money, price, count)
매개변수 : 자판기에 넣을 돈, 음료수 가격, 뽑을 음료수 수량
반환값 : 잔액(balance)
'''

def vending_machine(money, price, count):
    balance = money - count * price

    return balance

result = vending_machine(3000, 700, 2)
print('잔액은 {}입니다.'.format(result))
