# [문제]
# student = '"김철수", 85'
# 이 데이터를 각각 name과 score 변수에 저장하세요.
# [실행예]
# 이름은 홍길동이고, 점수는 85점입니다.
# [힌트]
# split() : 문자열 분리
# strip() : 문자열 제거

student = '"홍길동",85'
student = student.split(',')
name = student[0].strip('"')
student = student[1]
print('이름은 {}이고, 점수는 {}점입니다.'.format(name, student))

# 응용
student = ('"홍길동",85', '"김길동",90', '"고길동",75')
name = list()
scores = list()
for n in range(len(student)):
    name.append(student[n].split(',')[0].strip('"'))
    scores.append(int(student[n].split(',')[1]))
print(name)
print(scores)