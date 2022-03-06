# [실행예]
# 커피를 선택하세요. (아아, 뜨아, 라떼) >>> 라떼
# 얼마를 내시나요? >>> 10000
# 10000원에 라떼를 선택하셨습니다.
# 잔돈 : 8000원, 메뉴 : 라떼
'''
[힌트]
def coffee_machine(money, coffee):
    menu = {
        '아아': 1000,
        '뜨아': 1500,
        '라떼': 2000
    }

    return 잔액, 메뉴명
'''

def coffee_machine(money, coffee):
    print('{}원에 {}를 선택하셨습니다.'.format(money, coffee))
    menu = {
        '아아': 1000,
        '뜨아': 1500,
        '라떼': 2000
    }
    # return money-menu[coffee], coffee

    if coffee not in menu:
        return money, '없는메뉴입니다.'
    elif menu[coffee] > money:
        return money, '금액이부족합니다.'
    else:
        return money - menu[coffee], coffee

order = input('커피를 선택하세요. (아아, 뜨아, 라떼) >>> ')
pay = int(input('얼마를 내시나요? >>> '))

change, coffee = coffee_machine(pay, order)
print('잔돈 : {}원, 메뉴 : {}'.format(change, coffee))
