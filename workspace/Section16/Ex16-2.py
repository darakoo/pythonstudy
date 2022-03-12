# [문제]
# 다음은 생성자와 소멸자를 이용해서 서비스 안내 메세지를 출력하는 프로그램입니다.

class Service:
    
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{} Service가 종료되었습니다.'.format(self.service))

s = Service('길 안내')
del s
