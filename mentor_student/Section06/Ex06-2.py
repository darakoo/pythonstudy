# while문(반복횟수가 정해져 있지 않을 경우)
# 사용자로부터 임의의 정수를 입력받아 모두 리스트에 보관합니다. 
# 단 사용자가 0을 입력하면 더 이상 입력받지 않고 프로그램을 종료합니다. 
# 이때 0은 리스트에 보관하지 않습니다.

my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

# while True:
#     if n == 0:
#         break

#     my_list.append(n)
#     n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

print(my_list)