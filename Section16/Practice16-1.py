# skip

# [문제:생성자, 소멸자]
# 전체 인구수를 저장할 수 있는 Person 클래스를 완성 하세요
# [실행예시]
# james is born.
# emily is born.
# 전체 인구수: 2명
# james is dead.
# emily is dead.
# 전체 인구수: 0명

# 클래스 구현부
class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        # 객체가 생성될 때 population 1 증가
        ???
        print('{} is born.'.format(self.name))

    def __del__(self):
        # 객체가 소멸될때 population 1 감소
        ???
        print('{} is dead.'.format(self.name))

    # population을 반환하는 get_population() 클래스 메소드를 구현 하세요.
    ???

# # 클래스 호출부
# man = Person('james')
# woman = Person('emily')
# print('전체 인구수: {}명'.format(Person.get_population()))
# del man
# print('전체 인구수: {}명'.format(Person.get_population()))

#####################################

class Person: 
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1
        print('{} is born.'.format(self.name))

    def __del__(self):
        Person.population -= 1
        print('{} is dead.'.format(self.name))

    @classmethod
    def get_population(cls):
        return cls.population

man = Person('James')
woman = Person('Alice')
print('전체 인구수: {}명'.format(Person.get_population()))
del man
print('전체 인구수: {}명'.format(Person.get_population()))