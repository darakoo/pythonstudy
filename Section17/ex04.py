# 강제로 예외 발생 시키기 skip
# 예를 들어 시험점수를 정수로 입력받는데 음수를 입력할 경우는 현실적으로 문제가 될 수 있습니다. 
try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print('발생한 예외 메시지는 다음과 같습니다.')
    print(e)
'''

# 기본예제 03

# 사용자 예외 클래스
# 예외 클래스를 직접 만들기
class HourError(Exception):
    def __init__(self, message='올바른 시간이 아닙니다.'):
        super().__init__(message)

try:
    hour = int(input('시간을 입력하세요>>>'))
    if hour < 0 or hour > 23:
        # raise HourError()
        raise HourError('시간오류')
except HourError as e:
    print(e)

# 기본 예제 04

# 응용 예제 

#============== section20 주소록 프로젝트
# 구글 파이썬/프로젝트개요/주소록프로젝트개요 ppt 설명 
# addressBook.py : 완성본
# addressBook01.py : 교육생 문제풀이용 전달
# addressBook01.csv : 교육생 문제풀이용 전달
'''
