# 상속관계도 구현하기

class Person: # 슈퍼 클래스
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + '가 먹습니다.')


class Student(Person): # 서브 클래스
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def study(self):
        print(self.name + '는 ' + self.school + '에서 공부를 합니다.')

class HighSchoolStudent(Student): # 서브 클래스
    def __init__(self, name, school, grade):
        super().__init__(name, school)
        self.grade = grade
    def grade_info(self):
        print(self.name + '는 ' + str(self.grade) + '학년 입니다.')

class Worker(Person): # 서브 클래스
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
    def work(self):
        print(self.name + '는 ' + self.company + '에서 일을 합니다.')

st = Student('김영희', '일산고')
st.eat()
st.study()

wo = Worker('홍철수', '고양고')
wo.eat()
wo.work()

hi = HighSchoolStudent('홍철수', '고양고', 3)
hi.eat()
hi.study()
hi.grade_info()

