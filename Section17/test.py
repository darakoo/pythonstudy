try:
    a = 343.342
    b = 3
    result = a / b  # 예외가 발생할 수 있는 구문
except ZeroDivisionError as e:  # 변수 b가 0일 경우
    print(e)
except ValueError as e:         # 변수 a, b가 정수가 아닐 경우
    print(e)   
else:       # 예외가 발생하지 않으면 처리되는 구문
    print(result)
finally:
    print('프로그램을 종료 합니다.')