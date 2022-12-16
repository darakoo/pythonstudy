# [문제:클래스 메소드]
# 가게 의 매출을 구할 수 있는 Shop 클래스를 완성 하세요

# [실행예]
# 매출: 9500원

'''
class Shop:
    total = 0
    menu_list = [
        {'떡볶이': 3000},
        {'순대': 3000},
        {'튀김': 500},
        {'김밥': 2000}
    ]
    # ???
    def sales(???):
        for menu in cls.menu_list:
            if food in menu:
                ??? # total 클래스 변수에 매출을 누적하기

Shop.sales('떡볶이', 1)  # 떡볶이를 1개 판매
Shop.sales('김밥', 2)  # 김밥을 2개 판매
Shop.sales('튀김', 5)  # 튀김을 5개 판매
print(f'매출: {???}원')  # 매출: 9500
'''


##########################
class Shop:

    total = 0
    menu_list = [
        {'떡볶이': 3000},
        {'순대': 3000},
        {'튀김': 500},
        {'김밥': 2000}
    ]
    
    @classmethod
    def sales(cls, food, count):
        for menu in cls.menu_list:
            if food in menu:
                cls.total += (menu[food] * count)


Shop.sales('떡볶이', 1)  # 떡볶이를 1개 판매
Shop.sales('김밥', 2)  # 김밥을 2개 판매
Shop.sales('튀김', 5)  # 튀김을 5개 판매
print('매출: {}원'.format(Shop.total))  # 매출: 9500