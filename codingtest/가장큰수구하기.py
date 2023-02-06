
def solution(array):
    answer = []
    max1 = max(array) # 최대값(max)
    for n in range(len(array)): # 최대값의 인덱스값
        if array[n] == max1:
            idx = n
            break
    answer.append(max1)
    answer.append(idx)
    return answer

print(solution([1, 8, 3]))
