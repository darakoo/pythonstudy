# [문제]
# [실행예]
# 전화번호를 입력하세요 >>> 02-1234-5678
# 1234
# [힌트]
# split()

phone = input('전화번호를 입력하세요 >>> ')
code = phone.split('-')[1]
print(code)
# code = phone.split('-')
# print(code[1])
