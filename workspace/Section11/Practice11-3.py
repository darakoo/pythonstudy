# [문제]
# 축의금 합계를 구하세요. 축의금은 사용자로 부터 입력 받고 입력 종료는 0입니다.
# [실행예]
# 축의금을 입력하세요.종료:0 >>>100000
# 축의금을 입력하세요.종료:0 >>>50000
# 축의금을 입력하세요.종료:0 >>>60000
# 축의금을 입력하세요.종료:0 >>>0
# 전체 축의금: 210,000
# [힌트]
# 함수 정의
# - 반환값 없음
# - 함수이름 gift(축의금)

total = 0

def gift(money):
    global total
    total += money

while True:
    money = int(input('축의금을 입력하세요.종료:0 >>>'))
    
    if money == 0:
        break
    else:
        gift(money)

print('전체 축의금: {}'.format(format(total, ',')))
