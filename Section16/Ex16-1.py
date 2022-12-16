#1. 생성자와 소멸자

#1) 생성자
# 생성자 없는 클래스 만들기
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color

# candy = Candy()
# candy.set_info('cicle', 'brown')
# print(candy.shape)
# print(candy.color)

# 생성자 있는 클래스 만들기
# '__' 로 시작 하는 메소드들은 파이썬에 의해서 미리 기능과 역할이 부여된 메소드를 의미한다.
class Candy:
    # 생성자 : 객체를 생성하고 값을 초기화 한다.
    def __init__(self, shape, color) -> None:
        print('init called')
        self.shape = shape
        self.color = color
    # 소멸자 : 프로그램이 종료되면 자동으로 호출된다.
    def __del__(self):
        print('del called')

candy = Candy('square', 'blue')
print(candy.shape)
print(candy.color)

# 2) 소멸자
del candy


# [문제]
# 다음은 생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램입니다.
class USB:
    def __init__(self, capacity):
        self.capacity = capacity    
    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)
usb.info()

# [문제] skip
# 다음은 생성자와 소멸자를 이용해서 서비스 안내 메세지를 출력하는 프로그램입니다.
class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))
    def __del__(self):
        print('{} Service가 종료되었습니다.'.format(self.service))
s = Service('길 안내')
del s