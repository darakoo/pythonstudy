'''
[문제]
range 함수를 사용하여 아래와 같이 출력 되도록 프로그램을 구현하세요.
[실행예]
5 4 3 2 1 
1 2 3 4 5
[힌트]
range()
'''

for n in range(5, 0, -1):
    print(n, end=' ')
print()
for n in range(5):
    print(n+1, end=' ')