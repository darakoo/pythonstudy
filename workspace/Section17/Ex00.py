
# 예외 종류(예외 발생하기)
# ZeroDivisionError: division by zero
# 0으로 나눌 수 없다.
print(2/0)

'''
# IndexError: list index out of range
a = [1, 2, 3]
print(a[3])

# TypeError: unsupported operand type(s) for /: 'str' and 'int'
a = '3'
b = 2
print(a / b)

# 고전적인 예외 처리 방식
a = int(input('나누 어질 수를 입력하세요>>>'))
b = int(input('나눌 수를 입력하세요>>>'))

if b == 0:
    print('0으로 나누는 것은 불가능 합니다.')
else:
    print(a/b)

# 예외 처리 방식
# 모든 예외를 처리하는 방식
a = int(input('나누 어질 수를 입력하세요>>>'))
b = int(input('나눌 수를 입력하세요>>>'))

try:
    print(a/b)
except:
    print('예외가 발생했습니다.')

# 기본예제 01 풀기

# 특정 예외만 처리하는 방식
a = int(input('나누 어질 수를 입력하세요>>>'))
b = int(input('나눌 수를 입력하세요>>>'))

try:
    print(a/b)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except Exception:
    print('알 수 없는 예외가 발생했습니다.')

# 예외 메시지 처리하기
# 지금까지는 예외 메시지를 직접 만들어서 사용했다. 
# 하지만 예외는 기본저그로 예외 메시지를 가지고 있다.
a = [1, 2, 3, 4, 5]
try:
    a[10]
except IndexError as e:
    print(e)

# else 문과 finally문
try:
    a = int(input('나누어 질 수를 입력하세요>>>'))
    b = int(input('나눌 수를 입력하세요>>>'))

    result = a / b
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)   
else:
    print(a / b)
finally:
    print('프로그램을 종료 합니다.')

# 기본예제 02 풀기

# 강제로 예외 발생 시키기
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

# Section 20
# ./addressBook01.csv
# ./Section20/addressBook01.py
# 위 파일 전달

# ppt 설명, 문제 설명
