# 예외 강제로 발생시키기

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print('발생한 예외 메시지는 다음과 같습니다.')
    print(e)

# 기본예제
# 예외 클래스를 직접 만들고 발생시키기
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
