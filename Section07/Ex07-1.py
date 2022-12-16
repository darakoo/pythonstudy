# for문과 문자열

a = {'a', 'b', 'c'}
a = ['a', 'b', 'c']
a = 'hello'
a = ('a', 'b', 'c')
for ch in a:
    print(ch)


'''
# 기본 문제
# 다음은 문자열 자료형의 비밀번호를 입력받아서 숫자와 문자가 모두 포함 되었는지 확인한 뒤 
# 모두 포함되어 있으면 '가능한 비밀번호입니다.' 아니면 '불가능한 비밀번호입니다.'를 출력하는 프로그램입니다.
ch_count = 0
num_count = 0

pwd = input('비밀번호를 입력하세요 >>> ')
for ch in pwd:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호입니다.')
'''