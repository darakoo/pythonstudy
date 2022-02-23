# 시퀀스 연산자
# *, space 를 이용하여 크리스마스 트리 형태 출력
# [실행예]
#     *
#    ***
#   *****
#  *******
# *********

tree = '*'
space = ' '
print(space * 4 + tree * 1)
print(space * 3 + tree * 3)
print(space * 2 + tree * 5)
print(space * 1 + tree * 7)
print(space * 0 + tree * 9)
