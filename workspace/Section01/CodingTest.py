# 내적 풀이1
# def solution(a, b):
#     answer=0
#     n = len(a)
#     for i in range(n):
#         answer += a[i] * b[i]
#     return answer

# 내적 풀이2
def solution(a,b):
    n = len(a) 
    return sum([a[i]*b[i] for i in range(n)])

a = [1,2,3,4]	
b = [-3,-1,0,2]
result = solution(a, b)
print(result)
