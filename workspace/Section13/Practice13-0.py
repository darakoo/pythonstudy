# 교재에 없는 문제
# 응용문제를 풀지 않고 아래 문제를 푼후 마무리한다.
# [문제]
# 당신의 회사에는 매주 작성해야할 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# 1주차.txt 부터 20주차.txt 파일까지 만드세요.
# == X 주차 주간보고 ==
# 부서 : 
# 이름 :
# 업무 요약 : 

for n in range(1, 21):
    file_name = './Section14/' + str(n) + '주차.txt'
    with open(file_name, 'wt') as file:
        # pass
        file.write(' == ' + str(n) + ' 주차 주간보고 ==')
        file.write('부서 : ')
        file.write('이름 : ')
        file.write('업무 요약 : ')