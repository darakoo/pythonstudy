#2. 클래스 변수, 클래스 메소드, 정적 메소드

#1) 클래스 변수
# 교재 참고
class Korean:
    # 클래스 변수
    country = 'korea'

    # 생성자
    def __init__(self, name, age, address):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.address = address

    # 인스턴스 메소드
    def print_info(self):
        print(f'country is {Korean.country}')
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'address is {self.address}')

man = Korean('Tom', 25, 'goyang si')
woman = Korean('Alice', 25, 'goyang si')

# 인스턴스 변수 접근 방법
# print(Korean.name) # 클래스 이름으로는 접근 안됨
print(man.name)

# 클래스 변수 접근 방법 : 인스턴스, 클래스 이름 둘다 접근 가능
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

#2) 클래스 메소드
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
print("클래스 변수 : " + Korean.country)

#3) 정적 메소드
# self, cls를 사용하지 않기 때문에 인스턴스변수, 클래스변수를 사용하지 않는다.
# 인스턴스를 생성하지 않아도 사용할 수 있다.
class Korean:
    country = 'korea'

    @staticmethod
    def slogan():
        print('Korea Fighting')

Korean.slogan()
