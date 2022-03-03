# break문
# break 위치 중요, 
n = 1
while True:
    if n == 10:
        break

    print(n)
    n += 1

# continue 문
for n in range(1, 31):
    if n % 3 == 0: # 3의 배수인지 검사합니다.
        continue
    print(n)