'''
##### 생성자

# 지금까지 클래스를 이용하여 객체를 생성한 방법
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

# 값 없는 인스턴스 생성
candy = Candy()
# 값(인스턴스 변수)을 저장할 수 있는 메소드 호출
candy.set_info('cicle', 'brown')
# __init__() 메소드(생성자)
from itertools import count


class Candy:
    def __init__(self, shape, color) -> None:
        print('init called')
        self.shape = shape
        self.color = color
    
    def __del__(self):
        print('del called')

candy = Candy('square', 'blue')
print(candy.shape)
print(candy.color)

##### 소멸자
del candy

##### 기본예제 01 02 소스 띄우고 타이핑하기

##### 클래스 변수
# 교재 참고
class Korean:
    # 클래스 변수
    country = 'korea'

    def __init__(self, name, age, address) -> None:
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.address = address

man = Korean('gildong', 25, 'goyang si')
woman = Korean('minji', 25, 'goyang si')

# 인스턴스 변수 접근 방법 : 클래스 이름으로는 접근 안됨
print(man.name)
# print(Korean.name)

# 클래스 변수 접근 방법
print(Korean.country)
print(man.country)

# 클래스 변수, 인스턴스 변수 변경 시 값의 변화 확인 하기
# 클래스 변수 접근은 클래스명.클래스변수 으로 하도록 하자
man.name = 'gildong_'
Korean.country = 'korea_'
print(man.name)
print(man.country)
print(woman.name)
print(woman.country)

print(Korean.country)

##### 클래스 메소드
# 클래스 메소드란 클래스 변수를 사용하는 메소드이다.
# 인스턴스를 생성하지 않아도 사용할수 있다.
# @classmethod 쓰지 않으면 오류 발생

class Korean:
    country = 'korea'

    @classmethod
    def trip(cls, country):
        if cls.country == country:
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

Korean.trip('korea')
Korean.trip('japan')

##### 정적 메소드
# self, cls를 사용하지 않기 때문에 인스턴스변수, 클래스변수를 사용하지 않는다.
# 인스턴스를 생성하지 않아도 사용할 수 있다.
class Korean:
    country = 'korea'

    @staticmethod
    def slogan():
        print('Korea Fighting')

Korean.slogan()

##### 기본예제 03

'''
##### 상속
# 어떤 클래스가 가지고 있는 기능을 그래로 물려받아서 사용할때 상속받는다라고 한다.
# 상속 관계 있을 때/ 없을 때 기능 비교 
class Person:

    def __init__(self, name) -> None:
        self.name = name

    def eat(self, food):
        print(self.name + '가 ' + food + '를 먹습니다.')

class Student(Person):

    def __init__(self, name, school) -> None:
        super().__init__(name)
        self.school = school
    
    def study(self):
        print(self.name + '는 ' + self.school + '에서 공부를 합니다.')

student = Student('철수', 'sbs')
student.eat('사과')
student.study()


##### 기본예제 04
