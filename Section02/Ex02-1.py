##### 주석

'''
1. 파일명: circle.py
2. 개요: 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수
3. 작성자: 홍길동
4. 작성일: 2020-08-25
'''

# math 모듈 포함
import math

# get_area() 함수 정의
def get_area(radius):
    """
    반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수
    사용예) get_area(2)
    """
    area = math.pi * math.pow(radius, 2)
    return area

radius = 1.5
# get_area() 함수 호출 결과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area.__doc__)  # Docstring 확인
