# [문제]
# 학생의 점수를 입력받아 평균, 최고, 최저 점수를 구하는 성적 계산 프로그램을 구현하세요.
# 음수를 입력하면 입력이 종료됩니다.
# 입력받은 모든 점수는 exam 리스트에 저장합니다.
# [실행예]
# 점수 입력 >>> 80
# 점수 입력 >>> 50
# 점수 입력 >>> 60
# 점수 입력 >>> 30
# 점수 입력 >>> 90
# 점수 입력 >>> -1
# 평균 = 62.0, 최대 = 90, 최소 = 30
# [힌트]
# 수학 내장 함수이용

exam = []
while True:
    score = int(input('점수 입력 >>>'))
    if score < 0:
        break
    exam.append(score)

avg = sum(exam) / len(exam)
max = max(exam)
min = min(exam)
print('평균 = {}, 최대 = {}, 최소 = {}'.format(avg, max, min))
