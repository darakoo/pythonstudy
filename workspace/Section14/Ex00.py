##### 파일복사
# 소스파일 전달 후 분석
# 파이썬 홈피에서 로고 이미지 저장후 테스트
# org_file_name = './Section14/code.mp4'
# new_file_name = './Section14/code_new.mp4'

# org_file_name = './Section14/python-logo@2x.png'
# new_file_name = './Section14/python-logo@2x_new.png'

# buffer_size = 1024
# with open(org_file_name, 'rb') as source:       # file io에서는 보통 with구문을 사용한다. 별도 close() 하지 않아도 된다.
#     with open(new_file_name, 'wb') as copy:
#         while True:
#             buffer = source.read(buffer_size)
#             if not buffer:
#                 break
#             copy.write(buffer)
# print(org_file_name + ' 파일이 복사 되었습니다.')


##### csv파일
# csv 파일읽고 터미널에 출력하기
# file_name = './Section14/학생명단.csv'
# student_all = []
# student_one = []

# with open(file_name, 'rt') as file:
#     file.readline()         # 타이틀을 먼저 읽어 출력에서 제외한다.
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         student_one = line.split(',')
#         # student_one = line
#         student_all.append(student_one)
# print(student_all)

# csv 모듈로 csv 파일 생성하기
# import csv
# file_name = './Section14/차량관리.csv'
# with open(file_name, 'w', newline='', encoding='utf-8') as file:
#     csv_maker = csv.writer(file, delimiter=',')
#     csv_maker.writerow([1, '08러1234', '2020-10-20 14:00'])
#     csv_maker.writerow([2, '12다1234', '2020-10-20 14:00'])
#     csv_maker.writerow([3, '67노1234', '2020-10-20 14:00'])
# print(file_name + ' 파일이 생성되었습니다.')

# csv 모듈로 csv 파일 읽기
# import csv
# file_name = './Section14/차량관리.csv'
# with open(file_name, 'r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     for line in csv_reader:
#         print(line)


##### json 파일 입출력
# json 파일 생성
# import json
# dict_list = [
#     {
#         'name':'james',
#         'age':20,
#         'spec':[
#             175.5,
#             70.5
#         ]
#     },
#     {
#         'name':'alice',
#         'age':22,
#         'spec':[
#             168.5,
#             60.5
#         ]
#     }
# ]
# json_string = json.dumps(dict_list)
# file_name = './Section14/dictList.json'
# with open(file_name, 'w') as file:
#     file.write(json_string)
# print(file_name + '파일이 생성 되었습니다.')

# json 파일 읽기
# import json
# file_name = './Section14/dictList.json'
# with open(file_name, 'r') as file:
#     json_reader = file.read()
#     dict_list = json.loads(json_reader)
# for dic in dict_list:
#     print('이름:{}'.format(dic['name']))
#     print('나이:{}'.format(dic['age']))
#     print('키:{}'.format(dic['spec'][0]))
#     print('몸무게:{}'.format(dic['spec'][1]))
#     print()


