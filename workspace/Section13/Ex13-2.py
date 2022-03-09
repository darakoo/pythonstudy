# 엄마돼지아기돼지.txt, 소스 전달 후 테스트 해보기
# 소스 분석하기
# IDE 인코딩 처리로도 안되는 경우는 encoding='utf-8' 옵션 추가한다.

file = open('.\Section13\엄마돼지아기돼지.txt', 'rt', encoding='utf-8')

line_list = file.readlines()
print(line_list)
count = 0
for line in line_list:
    for ch in line:
        if ch == '꿀':
            count += 1

print('꿀은 전체 {}번 나타납니다.'.format(count))
