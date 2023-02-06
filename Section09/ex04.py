##### 시퀀스 관련 내장 함수

# range() : 시퀀스 데이타를 생성할 수도 있다.
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, 10, 3)))

# len() : 객체의 길이 반환
a = [1,2,3]
print(len(a))

# sorted() : 반복가능객체의 정렬 결과를 반환
print('sorted()')
a = [1,3,9,3,6,7,3]
a = (1,3,9,3,6,7,3)
print(sorted(a))
# print(sorted(a), reverse=True)

# zip() : 여러 개의 반복가능객체의 요소를 튜플로 묶어서 반환
print('zip()')
a = ['korea', 'japan', 'china']
b = [0.9, 0.3, 0.5]
c = [90, 30, 50]
for student in zip(a, b, c):
    print(student)

# enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플 형태(인덱스, 값)로 추출된다.
print('enumerate()')
for item in enumerate([1,2,3]):
    print(item)

# 기본예제
'''
[샐행예]
1월 = 31일
2월 = 28일
...
10월 = 31일
11월 = 30일
12월 = 31일
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print('{}월 = {}일'.format(month + 1, day))
