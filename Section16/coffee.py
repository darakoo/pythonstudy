# 상속관계도 구현하기

'''
[문제]
Espresso : 부모 클래스
- 속성 : bean
- 기능 : taste_info
Americano : 자식 클래스
- 속성 : water
- 기능 : americano_info
Latte : 자식 클래스
- 속성 : milk
- 기능 : latte_info
'''

class Espresso:
    def __init__(self, bean):
        self.bean = bean
    def espresso_info(self):
        print('원두 맛은 쓰다')

class Americano(Espresso):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water
    def americano_info(self):
        print(f'원두: {self.bean}')
        print(f'물: {self.water} ml')

class Latte(Espresso):
    def __init__(self, bean, milk):
        super().__init__(bean)
        self.milk = milk
    def latte_info(self):
        print(f'원두: {self.bean}')
        print(f'우유: {self.milk} ml')

americano = Americano('콜롬비아', 50)
americano.americano_info()
americano.espresso_info()  # 부모(Espresso)정보

latte = Latte('베트남', 30)
latte.latte_info()
latte.espresso_info()      # 부모(Espresso)정보
