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


# 타이핑하면서 작성해본다.

class Computer:

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))


desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX1060', '512GB')
desktop.hardware_info()
print()
notebook = Computer()
notebook.set_spec('i5', '8GB', 'MX300', '256GB')
notebook.hardware_info()
