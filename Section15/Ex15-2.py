##### 클래스의  구성과 용어
# 값(변수) : 이름, 나이, 연락처, 주소 등
# 기능(메소드) : 잔다, 먹는다, 공부한다 등

# 클래스 구현
class Person:
    # 인스턴스 메소드
    def who_am_i(self, name, age, tel, address):
        # 인스턴스 변수
        self.name = name    
        self.age = age
        self.tel = tel
        self.address = address
    def sleep(self):
        print('I am sleeping')
    def study(self):
        print('I am studying')       

# 객체(인스턴스)생성
person = Person()

# 생성된 객체를 이용한 메소드 호출
person.who_am_i('john', 15, '123-1234', 'toronto')
person.sleep()
person.study()