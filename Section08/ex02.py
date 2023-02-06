# continue 문
# continue 아래 명령은 실행하지 않는다.

# 3의 배수는 출력하지 마세요.
for n in range(1, 10):
    if n % 3 == 0:
        continue 
    
    print(n, end=", ")
