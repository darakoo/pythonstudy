# [문제]
# 무지개의 일곱 색깔을 저장하는 rainbow 리스트를 생성하고 다음과 같이 출력하세요.
# [실행예]
# 무지개의 1번째 색은 red입니다.
# 무지개의 2번째 색은 orange입니다.
# 무지개의 3번째 색은 yellow입니다.
# 무지개의 4번째 색은 green입니다.
# 무지개의 5번째 색은 blue입니다.
# 무지개의 6번째 색은 navy입니다.
# 무지개의 7번째 색은 purple입니다.
# [힌트]
# enumerate()

# 첫 번째 풀이입니다.
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for no, color in enumerate(rainbow):
    print('무지개의 {}번째 색은 {}입니다.'.format(no + 1, color))
    
print()

# 두 번째 풀이입니다.
for idx in range(len(rainbow)):
    print('무지개의 {}번째 색은 {}입니다.'.format(idx + 1, rainbow[idx]))
