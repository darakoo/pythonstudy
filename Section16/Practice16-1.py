'''
[문제:생성자, 소멸자]
전체 인구수를 저장할 수 있는 Person 클래스를 완성 하세요
[실행예시]
james is born.
emily is born.
전체 인구수: 2명
james is dead.
emily is dead.
전체 인구수: 0명
'''

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