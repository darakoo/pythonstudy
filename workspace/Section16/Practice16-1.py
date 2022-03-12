# [문제]
# 전체 인구수를 저장할 수 있는 Person 클래스를 완성 하세요
# [실행예시]
# james is born.
# emily is born.
# 전체 인구수: 2명
# james is dead.
# emily is dead.
# 전체 인구수: 0명

class Person:
    
    population = 0

    def __init__(self, name):
        self.name = name
        # 클래스 변수인 population 값을 1 증가 시킨다.
        print('{} is born.'.format(???))

    def __del__(self):
        # 클래스 변수인 population 값을 1 감소 시킨다.
        print('{} is dead.'.format(???))

    @classmethod
    def get_population(cls):
        return cls.population


man = Person('james')
woman = Person('emily')
print('전체 인구수: {}명'.format(Person.get_population()))
del man
del woman
print('전체 인구수: {}명'.format(Person.get_population()))

#####################################

# class Person:
    
#     population = 0

#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print('{} is born.'.format(self.name))

#     def __del__(self):
#         Person.population -= 1
#         print('{} is dead.'.format(self.name))

#     @classmethod
#     def get_population(cls):
#         return cls.population


# man = Person('james')
# woman = Person('emily')
# print('전체 인구수: {}명'.format(Person.get_population()))
# del man
# print('전체 인구수: {}명'.format(Person.get_population()))