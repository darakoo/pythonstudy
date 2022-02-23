# [문제]
# 1박스에 라면이 20개씩 들어갑니다. 라면이 21개가 있다면 2박스가 있어야 모두 담을 수 있습니다.
# 라면의 개수를 입력받아 라면을 담기 위해서 필요한 박스의 개수를 구하여 출력하는 프로그램을 구현하세요.
# [실행예]
# 라면의 개수를 입력하세요 >>> 50
# 50개 라면을 담으려면 3박스가 필요합니다.
# [힌트]
# 조건연산자(삼항연산자)를 이용하세요.
# (라면개수 % 20) 한 결과가 '0 인경우' 와 '아닌경우' 를 생각해 보세요.


print('한 박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
ramen = int(input('라면의 개수를 입력하세요 >>> '))
box = ramen // 20 if ramen % 20 == 0 else ramen // 20 + 1
print('{}개 라면을 담으려면 {}박스가 필요합니다.'.format(ramen, box))
