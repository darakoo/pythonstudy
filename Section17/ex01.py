# 예외 종류 살펴보기

# IndexError: list index out of range
a = [1, 2, 3]
print(a[3])

# TypeError: unsupported operand type(s) for /: 'str' and 'int'
a = '3'
b = 2
print(a / b)

# ZeroDivisionError: division by zero
# 0으로 나눌 수 없다.
a, b = 3, 0
print(a/b)
