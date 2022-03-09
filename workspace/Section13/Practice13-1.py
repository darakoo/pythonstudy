# [문제]
# 나라별 수도를 저장한 nation 리스트의 내용을 nation.txt 파일명으로 생성요.
# [파일내용]
# 그리스-그리스
# 독일-독일
# 러시아-러시아
# 미국-미국

nations = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']

file = open('./Section13/nation.txt', 'wt')
for index in range(0, len(nations), 2):
    file.write('{}-{}'.format(nations[index], nations[index]  + '\n'))
file.close()


'''
# 첫 번째 풀이
nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']

print(range(0, len(nation), 2))

file = open('nation.txt', 'wt')
for i in range(0, len(nation), 2):
    file.write('{}-{}\n'.format(nation[i], nation[i + 1]))
file.close()

print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
file = open('nation.txt', 'rt')
line_list = file.readlines()
for line in line_list:
    print(line, end='')
file.close()


# 두 번째 풀이
nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
file = open('nation.txt', 'wt')
for i, country in enumerate(nation):
    if i % 2 == 0:
        file.write('{}-{}\n'.format(nation[i], nation[i + 1]))
file.close()

print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
file = open('nation.txt', 'rt')
line_list = file.readlines()
for line in line_list:
    print(line, end='')
file.close()
'''