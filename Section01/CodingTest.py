# 음양 더하기 함수
def solution(absolutes, signs):
    sum = 0
    for idx in range(len(absolutes)):
        if signs[idx] :
            sum += absolutes[idx]
        else:
            sum += absolutes[idx] * (-1)
            
    answer = sum
    return answer

# 함수호출
a = [4, 7, 12]
b = [True, False, True]	
result = solution(a, b)
print(result)

# 내적 풀이1
# def solution(a, b):
#     answer=0
#     n = len(a)
#     for i in range(n):
#         answer += a[i] * b[i]
#     return answer

# 내적 풀이2
# def solution(a,b):
#     n = len(a) 
#     return sum([a[i]*b[i] for i in range(n)])

# a = [1,2,3,4]	
# b = [-3,-1,0,2]
# result = solution(a, b)
# print(result)
