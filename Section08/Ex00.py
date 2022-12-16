# break문
# break 위치 중요, 
n = 1
while n <= 10:
    if n == 5:
        break
    print(n, end=" ")
    n += 1
print()
# continue 문
for n in range(1, 10):
    if n % 3 != 0: # 3의 배수인지 검사합니다.
        continue
    print(n, end=" ")
