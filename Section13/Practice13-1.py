'''
[문제]
나라별 수도를 저장한 리스트의 내용을 nation.txt 파일명으로 생성 하세요.
[nation.txt]
그리스-그리스
독일-독일
러시아-러시아
미국-미국
'''

# 첫 번째 풀이
nations = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
file = open('./Section13/nation.txt', 'wt', encoding='utf-8')
for index in range(0, len(nations), 2):
    file.write(nations[index] + '-' + nations[index + 1]  + '\n')
file.close()

# 두 번째 풀이
# nations = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
# file = open('nation.txt', 'wt', encoding='utf-8')
# for index, country in enumerate(nations):
#     if index % 2 == 0:
#         file.write(nations[index] + '-' + nations[index + 1]  + '\n')
# file.close()

# 파일 읽기
print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
file = open('nation.txt', 'rt', encoding='utf-8')
line_list = file.readlines()
print(line_list)
for line in line_list:
    print(line, end='')
file.close()
