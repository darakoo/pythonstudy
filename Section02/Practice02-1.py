'''
[파일명:pr02-1]
[문제]
student = '31025'
위와 같이 학번이 변수로 선언되었을 때 학년, 반, 번호로 나누어 출력하세요.
[실행예]
3 학년 10 반 25 번
[힌트]
문자열 인덱싱과 슬라이싱
'''

student = '31025'
grade_no = student[0]
class_no = student[1:3]         # 뒷자리 인덱스는 포함하지 않는다.
stu_no = student[-2:]            # stu_no = student[-2:] 도 가능합니다.
print(grade_no, '학년', class_no, '반', stu_no, '번')
