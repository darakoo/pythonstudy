##### 클래스 이해

#===== 사람정보 출력하기 함수 이용
def who_am_i(name, age, tel, address):
        print(f'이름 : {name}, 나이 : {age}, 연락처 : {tel}, 주소 : {address}')

who_am_i('John', 25, '123-1234', 'Toronto')
who_am_i('Alice', 19, '123-1234', 'NewYork')

#===== 사람정보 출력하기 클래스 이용
# 클래스 이름은 Upper Camel 표기법으로 한다. 
class Person:
    def who_am_i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address
boy = Person()
boy.who_am_i('John', 25, '123-1234', 'Toronto')
print(f'이름 : {boy.name}, 나이 : {boy.age}, 연락처 : {boy.tel}, 주소 : {boy.address}')

girl = Person()
girl.who_am_i('Alice', 19, '123-1234', 'NewYork')
print(f'이름 : {girl.name}, 나이 : {girl.age}, 연락처 : {girl.tel}, 주소 : {girl.address}')

