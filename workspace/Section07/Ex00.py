
# for 변수 in 반복가능객체:
#     반복실행문
# 반복가능객체-시퀀스 : 문자열, list, tuple, range
# 반복가능객체-비시퀀스 : set, dict

# 시퀀스와 for문
a = (1,2,3)
for n in a:
    print(n, end=' ')

a = [1,2,3]
for n in a:
    print(n, end=' ')
    
a = [n*2 for n in [1,2,3]]
print(a)

# range(초기값, 종료값, 증감값))

for n in range(1, 11):
    print(n, end='')
print('')
for n in range(1, 11, 2):
    print(n, end='')
print('')
for n in range(10, 0, -1):
    print(n, end='')

print()

# for n in range(10):
#     print('hello')

# 비시퀀스와 for문
# for문과 세트
person = {  'name':'홍길동', 
            'age':25
            }
for key in person:
    print(key)

for key in person:
    print(person[key])



# for문과 딕셔너리