# skip
# [문제]
# 현재 10000원을 가지고 있습니다. 얼마를 사용할 것인지 반복해서 입력받아 10000원을 모두 사용하세요. 
# 0이하의 금액은 사용할 수 없으며, 현재 가지고 있는 돈보다 더 큰 금액도 사용할 수 없습니다.
# [실행예]
# 현재 10000원이 있습니다.
# 사용할 금액 입력 >>> 5000
# 현재 5000원이 있습니다.
# 사용할 금액 입력 >>> -5000
# 0 이하의 금액은 사용할 수 없습니다.
# 현재 5000원이 있습니다.
# 사용할 금액 입력 >>> 6000
# 1000원이 부족합니다.
# 현재 5000원이 있습니다.
# 사용할 금액 입력 >>> 4000
# 현재 1000원이 있습니다.
# 사용할 금액 입력 >>> 1000
# 현재 0원이 있습니다.
# [힌트]
# 문한루프와 break문 활용

money = 10000
while True:
    print('현재 {}원이 있습니다.'.format(money))
    if money == 0:
        break
    spend = int(input('사용할 금액 입력 >>> '))
    if spend <= 0:
        print('0 이하의 금액은 사용할 수 없습니다.')
    elif spend > money:
        print('{}원이 부족합니다.'.format(spend - money))
    else:
        money -= spend