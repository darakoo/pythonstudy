# [문제]
# 사용자로부터 0부터9사이의 정수를 입력받습니다. 
# 이때 입력된 정수가 3개가 될 때까지 입력받는 프로그램을 구현하세요.
# 이 때 중복된 값이 입력되면 해당 입력은 무시하세요.
# [실행예]
# [힌트]
# s = set(), len(s)

numbers = set()
while len(numbers) < 3:
    n = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
    numbers.add(n)
print('모두 입력되었습니다.')
print('입력된 값은 {}입니다.'.format(numbers))