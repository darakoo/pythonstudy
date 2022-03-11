# [문제]
# 과목의 평균을 구현하세요.
# [실행예]
# 과목의 평균은 85.0점입니다.
# [함수정의]
# 함수이름 : get_average()
# 매개변수 : dict 자료형의 과목별 점수
# 반환값 : 평균

# marks = {'국어': 90, '영어': 80, '수학': 85}
# 함수호출 : get_average(marks)

# [힌트:딕셔너리에서 키,값을 얻는 방법을 재 확인]
# marks = {'국어': 90, '영어': 80, '수학': 85}
# for subject in marks:
#     print(subject, marks[subject])

def get_average(marks):
    total = 0   
    for subject in marks:
        total += marks[subject]
    average = total / len(marks)
    return average

marks = {'국어': 90, '영어': 80, '수학': 85}
average = get_average(marks)
print('과목의 평균은 {}점입니다.'.format(average))
