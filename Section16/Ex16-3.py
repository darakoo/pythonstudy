#3. 상속
# 어떤 클래스가 가지고 있는 기능을 그래로 물려받아서 사용할때 상속받는다라고 한다.
# 상속 관계 있을 때/ 없을 때 기능 비교 
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self, food):
        print(self.name + '가 ' + food + '를 먹습니다.')
    
    def sleep(self):
        print(self.name + '가 자고 있습니다.')

class Student(Person):
    def __init__(self, name, school) -> None:
        super().__init__(name)
        self.school = school
    
    def study(self):
        print(self.name + '는 ' + self.school + '에서 공부를 합니다.')

stu1 = Student('철수', 'sbs')
stu1.eat('사과')
stu1.study()
stu1.sleep()

stu2 = Student('영희', 'sbs')
stu2.eat('딸기')
stu2.study()
stu2.sleep()

##### 기본예제 04

##### 응용예제

##### 주소록 프로젝트
