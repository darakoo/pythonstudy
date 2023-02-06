# 예외 처리하기

# 예외 처리1 : except
a, b = 3, 0
try:
    print(a/b)
except:
    print('예외가 발생했습니다.')

# 예외 처리2 : 예외메세지 출력
# a, b = 3, 0 
a, b = 'a', 0 
try:
    print(a/b)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
    print('예외:', e)
except Exception as e:
    print('알 수 없는 예외가 발생했습니다.')
    print('예외:', e)

