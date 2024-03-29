# [문제]
# 저장된 비밀번호를 맞히는 프로그램을 구현하세요. 저장된 비밀번호는 'qwert'이며 최대 5번 시도할 수 있습니다.
# 5번 이내에 비밀번호를 맞히면 '비밀번호를 맞혔습니다.' 그렇지 않으면 '비밀번호 입력 횟수를 초과했습니다.'
# 를 출력하세요.
# [실행예]
# 비밀번호를 입력하세요 >>> 12345
# 비밀번호를 입력하세요 >>> asdfg
# 비밀번호를 입력하세요 >>> qwerty
# 비밀번호를 맞혔습니다.


# 비밀번호를 입력하세요 >>> 12345
# 비밀번호를 입력하세요 >>> zxcv
# 비밀번호를 입력하세요 >>> hjk
# 비밀번호를 입력하세요 >>> tyuio
# 비밀번호를 입력하세요 >>> ghjk
# 비밀번호 입력 횟수를 초과했습니다.

answer = '1234'
count = 1
while True:
    if count > 5:
        print('비밀번호 입력 횟수를 초과했습니다.')
        break
    pwd = input('비밀번호를 입력하세요 >>> ')
    if pwd == answer:
        print('비밀번호를 맞혔습니다.')
        break
    count += 1
