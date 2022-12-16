'''
[파일명:pr03-4]
[문제]
3명의 학생으로부터 수학여행지를 입력 받아 출력하세요.
단, 동일한 장소의 입력은 무시합니다.
[실행예]
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌
조사된 수학여행지는 {'제주', '민속촌'}입니다.
[힌트] 
중복데이타를 허용하지 않는 데이터 타입을 사용하세요.
'''

s = set()
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
print('조사된 수학여행지는 {}입니다.'.format(s))
