# NameError 예외 클래스
'''
class NameError(Exception):
    # ?????

# 로직구현
try:
    name = input('이름을 입력하세요 >>> ')
    # 입력받은 이름이 2~6자 사이가 아니면 NameError 예외 발생 시키기(예외메시지:이름은 2~6 글자 입니다.)
    # ???
except NameError as e:
    print(e)
else:
    print('입력된 이름은 {}입니다.'.format(name))
'''

#############################################################3
class NameError(Exception):

    def __init__(self, message):
        super().__init__(message)


try:
    name = input('이름을 입력하세요 >>> ')
    if len(name) < 2 or len(name) > 6:
        raise NameError('이름은 2~6자 사이로 입력해 주세요.')
except NameError as e:
    print(e)
else:
    print('입력된 이름은 {}입니다.'.format(name))
