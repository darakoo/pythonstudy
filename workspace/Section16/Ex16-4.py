# [문제]
# 원두를 저장하는 Coffee 클래스와 원두에 물을 썩은 Espresso 클래스를 상속 관계로 구현하였습니다.

class Coffee:

    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))
    
    def taste_info(self):
        print('원두 맛은 쓰다')

class Americano(Coffee):

    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def americano_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))

class Latte(Coffee):

    def __init__(self, bean, milk):
        super().__init__(bean)
        self.milk = milk

    def latte_info(self):
        super().coffee_info()
        print('우유: {}ml'.format(self.milk))

americano = Americano('콜롬비아', 50)
americano.americano_info()
americano.taste_info()
latte = Latte('콜롬비아', 30)
latte.latte_info()
latte.taste_info()
