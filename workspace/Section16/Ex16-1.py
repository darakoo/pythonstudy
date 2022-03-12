# [문제]
# 다음은 생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램입니다.

class USB:

    def __init__(self, capacity):
        self.capacity = capacity    

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)
usb.info()
