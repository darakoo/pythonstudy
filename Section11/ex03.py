#=====반환값
# 반환값이 없는 함수
# 지금까지 한 예제들

# 반환값이 있는 함수
def bigger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
print(bigger(1, 3))

# 다중 반환
# result는 4개의 반환값을 저장하는 튜플입니다.
# 반환값이 가변으로 반환되지는 않는다.
def calculator(*args):
    return sum(args), sum(args)/len(args), max(args), min(args)

a, b, c, d = calculator(1, 2, 3, 4, 5)
print('합계', a)
print('평균', b)
print('최댓값', c)
print('최솟값', d)

result = calculator(1, 2, 3, 4, 5)
print('합계', result[0])
print('평균', result[1])
print('최댓값', result[2])
print('최솟값', result[3])

# 함수 종료를 위한 return
# 값을 반환 한다는 의미가 아니라 함수실행을 종료하는 의미이다.
# 자주 사용되는 기능이다.
def charge(energy):
    if energy < 0:
        print('0보다 작은 에너지는 충전할 수 없습니다.')
        return  # charge( ) 함수의 종료, 아래 코드가 실행되지 않는 것을 확인한다.
    print('에너지가 충전되었습니다.')

charge(1)
charge(-1)



#skip
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
'''