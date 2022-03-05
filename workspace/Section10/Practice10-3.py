# [문제]
# student = '"김철수", 85'
# 이 데이터를 각각 name과 score 변수에 저장하세요.
# [실행예]
# 이름은 김철수이고, 점수는 85점입니다.
# [힌트]
# split() : 문자열 분리
# strip() : 문자열 제거

student = '"김철수",85'
name = student.split(',')[0].strip('"')
age = student.split(',')[1]
print('이름은 {}이고, 점수는 {}점입니다.'.format(name, age))

# 응용
name = list()
score = list()
student = ['"김철수",85', '"아무개",90', '"홍길동",75']
for n in range(len(student)):
    name.append(student[n].split(',')[0].strip('"'))
    score.append(int(student[n].split(',')[1]))
print(name)
print(score)