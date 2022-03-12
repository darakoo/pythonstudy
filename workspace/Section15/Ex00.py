'''
##### 함수를 이용한 학생정보 출력
def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)

name1 = 'emily'
department1 = 'computer engineering'
professor1 = 'james'
phone1 = '010-1111-2222'
address1 = 'seoul'
grade1  = 'A'
student_info(name1, department1, professor1, phone1, address1, grade1)

name2 = 'alice'
department2 = 'computer engineering2'
professor2 = 'david'
phone2 = '010-3333-5555'
address2 = 'daegu'
grade2 = 'A+'
student_info(name2, department2, professor2, phone2, address2, grade2)

##### 학생정보를 객체를 사용하여 변경시
# 코드를 간략히 할 수 있다.
class Student:
    pass

student1 = Student('alice', 'computer engineering2', 'david', '010-3333-5555', 'daegu', 'A') 
student2 = Student('alice', 'computer engineering2', 'david', '010-3333-5555', 'daegu', 'A') 

student_info(student1)
student_info(student2)

##### NamingRule 설명

##### 클래스 정의와 객체 생성
# 클래스, 객체 설명
class WaffleMachine:
    pass

waffle = WaffleMachine()
print(waffle)
'''

##### 클래스의 구성
# 클래스의 기본구성
# 값(변수) : 이름, 나이, 연락처, 주소 등
# 기능(메소드) : 잔다, 먹는다, 공부한다, 달린다 등

# 인스턴스 변수와 인스턴스 메소드
class Person:
    def who_am_i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address
boy = Person()
boy.who_am_i('john', 15, '123-1234', 'toronto')
print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)

##### 기본예제 01

