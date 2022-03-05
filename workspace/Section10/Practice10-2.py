# 소스 제공후 condition3, 4 조건을 추가 할 수 있도록 하기

# [문제]
# 사업자등록 번호(예: 123-45-67890)를 입력받아서 형식이 맞는지 점검하는 프로그램을 구현하세요. 
# 하이픈의 위치와 글자수를 점검합니다.
# [실행예]
# 사업자등록번호를 입력하세요(예: 123-45-67890) >>> 123-45-67890
# 올바른 형식입니다.

# 사업자등록번호를 입력하세요(예: 123-45-67890) >>> 123-4567-12
# 올바른 형식이 아닙니다.
# [힌트]

no = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')

condition1 = (no.find('-') == 3)
condition2 = (no.find('-', 4) == 6)
if condition1 and condition2:
    print('올바른 형식입니다.')
else:
    print('올바른 형식이 아닙니다.')

# condition3 = (len(no) == 12)
# condition4 = (no.replace('-', '').isdecimal())