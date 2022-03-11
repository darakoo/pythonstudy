# [문제]
# 로또 추첨 프로그램을 다음 지시사항을 따라 구현하세요.
# [지시사항]
# 1. 1~45사이의 모든 정수를 순서대로 pot리스트에 저장합니다.
# 2. 다음 과정을 6번 반복합니다.                         
#     - pot 리스트를 무작위로 썩어줍니다.                         
#     - pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
#     - 당첨번호를 출력합니다. 
#     - 2초 동안 잠시 멈춥니다.                                     
# 3. jackpot 리스트의 모든 요소를 오름차순 정렬합니다.             
# 4. jackpot 리스트의 모든 요소를 출력합니다.      
# [실행예]
# 1번째 당첨번호는 38입니다.
# 2번째 당첨번호는 14입니다.
# 3번째 당첨번호는 28입니다.
# 4번째 당첨번호는 41입니다.
# 5번째 당첨번호는 3입니다.
# 6번째 당첨번호는 24입니다.
# 이번 당첨번호는 [3, 14, 24, 28, 38, 41] 입니다.
                
# [지시사항]
# 1. 1~45사이의 모든 정수를 순서대로 pot리스트에 저장합니다.                    => 내포 리스트 : pot = [n for n in range(1, 46)]
# 2. 다음 과정을 6번 반복합니다.                                                => for
#     - pot 리스트를 무작위로 썩어줍니다.                                       => random.shuffle()
#     - pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.     => 리스트명.pop()
#     - 2초 동안 잠시 멈춥니다.                                                 => time.sleep(2)
# 3. jackpot 리스트의 모든 요소를 오름차순 정렬합니다.                          => 리스트명.sort()
# 4. jackpot 리스트의 모든 요소를 출력합니다.                                   => print()

import random
import time

pot = [n for n in range(1, 46)]
jackpot = []
for n in range(1, 7):
    random.shuffle(pot)
    pick = pot.pop()
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick)
    time.sleep(1)
jackpot.sort()
print('이번 당첨번호는 {} 입니다.'.format(jackpot))
