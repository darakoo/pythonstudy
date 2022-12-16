def get_grade(count):
    if count == 6:
        return 1
    elif count == 5:
         return 2
    elif count == 4:
         return 3
    elif count == 3:
         return 4
    elif count == 2:
         return 5
    else:
         return 6   

def solution(lottos, win_nums):
    answer = []
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    count = 0
    for i in range(0, 6):
        for j in range(0, 6):
            if lottos[i] == win_nums[j]:
                count += 1

    # first = get_grade(count + lottos.count(0))
    # second = get_grade(count)

    first = rank[count + lottos.count(0)]
    second = rank[count] 

    answer = [first, second]
    return answer


result = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
print(result)