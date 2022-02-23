# [문제]
# 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 그 숫자만큼 '과일이름'을 입력받아 
# 'basket'리스트에 저장하는 프로그램을 구현하세요.
# [실행예]
# 몇 개의 과일을 보관할까요? >>> 5
# 1번째 과일을 입력하세요 >>> 사과
# 2번째 과일을 입력하세요 >>> 바나나
# 3번째 과일을 입력하세요 >>> 체리
# 4번째 과일을 입력하세요 >>> 오렌지
# 5번째 과일을 입력하세요 >>> 망고
# 입력 받은 과일들은 ['사과', '바나나', '체리', '오렌지', '망고']입니다.
# [힌트]
# 리스트에 값을 저장할때 listname.append()


count = int(input('몇 개의 과일을 보관할까요? >>> '))
basket = []
for n in range(count):
    fruit = input('{}번째 과일을 입력하세요 >>> '.format(n + 1))
    basket.append(fruit)
print('입력 받은 과일들은 {}입니다.'.format(basket))
