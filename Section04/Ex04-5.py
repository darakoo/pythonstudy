# 시퀀스 연산자

'''
[문제]
시퀀스 연산자를 이용하여 크리스마스 트리를 출력 하세요.
[실행예]
    *
   ***
  *****
 *******
*********
[힌트]
'''


tree = '*'
space = ' '
print(space * 4 + tree * 1)
print(space * 3 + tree * 3)
print(space * 2 + tree * 5)
print(space * 1 + tree * 7)
print(space * 0 + tree * 9)
