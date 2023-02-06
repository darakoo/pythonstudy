
def solution(array):
    count = 0
    s = ""
    # 리스트를 문자열로 합치기
    for n in range(len(array)):
        s += str(array[n])
        
    # 문자 "7"의 개수 구하기
    for n in range(len(s)):
        if s[n] == "7":
            count += 1
    return count

print(solution([77, 99, 22]))

