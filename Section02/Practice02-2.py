'''
[파일명:pr02-2]
[문제]
차량번호 뒷 숫자 4자리만 출력하세요.
[실행예]
서울2가1234 의 차량번호 4자리는 1234 입니다.
10가1234 의 차량번호 4자리는 1234 입니다.
288가1234 의 차량번호 4자리는 1234 입니다.
[힌트]
마이너스 인덱싱
'''

car1 = '서울2가1234'
car2 = '10가1234'
car3 = '288가1234'
car_no1 = car1[-4:]
car_no2 = car2[-4:]
car_no3 = car3[-4:]
print(car1, '의 차량번호 4자리는', car_no1, '입니다.')
print(car2, '의 차량번호 4자리는', car_no2, '입니다.')
print(car3, '의 차량번호 4자리는', car_no3, '입니다.')