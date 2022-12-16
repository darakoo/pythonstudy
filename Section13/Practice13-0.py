'''
교재에 없는 문제
[미션]
1단계 : 함수없이 파일 생성코드만 완성
2단계 : 파일 생성을 함수로 구현, 매개변수 week 추가하기
3단계 : 폴더 생성하기 함수로 구현하기, 매개변수 directory 추가하기
4단계 : 1주차주간보고.txt => 01주차주간보고.txt 숫자부분을 2자리로 파일명 변경하기


[문제]
당신의 회사에는 매주 작성해야할 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
1주차.txt 부터 20주차.txt 파일까지 만드세요.
== X 주차 주간보고 ==
부서 : 
이름 :
업무 요약 : 
'''

import os

# 디렉토리 생성
def createFolder(directory):       
    if not os.path.exists(directory):            
        os.makedirs(directory)    

# 파일 생성
def createFile(totalweek):
    contents = '주차 주간보고\n부서 : \n이름 : \n업무요약 : \n'
    for week in range(0, totalweek):
        # 파일명 만들기
        if week < 9:
            file_name = directory + '/0' + str(week+1) + '주차.txt'
        else:
            file_name = directory + '/' + str(week+1) + '주차.txt'

        # 파일에 쓰기
        with open(file_name, 'wt') as file:
            file.write(str(week+1) + contents)



# print(os.getcwd())      # 현재 디렉토리 경로
directory = './Section13/weekly'
createFolder(directory)
createFile(10)
