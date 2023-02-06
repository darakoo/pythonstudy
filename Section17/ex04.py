# 예외 처리 : else 문과 finally문

try:
    a = int(input('나누어 질 수를 입력하세요>>>'))
    b = int(input('나눌 수를 입력하세요>>>'))
    result = a / b  # 예외가 발생할 수 있는 구문
except ZeroDivisionError as e:  # 변수 b가 0일 경우
    print('0으로 나눌수 없습니다. ', e)
except ValueError as e:         # 변수 a, b가 정수가 아닐 경우 ???
    print('숫자를 입력하세요. ', e)   
else:       # 예외가 발생하지 않으면 처리되는 구문
    print(result)
finally:
    print('프로그램을 종료 합니다.')